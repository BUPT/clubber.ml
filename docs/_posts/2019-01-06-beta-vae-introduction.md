---
title: Beta Variational AutoEncoder Introduction
author: huan
date: 2019-01-06 12:00 +0800
comments: true
mathjax: true
categories: 
  - generative model
tags:
  - vae
header:
  teaser: /assets/2019/vae-architecture.png
---

Poster for [2019-01-06 CAIC(Conversaional AI Club)第二十一次CAIC沙龙活动通知](https://github.com/BUPT/ai-ml.club/issues/51)

![Beta-VAE]({{ '/assets/2019/2019-01-06-beta-vae-introduction-celeba_h_beta10_z32_traverse.jpg' | relative_url }})
> [Pytorch implementation of β-VAE](https://github.com/1Konny/Beta-VAE)

> Beta-VAE
> If each variable in the inferred latent representation z is only sensitive to one single generative factor and relatively invariant to other factors, we will say this representation is disentangled or factorized. One benefit that often comes with disentangled representation is good interpretability and easy generalization to a variety of tasks.
> 
> For example, a model trained on photos of human faces might capture the gentle, skin color, hair color, hair length, emotion, whether wearing a pair of glasses and many other relatively independent factors in separate dimensions. Such a disentangled representation is very beneficial to facial image generation.
> 
> β-VAE ([Higgins et al., 2017](https://openreview.net/forum?id=Sy2fzU9gl)) is a modification of Variational Autoencoder with a special emphasis to discover disentangled latent factors. Following the same incentive in VAE, we want to maximize the probability of generating real data, while keeping the distance between the real and estimated posterior distributions small.
> 
> Source: [From Autoencoder to Beta-VAE](https://lilianweng.github.io/lil-log/2018/08/12/from-autoencoder-to-beta-vae.html)

## SEE ALSO

### Codes

- [Replicating "Understanding disentangling in β-VAE"](https://github.com/miyosuda/disentangled_vae)
- [Pytorch implementation of β-VAE](https://github.com/1Konny/Beta-VAE)

### Blogs

- [From Autoencoder to Beta-VAE](https://lilianweng.github.io/lil-log/2018/08/12/from-autoencoder-to-beta-vae.html)
- [Summary: Beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework](https://medium.com/uci-nlp/summary-beta-vae-learning-basic-visual-concepts-with-a-constrained-variational-framework-91ad843b49e8)
- [Variational Autoencoder (VAE)](https://snowkylin.github.io/autoencoder/2016/12/05/introduction-to-variational-autoencoder.html)
