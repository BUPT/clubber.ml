---
title: 变分自编码器及其应用
comments: true
mathjax: true
categories:
  - VAE
tags:
  - note
  - code
---

## 引言
笔记主要参考变分自编码器的原论文[《Auto-Encoding Variational Bayes》](https://arxiv.org/pdf/1312.6114.pdf)，与[苏神的博客](https://kexue.fm/archives/5253)

## VAE模型
VAE的目标（与GAN相同）：希望构建一个从隐变量$Z$生成目标数据$X$的模型。
VAE的核心是：**进行分布之间的变换。**

![](http://ww1.sinaimg.cn/large/ca26ff18gy1fvzqckwnkhj20my0aegn1.jpg)

VAE的Encoder有两个，一个用来计算均值，一个用来计算方差。

### 问题所在
但生成模型的难题是判断生成分布与真实分布的相似度。（即我们只知道抽样结果，不知道分布表达式）
![](http://ww1.sinaimg.cn/large/ca26ff18gy1fvuzgu3recj20or0c7400.jpg)

### 大部分教程所述的VAE
![](http://ww1.sinaimg.cn/large/ca26ff18gy1fvxa4kzerpj20qt0dy40q.jpg)
模型思路是：先从标准正态分布中采样一个Z，然后根据Z来算一个X。
若VAE结构确实是这个图的话，我们其实完全不清楚：究竟经过重新采样出来的$Z_k$，是不是还对应着原来的$X_k$。

其实，在整个VAE模型中，我们并没有去使用$p(Z)$（隐变量空间的分布）是正态分布的假设，我们用的是假设$p(Z|X)$（后验分布）是正态分布!

但是，训练好的神经网络
并且VAE会让所有的$P(Z|X)$都向标准正态分布看齐：
$$p(Z)=\sum_X p(Z|X)p(X)=\sum_X \mathcal{N}(0,I)p(X)=\mathcal{N}(0,I) \sum_X p(X) = \mathcal{N}(0,I)$$

### 真实的VAE
![](http://ww1.sinaimg.cn/large/ca26ff18gy1fvuzt27ie8j20rf0imjv6.jpg)
VAE是为每个样本构造**专属**的正态分布，然后采样来重构。

但是神经网络经过训练之后的方差会接近0。采样只会得到确定的结果。

因此还需要使所有的正态分布都向**标准正态分布**（模型的假设）看齐。为了使所有的P(Z|X)都向$\mathcal{N}(0,I)$看齐，我们需要：

#### 编码器：使用神经网络方法拟合参数
构建两个神经网络：$\mu_k=f_1(X_k), log_{\sigma^2}=f_2(X_k)$来拟合均值和方差。当二者尽量接近零的时候，分布也就达到了$\mathcal{N}(0,I)$。
```python
z_mean = Dense(latent_dim)(h)
z_log_var = Dense(latent_dim)(h)
```

针对两个损失的比例选取，使用KL散度$KL(N(\mu,\sigma^2)||N(0,I))$作为额外的loss。上式的计算结果为：

$$\mathcal{L}_{\mu,\sigma^2}=\frac{1}{2} \sum_{i=1}^d \Big(\mu_{(i)}^2 + \sigma_{(i)}^2 - \log \sigma_{(i)}^2 - 1\Big)$$

```python
kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
```

#### 解码器：保证生成能力
我们最终的目标则是最小化误差$\mathcal{D}(\hat{X_k},X_k)^2$。

解码器重构$X$的过程是希望没噪声的，而$KL loss$则希望有高斯噪声的，两者是对立的。所以，VAE跟GAN一样，内部其实是包含了一个对抗的过程，只不过它们两者是混合起来，共同进化的。





#### reparameterization trick（重参数技巧）
在反向传播优化均值和方差的过程中，“采样”操作是**不可导**的，但是采样的结果是可导的。

因此可以利用标准正太分布采样出的$\epsilon$直接估算$Z=\mu+\epsilon\times\sigma$。
```python
def sampling(args):
    """Reparameterization trick by sampling fr an isotropic unit Gaussian.

    # Arguments:
        args (tensor): mean and log of variance of Q(z|X)

    # Returns:
        z (tensor): sampled latent vector
    """

    z_mean, z_log_var = args
    batch = K.shape(z_mean)[0]
    dim = K.int_shape(z_mean)[1]
    # by default, random_normal has mean=0 and std=1.0
    epsilon = K.random_normal(shape=(batch, dim))
    return z_mean + K.exp(0.5 * z_log_var) * epsilon
```

于是“采样”操作不再参与梯度下降，改为采样的结果参与，使得整个模型可以训练。

## DEMO:基于CNN和VAE的作诗机器人
### 模型结构
![](http://ww1.sinaimg.cn/large/ca26ff18gy1fvuzt1xl9cj20rf0imjv6.jpg)
先将每个字embedding为向量，然后用层叠CNN来做编码，接着池化得到一个encoder的结果，根据这个结果生成计算均值和方差，然后生成正态分布并重新采样。在解码截断，由于现在只有一个encoder的输出结果，而最后要输出多个字，所以先接了多个不同的全连接层，得到多样的输出，然后再接着全连接层。

#### GCNN(Gated Convolutional Networks)
这里的CNN不是普通的CNN+ReLU，而是facebook提出的GCNN，其实就是做两个不同的、外形一样的CNN，一个不加激活函数，一个用sigmoid激活，然后把结果乘起来。这样一来sigmoid那部分就相当于起到了一个“门（gate）”的作用。
 

## 参考与引用
- https://kexue.fm/archives/5253
- https://arxiv.org/pdf/1312.6114.pdf
- https://kexue.fm/archives/5332
- https://jaan.io/what-is-variational-autoencoder-vae-tutorial/