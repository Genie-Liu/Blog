# Expectation Maximization #

1. 单个高斯分布假设

    已知观测到的数据<img src="http://latex.codecogs.com/gif.latex?\bm{x}=\{x_1, x_2 ...\}" />. 若对该数据进行单个高斯分布<img src="http://latex.codecogs.com/gif.latex?\theta(\mu, \sigma)" />的假设，则可有以下log likelyhood ：

    <img src="http://latex.codecogs.com/gif.latex?L(\theta|\bar{x})=log(P(\bar{x}|\theta))=\sum_{i=1}^{n}log(P(x_i|\theta))" />

    <img src="http://latex.codecogs.com/gif.latex?P(x_i|\theta)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{({x_i-\mu})^2}{2\sigma^2}}" />

    找到最可能的高斯分布参数，即<img src="http://latex.codecogs.com/gif.latex?P(\bar{x}|\theta)" />最大. 可以对<img src="http://latex.codecogs.com/gif.latex?L(\theta|\bar{x})"/>求导, 令其为0，解得<img src="http://latex.codecogs.com/gif.latex?\theta" />

2. 对于混合高斯分布，<img src="http://latex.codecogs.com/gif.latex?L(\theta|\bar{x})" />较为复杂，故需要引入EM算法来进行求解


3. EM 算法, 原理为：已知上一参数，迭代求解

    <img src="http://latex.codecogs.com/gif.latex?\theta^{(g+1)}=\mathop{\arg\max}_{\theta}\int_{z}{log(P(x,z|\theta)) * P(z|x, \theta^{(g)})}dz" />







<img src="http://latex.codecogs.com/gif.latex?" />

P(\bar{x}|\theta)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{({\bar{x}-\mu})^2}{2\sigma^2}}

$$\theta^{(g+1)}=\mathop{\arg\max}_{\theta}\int{log(P(x,z|\theta)) * P(z|x, \theta^{(g)})}dz$$




