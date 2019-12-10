---
title: 第三季18场 AI ML Club 活动纪要
author: Leona08
date: 2019-12-08 19:00 +0800
comments: true
mathjax: true
categories:
  - events
tags:
  - 
header:
  teaser: /assets/2019/seminar-3-18/t-photo.jpg
---

<< 本次沙龙通知: [#441](https://github.com/BUPT/ai-ml.club/issues/441)  <<

## 第三季5场 AMC 沙龙活动纪要

- 日期：2019年12月08日周日下午7-10点
- 地点：北邮科研楼821
- 轮值主席：吴凤民 @[Leona08](https://github.com/Leona08)
- 轮值副主席：Duan-JM @[Duan-JM](https://github.com/Duan-JM)
- 会员：贺新 @[newip](https://github.com/newip)

本届沙龙内容（按发言顺序，由主席指定顺序)

## 沙龙内容

### Poster

- 段嘉铭 @[Duan-JM](https://github.com/Duan-JM)：[Brief roadmap to fewshot classification](https://docs.google.com/presentation/d/1-QjhxMxAG955i51BAihilcoLDtBhDDpZjgT4k4u05MQ/edit?usp=sharing)

  > 在看论文的过程中有三个点值得注意，一个是通过可视化的方式查看其backbone是否提出具有区分度的特征，一个是是否充分利用了所有信息（如，episode与episode之间的信息，大样本数据集中的信息等），以及使用的度量相似程度的公式是否恰当。
  
  ![段嘉铭]({{ '/assets/2019/seminar-3-18/seminar-3-18-talk-duan-jm.jpg'| relative_url }})

 - 行习铭 @[ximingxing](https://github.com/ximingxing)：Optimization-Based Meta-Learning （[MAML](https://arxiv.org/abs/1703.03400) [LEO](https://arxiv.org/abs/1807.05960)）

  > 介绍了 optimization-Based的Meta-Learning，MAML讲基于梯度更新参数的方法应用在小样本学习中，但是该方法存在few-shot在内部梯度回传存在高维参数的问题；另外一种是LEO，通过encoder和decoder的方法解决高维的问题，并且取得了很好的成绩。

  ![行习铭]({{ '/assets/2019/seminar-3-18/seminar-3-18-talk-ximingxing.jpeg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-3-18/seminar-3-18-meta-learning.pdf' | relative_url }}'
      width='560'
      height='315'
      allowfullscreen
      webkitallowfullscreen
      frameborder="0"
      style="
        position: absolute;
        top:0;
        left:0;
        width:100%;
        height:100%;
      "
    ></iframe>
  </di>
  
- 吴凤民 @[Leona08](https://github.com/Leona08): [Generalized Autoencoder: A Neural Network Framework for Dimensionality Reduction](https://www.semanticscholar.org/paper/Generalized-Autoencoder%3A-A-Neural-Network-Framework-Wang-Huang/2a4774a811ec32f005a043653dd15eb184d96dfa)

  > 分享了关于降维的文章，利用神经网络的autoencoder实现降维，相比于传统的方法，重新改写了construction error。并且基于loss function，提出framework，和多种流行的降维方法结合，实现降维效果的提升。

  ![吴凤民]({{ '/assets/2019/seminar-3-18/seminar-3-18-talk-leona08.jpeg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-3-18/seminar-3-18-gae.pdf' | relative_url }}'
      width='560'
      height='315'
      allowfullscreen
      webkitallowfullscreen
      frameborder="0"
      style="
        position: absolute;
        top:0;
        left:0;
        width:100%;
        height:100%;
      "
    ></iframe>
  </di>
## 授蛋仪式

![授蛋]({{ '/assets/2019/seminar-3-18/seminar-3-18-chairman-appointment.jpeg'| relative_url }})

> 从左起：段嘉铭，吴凤民，行习铭

## 集体合照

![合照]({{ '/assets/2019/seminar-3-18/seminar-3-18-group-photo.jpg' | relative_url }})

> 从左起：吴凤民，段嘉铭，行习铭，贺新

## 脑洞

1. newip: 
    1. 小样本学习在医疗领域是一个重要的方向，但是是否可以用多样本来替代是一个需要考虑的问题。
    2. 神经网络可视化和可解释有些牵强，是否应该将更多的时间花在建立评价体系上？

2. ximingxing: 衡量降维的方法，进行二维空间的投射是否足够客观，对齐baseline，以及baseline如何确定是值得探讨的。

3. Duan-JM: 对准baseline这个工作很有意义！

## 吐槽

1. newip: 最近活动的参与人数较少，应该采取一些措施激发大家的参与热情，比如去实验室邀请一些已发表论文的人来分享，或者开学季去BBS上进行宣传。

## RSVP

注：“回复”操作，指的是回复本ISSUE留言

1. 如果对活动纪要有修订意见，请回复对本次沙龙纪补充
2. 如果参加下次沙龙活动，请回复下次自己的分享是 Oral（30分钟）还是Poster（5分钟）
3. 如果计划邀请新朋友参加下次沙龙活动，请让新朋友回复一句话的自我介绍

## 特别鸣谢CAD中心提供活动场地，以及宋美娜老师和实验室全体人员对本沙龙的支持与帮助~
