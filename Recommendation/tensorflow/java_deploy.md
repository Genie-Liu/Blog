# Tensorflow之Java部署方案

最近使用Tensorflow的Estimator高阶API进行模型训练，支持保存成checkpoint和saved model格式。
其中saved model可以使用[Tensorflow serving](https://github.com/tensorflow/serving)进行部署.

但是目前公司内部还是使用tensorflow的[java api]()进行部署，所以需要把saved model转化成pb格式的模型，
并用java进行部署。希望后续能够转移到tensorflow serving方式部署，毕竟这是官方推荐的方式，而且无论从扩展性，
易用性都能得到保证。

## saved_model转pb

由于从estimator保存的格式为saved model，所以第一步是需要转成pd格式(注意estimator在export_saved_model时，需要指定好对应的placeholder，确保后续有feed的入口)。

1. 使用tf.saved_model.loader.load加载saved model格式，其中需要指定tags，而estimator保存saved model时默认tag为'serve'
2. 根据output node来freeze graph
3. 保存graph和参数为pb文件

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

## Java部署pb文件

java的部署方式与python类似

1. 先创建graph和session，以byte的方式读取pb文件
2. 构建用于feed的tensor，其中用于feed的node需要在estimator保存成saved model时export出来
3. 


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
            System.out.println("DeepFMModel initial fail!!!");
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