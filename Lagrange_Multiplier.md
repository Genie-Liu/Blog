## Lagrange multiplier ##

很多时候我们需要求的表达式的最大值，一般我们都是求导，令其等于0. 但在机器学习的过程中，我们经常遇到在有限制的情况下，最大化表达式. 如下例子所示:

$maximize f(x,y)$ subject to $g(x,y)=0$

这时我们引入一个拉格朗日乘子$\lambda$构造出拉格朗日表达式:

$$\mathcal{L}(x,y,\lambda) = f(x,y) - \lambda \cdot g(x,y)$$

对于有多个限制的表达式，则有:

$$\mathcal{L}(x_1, ..., x_n, \lambda_1, ..., \lambda_M) = f(x_1, ..., x_n) - \sum_{k=1}^{M}\lambda_kg_k(x_1, ..., x_n)$$

接下来要对朗格朗日表达式求导，令其为0

$\Delta_{x,y,\lambda}\mathcal{L}(x,y,\lambda) = 0 \iff \Delta_{x,y}f(x,y) = \lambda \Delta_{x,y}g(x,y)$   &&  $g(x,y) = 0$

$\Delta_{x,y}f = (\frac{\partial{f}}{\partial{x}}, \frac{\partial{f}}{\partial{y}})$

Example:

if we want to maximise $f(x,y) = x + y $ while $x^2 + y^2 = 1$

令 $g(x,y) = x^2+y^2-1$ 则: $\mathcal{L}(x,y,\lambda) = f(x,y) + \lambda \cdot g(x,y) = x + y + \lambda(x^2+y^2-1)$

对拉格朗日表达式求导，则有：
$$1+2\lambda x = 0$$  $$1+2\lambda y = 0$$  $$x^2 + y^2 - 1 = 0$$

求解可得$x,y,\lambda$