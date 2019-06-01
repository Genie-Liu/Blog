## Gaussian Mixture Model using EM Algorithm ##

E-M 算法有个典型的应用，就是高斯混合模型，适用于对多个高斯分布的数据进行分类。

Gaussian Mixture Model (k-mixture):

$$p(X|\theta) = \sum_{i=1}^{k}{\alpha_l\mathcal{N}(X|\mu_l, \Sigma_l)}$$
$$\sum_{l=1}^{k}{\alpha_l}=1$$
$$\theta = \{\alpha_1,...\alpha_k, \mu_1,...\mu_k, \Sigma_1,...\Sigma_k\}$$

由E-M算法我们有：

$$\theta^{(g+1)}=\mathop{\arg\max}_{\theta}\int_{z}{log(P(X,Z|\theta)) * P(Z|X, \theta^{(g)})}dz $$

又由混合高斯分布，我们有：

$$P(X,Z|\theta) = \prod_{i=1}^{n}P(x_i, z_i|\theta) = \prod_{i=1}^{n}P(x_i|z_i, \theta)\cdot P(z_i|\theta) = \prod_{i=1}^{n}\alpha_{z_i}\mathcal{N}(x_i|\mu_{z_i},\Sigma_{z_i}) $$

$$P(Z|X,\theta) = \prod_{i=1}^{n}P(z_i|x_i, \theta) = \prod_{i=1}^{n}{\frac{P(x_i|z_i, \theta)}{\sum_{l=1}^{k}P(x_i|z_l, \theta)}} = \prod_{i=1}^{n}{\frac{\alpha_{z_i}\mathcal{N}(x_i|\mu_{z_i},\Sigma_{z_i})}{\sum_{l=1}^{k}\alpha_{l}\mathcal{N}(x_i|\mu_{l},\Sigma_{l})}} $$

可以看到，虽然增加了隐变量Z， 但是$P(X,Z|\theta)$比$P(X|\theta)$显得更简单。

把上面两个式子代入EM迭代式子里，有:

$$\theta^{(g+1)} = \sum_{z_i=1}^{k}\sum_{i=1}^{n}logP(x_i, z_i|\theta)\cdot P(z_i|x_i,\theta^{(g)}) = \sum_{l=1}^{k}\sum_{i=1}^{n}log[\alpha_l\mathcal{N}(x_i|\mu_l, \Sigma_l)]\cdot P(l|x_i, \theta^{(g)})$$

代入高斯混合模型的前提，最后针对各个参数求导，令其为0. 最后有以下公式:

$$\alpha_l^{(g+1)} = \frac{1}{N}\sum_{i=1}^{N}P(l|x_i, \theta^{(g)})$$

$$\mu_l^{(g+1)} = \frac{\sum_{i=1}^{N}x_iP(l|x_i,\theta^{(g)})}{\sum_{i=1}^{N}P(l|x_i,\theta^{(g)})}$$

$$\Sigma_l^{(g+1)} = \frac {\sum_{i=1}^{N} [x_i - \mu_l^{(g+1)}] [x_i - \mu_l^{(g+1)}]^T P(l|x_i,\theta^{(g)})} {\sum_{i=1}^{N} P(l|x_i,\theta^{(g)})}$$

参考资料：

[优酷-徐亦达老师的GMM视频](http://v.youku.com/v_show/id_XMTM1MzMzMjk3Mg==.html?spm=a2hzp.8253869.0.0 "GMM")