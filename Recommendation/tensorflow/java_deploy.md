# Tensorflow之Java部署方案

最近使用Tensorflow的Estimator高阶API进行模型训练，支持保存成checkpoint和saved model格式。
其中saved model可以使用[Tensorflow Serving](https://github.com/tensorflow/serving)进行部署.

但是目前公司内部还是使用tensorflow的[Java API](https://www.tensorflow.org/api_docs/java/reference/org/tensorflow/package-summary)进行部署，所以需要把saved model转化成pb格式，
并用Java进行部署。希望后续能够转移到Tensorflow Serving方式部署，毕竟这是官方推荐的部署方式，而且无论从扩展性，
易用性都能得到保证，而Java API直接就告诉你这是Experimental的了, 还不是稳定版。

## saved_model转pb

由于从estimator保存的格式为saved model，所以第一步是需要转成pd格式.
需要注意的是estimator在export_saved_model时，需要指定好对应的placeholder，确保后续有对应的feed的入口。

1. 使用tf.saved_model.loader.load加载saved model格式，其中需要指定tags，而estimator保存saved model时默认tag为'serve'
2. 根据output node来freeze graph。如果我们用了feature column的话，还需要把`init_all_tables`也加入到output node，该问题在github已经被讨论过, 具体见下面的参考资料。
3. 把freeze之后的graph和constants参数序列化为pb文件

```python
# estimator export feed node
input_fn = tf.estimator.export.build_raw_serving_input_receiver_fn({
  "index": tf.placeholder(tf.int32, [None, field_size], name='index'),
  "value": tf.placeholder(tf.float32, [None, field_size], name='value'),
})

estimator.export_saved_model(saved_model_dir, input_fn)
```

```python
def save_model2pb(save_model_dir, pb_path, output_node, tags=['serve']):
  with tf.Session(graph=tf.Graph()) as sess, tf.device("/cpu:0"):
    tf.saved_model.loader.load(sess, tags, save_model_dir)
    output_graph_def = tf.graph_util.convert_variables_to_constants(
        sess=sess,
        input_graph_def=sess.graph_def,
        output_node_names=output_node)

    with tf.gfile.GFile(pb_path, "wb") as f:
      f.write(output_graph_def.SerializeToString())

    print("%d ops in the final graph." % len(output_graph_def.node))
```

## Java部署

Java的部署方式与python类似，对于下面代码，我们的input是value和index，output是output_node

1. 先创建graph和session，以byte的方式读取pb文件
2. 构建用于feed的tensor. 其中用于feed的node需要在estimator保存成saved model时export出来
3. 使用runner进行predict，取出predict结果。


```java
public class DeepModel {

    private Graph graph;
    private Session sess;

    public DeepModel(String pbFile) {
        try {
            graph = new Graph();
            byte[] graphBytes = IOUtils.toByteArray(new FileInputStream(pbFile));
            graph.importGraphDef(graphBytes);
            sess = new Session(graph);
        } catch (java.io.IOException e) {
            System.out.println("DeepModel initial fail!!!");
        }
    }

    public boolean isNull() {
        return (sess == null) || (graph == null);
    }

    public float[][] predict(int[][] index, float[][] value) {
        Tensor indexTensor = Tensor.create(index);
        Tensor valueTensor = Tensor.create(value);

        Tensor rlt = sess.runner().feed("index", indexTensor).feed("value", valueTensor).fetch("output_node").run().get(0);
        float[][] finalRlt = new float[index.length][1];
        rlt.copyTo(finalRlt);
        return finalRlt;
    }
}
```

参考资料：
1. [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)
2. [freeze_graph not initializing tables](https://github.com/tensorflow/tensorflow/issues/8665)