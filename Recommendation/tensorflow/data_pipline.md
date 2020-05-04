# Tensorflow之Data pipline

## 背景

之所以有这篇博文，起源于对[FM模型](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)的尝试。

该模型在LR基础之上，对离散化特征进行embedding,使用embedding的内积来作为特征之间的高阶相关性权重。![二阶交叉特征公式](http://latex.codecogs.com/gif.latex?\hat%20y(x)%20=%20w_0%20+%20\sum\limits_{i=1}^{n}%20w_ix_i%20+%20\sum\limits_{i=1}^{n}\sum\limits_{j=i+1}^{n}%20%3Cv_i,%20v_j%3E%20x_ix_j)

具体细节可以参考[晨晨学长这篇博文](http://tech.yuceyi.com/article/1585745474194).

理解完论文之后，就是后面的工程化工作了。秉着不重复造轮子的理念,我们快速找到了论文团队的实现： [libfm](https://github.com/srendle/libfm), 一个使用C++实现的库（[这篇文档帮助我们快速使用libfm](http://d0evi1.com/libfm)）。后来发现效率不够高（我们的train数据集有60+G），所以我们又找了另外一个实现库：[xlearn](https://github.com/aksnzhy/xlearn), 相对来说效率提升了一些。最终通过模型训练也得到了一阶权重和Embedding矩阵，并使用java实现了FM的inference代码。

这两个C++实现库对于我们来说存在以下局限性：

1. 使用C++实现，修改源代码较为困难。
2. 数据无法通过S3进行获取，对本地磁盘存储压力较大。
3. 不利于后面DeepFM等深度模型的改造。
4. 无法支持分布式训练。

## 迁移Tensorflow

考虑到以上痛点，我们选择工业界最为通用的Tensorflow框架进行开发（目前已经是2.0+版本，很多API也修改了，但是考虑到兼容，我们还是继续使用1.13版本）。



