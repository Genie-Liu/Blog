# CTR预估模型之DeepFM

FM模型把稀疏特征映射为K维的隐变量，并且通过隐变量之间的点积来作为两个特征交叉的权重值（当然FM可以做高阶的特征交叉，但是大部分时候我们还是只用二阶部分）。

整体来看FM解决了两个问题：

* 使用特征隐变量内积来模拟两个特征的交叉权重。假如我们有n个特征，则二阶交叉有$n x n$种可能，所以需要训练$n x n$个参数。通过隐变量的方式，我们只需要训练$kxn$个参数

参考资料：
1 [DeepFM: A Factorization-Machine based Neural Network for CTR Prediction](https://arxiv.org/abs/1703.04247)
