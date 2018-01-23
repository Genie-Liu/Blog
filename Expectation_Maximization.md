# Expectation Maximization #

1. 单个高斯分布假设

    已知观测到的数据$\mathbf{x}=\{x_1, x_2 ..., x_n\}$. 若对该数据进行单个高斯分布$\theta(\mu, \sigma^2) $的假设，则可有以下log likelyhood ：

    $L(\theta|\bar{x})=log(P(\bar{x}|\theta))=\sum_{i=1}^{n}log(P(x_i|\theta))$

    $P(x_i|\theta)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{({x_i-\mu})^2}{2\sigma^2}}$

    找到最可能的高斯分布参数，即$P(\bar{x}|\theta)$最大. 可以对$L(\theta|\bar{x})$求导, 令其为0，解得$\theta$

2. 对于混合高斯分布，$L(\theta|\bar{x})$较为复杂，故需要引入EM算法来进行求解


3. EM 算法, 原理为：迭代优化参数，使得$P({x}|\theta)$最大. 迭代方程如下: 可以证明通过如下方法可保证$P({x}|\theta^{(g+1)}) \ge P(x|\theta^{(g)})$. 

    $\theta^{(g+1)}=\mathop{\arg\max}_{\theta}\int_{z}{log(P(x,z|\theta)) * P(z|x, \theta^{(g)})}dz$， 其中z为隐变量

    证明如下：

    贝叶斯公式： $P(x|\theta) = \frac{P(x,z|\theta)}{P(z|x,\theta)}$
        
    两边取对数： $log(P(x|\theta)) = log(P(x,z|\theta)) - log(P(z|x,\theta))$

    以隐变量z为分布求期望： $E(log(P(x|\theta))) = E(log(P(x,z|\theta))) - E(log(P(z|x,\theta)))$

    $\int_z{log(P(x|\theta)) * P(z|x, \theta^{(g)})}dz = \int_z{log(P(x,z|\theta)) * P(z|x, \theta^{(g)})}dz - \int_z{log(P(z|x,\theta)) * P(z|x, \theta^{(g)})}dz $

    Log likelyhood就出来了： $log(P(x|\theta)) = \int_z{log(P(x,z|\theta)) * P(z|x, \theta^{(g)})}dz - \int_z{log(P(z|x,\theta)) * P(z|x, \theta^{(g)})}dz $

    当$\theta$取$\theta^{(g+1)}$时, $\int_z{log(P(x,z|\theta)) * P(z|x, \theta^{(g)})}dz$取到最大值。

    令$H(\theta, \theta^{(g)}) = \int_z{log(P(z|x,\theta)) * P(z|x, \theta^{(g)})}dz$

    如果我们证明了$H(\theta^{(g+1)}, \theta^{(g)}) \le H(\theta^{(g)}, \theta^{(g)})$ 则 $P({x}|\theta^{(g+1)}) \ge P(x|\theta^{(g)})$ 也就证明了.

    $H(\theta^{(g)}, \theta^{(g)}) - H(\theta^{(g+1)}, \theta^{(g)}) = \int_z{log(P(z|x,\theta^{(g)})) * P(z|x, \theta^{(g)})}dz - \int_z{log(P(z|x,\theta^{(g+1)})) * P(z|x, \theta^{(g)})}dz $

    $ = \int_z{log(\frac{P(z|x,\theta^{(g)})} {P(z|x,\theta^{(g+1)})}) * P(z|x, \theta^{(g)})}dz = \int_z{-log(\frac{P(z|x,\theta^{(g+1)})} {P(z|x,\theta^{(g)})}) * P(z|x, \theta^{(g)})}dz$

    为了证明这一点，需要用到Convax函数的知识：$(1-p)*f(x)+p*f(y) \ge f[(1-p)*x + p*y]$

    所以有$\int_z{-log(\frac{P(z|x,\theta^{(g+1)})} {P(z|x,\theta^{(g)})}) * P(z|x, \theta^{(g)})}dz \ge -log(\int_z{\frac{P(z|x, \theta^{(g+1)})} {P(z|x, \theta^{(g)})} * P(z|x, \theta^{(g)})}dz) = 0 $ 

    故EM算法是合理的，注意：隐变量z的选取不能破坏$x_i$的边缘分布




