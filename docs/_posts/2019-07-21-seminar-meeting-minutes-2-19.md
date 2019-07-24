---
title: 第二季19场 AI ML Club 活动纪要
author: VDeamoV
date: 2019-07-21 19:00 +0800
comments: true
mathjax: true
categories: 
  - events
tags:
  - 
header:
  teaser: /assets/2019/seminar-2-19/after-party-19.jpg
---

<< 本次沙龙通知: [#195](https://github.com/BUPT/ai-ml.club/issues/195)  <<

## 第二季19场 AMC 沙龙活动纪要

- 日期：2019年7月21日周日晚上7-10点
- 地点：北邮科研楼821
- 轮值主席： 段嘉铭 @VDeamoV
- 轮值副主席：林博 @linbo0518
- 会员： 李卓桓、贺新、林博、侯正罡、高久怡、董青、段嘉铭、李京伦、尹鹏宇
- 新人：臧群、李朋涛、李财

本届沙龙内容（按发言顺序，由主席指定顺序）

## 沙龙内容

### Poster

- 董青 @secortot
    > 分享了[Guided Anchor](https://arxiv.org/abs/1901.03278), 分享了一种 anchor free 的目标检测方法

![董青]({{ '/assets/2019/seminar-2-19/dq-poster.jpg'| relative_url }})

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-2-19/dq-slide.pdf' | relative_url }}'
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
</div>

- 段嘉铭 @VDeamoV
    > 分享了[Finding Task-Relevant Features for Few-Shot Learning by Category Traversal](https://arxiv.org/pdf/1905.11116.pdf), 一种通过先纵览当前 Task 之后生成 Mask 来过滤无关特征的方法来达到更好的模型学习效果

![段嘉铭]({{ '/assets/2019/seminar-2-19/djm-poster.jpg'| relative_url }})

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-2-19/djm-slide.pdf' | relative_url }}'
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
</div>

- 高久怡 @gaojiuy
    > [Learning Deep Features for Discriminative Localization](https://arxiv.org/pdf/1512.04150.pdf)，介绍了一篇2015年的一篇经典可视化论文，改论文的主要贡献为使用热力图来对模型进行解释。（注：该论文还在其他细节进行了分析，有兴趣的同学可以详细了解）

![高久怡]({{ '/assets/2019/seminar-2-19/gjy-poster.jpg' | relative_url }})

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-2-19/gjy-slide.pdf' | relative_url }}'
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
</div>

- 尹鹏宇 @WdBlink
    > [High-Resolution Representations for Labeling Pixels and Regions](https://arxiv.org/abs/1904.04514)，介绍了一篇来自 MSRA 的论文，采用多层并行的结构保留高分辨率信息，并在各大 CV 任务获得了不错的成绩

![尹鹏宇]({{ '/assets/2019/seminar-2-19/ypy-poster.jpg' | relative_url }})

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-2-19/ypy-slide.pdf' | relative_url }}'
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
</div>

- 侯正罡 @ArronHZG
    > [Attention in computer version](https://blog.csdn.net/Arron_hou/article/details/95676716)，介绍了 CV 领域常见的 Attention 结构

![侯正罡]({{ '/assets/2019/seminar-2-19/hzg-poster.jpg' | relative_url }})

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-2-19/hzg-slide.pdf' | relative_url }}'
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
</div>

## 授蛋仪式

![授蛋]({{ '/assets/2019/seminar-2-19/egg.jpg' | relative_url }})

## 集体合照

![合照]({{ '/assets/2019/seminar-2-19/selfie.jpg' | relative_url }})

## 俱乐部讨论内容

1. 大家在讲论文的时候最好先简单说明下输入输出，会让听众更容易听懂
2. 算法的公式，在 PPT 中需要更清晰的设计摆放位置，让听众能一眼知道这个公式用在模型什么地方
3. Poster 应该更加侧重讲论文的创新点，而不是通篇过论文
4. 之后增加博客作者介绍 profile，profile 中会加上一些该讲者遇到的常见问题
5. 下一任副主席为高久怡

## After Party

AfterParty 第十九次活动顺利结束！

![AfterParty]({{ '/assets/2019/seminar-2-19/after-party-19.jpg' | relative_url }})

## RSVP

注：“回复”操作，指的是回复本ISSUE留言

1. 如果对活动纪要有修订意见，请回复对本次沙龙纪补充
2. 如果参加下次沙龙活动，请回复下次自己的分享是 Oral（30分钟）还是Poster（5分钟）
3. 如果计划邀请新朋友参加下次沙龙活动，请让新朋友回复一句话的自我介绍

## 特别鸣谢CAD中心提供活动场地，以及宋美娜老师和实验室全体人员对本沙龙的支持与帮助~
