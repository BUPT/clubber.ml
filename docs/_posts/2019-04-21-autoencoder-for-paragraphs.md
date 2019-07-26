---
title: A Hierarchical Neural Autoencoder for Paragraphs and Documents
date: 2019-04-21 12:00 +0800
author: YapheeetS
comments: true
mathjax: true
categories:
  - classic paper
tags:
  - attention
  - lstm
  - autoencoder
  - nlp

header:
  teaser: 
---

## 论文基本信息

1. 论文名：A Hierarchical Neural Autoencoder for Paragraphs and Documents

2. 论文链接：<https://arxiv.org/pdf/1506.01057.pdf>

3. 论文源码：
    - [https://github.com/jiweil/Hierarchical-Neural-Autoencoder](https://github.com/jiweil/Hierarchical-Neural-Autoencoder)

---

## A Hierarchical Neural Autoencoder for Paragraphs and Documents

### 模型结构

1. Standard Sequence to Sequence Model

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a70e2jrhj214a0h8ain.jpg)

2. Hierarchical Sequence to Sequence Model

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8chlzljj21be0qmqfx.jpg)

3. Hierarchical Sequence to Sequence Model with Attention

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8dutm3ej21de0qi7ia.jpg)

    - 计算过程

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8h5s9shj20ls02u74e.jpg)

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8ie1fhnj20bm03uaa5.jpg)

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8jbvu52j20es04wt8u.jpg)

    ![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8jwv90tj20lk0b4dgk.jpg)

### Evaluation

![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a8odnib4j20k005qt8y.jpg)
<!-- markdownlint-disable MD033 -->
- 把每个句子（输出和输入）都表示成一个特征向量，并按顺序标注index
- 通过计算sentence-to-sentence的F1 score，将输出的句子对应到输入的句子上,即输入的第i个句子对应的是输出的第i<sup>'</sup>个句子
- (j − i)可以理解为由j和i索引的两个输出句子之间的索引距离，(j<sup>'</sup> - i<sup>'</sup>)表示对应的输入句子之间的距离
- 如果没有输入句子与输出句子相对应，则会随机找一个输入句子与其匹配计算
- 不足之处：只考虑了语意（句子之间的相关性），几乎没有考虑语法

### 实验结果
  
![img](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g2a9id54spj21520aojtw.jpg)
