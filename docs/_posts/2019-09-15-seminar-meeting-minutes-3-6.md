---
title: 第三季6场 AI ML Club 活动纪要
author: ArronHZG
date: 2019-09-15 15:00 +0800
comments: true
mathjax: true
categories: 
  - events
tags:
  - 
header:
  teaser: /assets/2019/seminar-3-6/afterparty.jpg
---

<< 本次沙龙通知: [#325](https://github.com/BUPT/ai-ml.club/issues/254)  <<

## 第三季1场 AMC 沙龙活动纪要

- 日期：2019年8月11日周日下午7-10点
- 地点：北邮科研楼821
- 轮值主席：侯正罡 @[CyFeng16](https://github.com/CyFeng16)
- 轮值副主席：段嘉明 @[cgpeter96](https://github.com/cgpeter96)
- 会员：李卓桓、刘云、贺新、范弘炜、石珅达、张璐
- 新人：王琳玉

本届沙龙内容（按发言顺序，由主席指定顺序）

## 沙龙内容

### Oral

- 范弘炜 @[hwfan](https://github.com/hwfan)

   >度量学习：监督与非监督
   >监督学习 ArcFace 比 TripletLoss 的优势在于模长的归一化
   >实验结果表明这样做对精度是有提升的，一个分析是可以避免由于模长过大带来的 target logit 值的不均匀分布,结束了 LFW 比赛
   >MegaFace 得分很高，也几乎终结了比赛
    
   >非监督学习 ECN
   >现有的数据集在量级上非常 Naïve，因此需要通过相对多的有标记数据辅助少的无标记数据
   >学习无监督的典型方法类似于聚类
   >Exemplar Neighbor→聚类
   >Cam→跨摄像头
   >际上是两个学习途径同时进行
   >实验结果达到了无监督 ReID 的 SOTA

  [ArcFace: Additive Angular Margin Loss for Deep Face Recognition](https://arxiv.org/abs/1801.07698)  and [Invariance Matters: Exemplar Memory for Domain Adaptive Person Re-identification](https://arxiv.org/abs/1904.01990)
  GitHub: https://github.com/deepinsight/insightface; https://github.com/zhunzhong07/ECN

    ![范弘炜]({{ '/assets/2019/seminar-3-6/seminar-3-6-fanhongwei.jpg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/' | relative_url }}#{{ '/assets/2019/seminar-3-6/deep-metric-learning-report.pdf' | relative_url }}'
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
  
- 侯正罡 @[ArronHZG](https://github.com/ArronHZG)

  >语义分割中的 Attention 机制
  >一作李夏，北大林宙辰组，本科北邮
  >Attention 机制的分析：实际上是自相关，通过自相关对信息进行加权，关心自相关程度更大的信息。外壳结构类似于 Bottleneck。
  >参数学习：EM 算法，提取特征的部分已经 pretrained 过，本质上是一个 Post-processing 的过程。
  >通过实验表明了学习得到的基向量具有代表性，数量少，且互不相似，对语义分割的去噪有明显的帮助。
  >传统方法与 DL 结合的一个案例。
  
  [Expectation Maximization Attention Networks for Semantic Segmentation](https://arxiv.org/abs/1907.13426)
  [Github](https://xialipku.github.io/EMANet)
    
  ![侯正罡]({{ '/assets/2019/seminar-3-6/seminar-3-6-arron.jpg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/' | relative_url }}#{{ '/assets/2019/seminar-3-6/1907-13426--emanet.pdf' | relative_url }}'
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

### Poster


- 刘云 @[fuyunfuyun666](https://github.com/fuyunfuyun666)
  
  >多模态问题的通用结构
  >2 3 5 层解决不同问题，每层是一个类 Res-Block 结构，表示从低级语义到高级语义。
  >通过实验探究了联合学习时几层 Res-Block 对问题最有帮助。
  >但实验性过强，并没有解释结果在不同问题的语义高低方面的启示（数据处理原理，越到高层互信息越少），略显遗憾。

  [Multi-task Learning of Hierarchical Vision-Language Representation](https://arxiv.org/pdf/1812.00500.pdf)
      
  ![刘云]({{ '/assets/2019/seminar-3-6/seminar-3-6-liuyun.jpg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-3-6/1812-00500-multi-task.pdf' | relative_url }}'
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
    
- 李卓桓 @[huan](https://github.com/huan)
  
  >TPU 的应用案例: [使用 TPU 训练 TensorFlow 模型（Huan）](https://www.zixia.net/tensorflow-handbook-tpu/)，帮助快速进行大规模训练
  >可能可以申请到2500刀的资源。
       
  ![李卓桓]({{ '/assets/2019/seminar-3-6/seminar-3-6-huan.jpg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-3-6/tensorflow-handbook-tpu.pdf' | relative_url }}'
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

- 张璐 @[23LuZ ](https://github.com/23LuZ)
  >语言中的注意力机制
  >Encoder-Decoder 结构
  >Local/Global/Global-Local 三种分类
      
  [Neural Responding Machine for Short-Text Conversation](https://www.aclweb.org/anthology/P15-1152)
      
  ![张璐]({{ '/assets/2019/seminar-3-6/seminar-3-6-23luz.jpg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-3-6/neural-responding-machine-for-short-text-conversation.pdf' | relative_url }}'
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

CV 授蛋仪式
![授蛋]({{ '/assets/2019/seminar-3-6/seminar-3-6-cv-chairman-appointment.jpg'| relative_url }})

NLP 授蛋仪式
![授蛋]({{ '/assets/2019/seminar-3-6/seminar-3-6-nlp-chairman-appointment.jpg'| relative_url }})

## 集体合照

![合照]({{ '/assets/2019/seminar-3-6/seminar-3-6-group-photo.jpg' | relative_url }})

## 俱乐部讨论内容

1. 惯性的时间控制需要每一届主席持续把控
2. 如果预期讨论过多的poster可以当成oral申报，poster主要还是集中在论文的某一个点讲清楚。
3. Zoom链接和视频录制正式上线，[入口地址:https://ai-ml.club/zoom/](https://ai-ml.club/zoom/)。
4. 下一任主席为陈光，下一任副主席为段清华。

## After Party

![AfterParty]({{ '/assets/2019/seminar-3-6/seminar-3-6-after-party.jpg' | relative_url }})

![AfterParty]({{ '/assets/2019/seminar-3-6/seminar-3-6-nlp-chairmen.jpg' | relative_url }})

## Notice!!!

根据AI-ML Club S3E6讨论的决定，从S3E7开始将实行CV/NLP分会计划，即隔周举办CV和NLP的分会议。具体实施是逢单周（本周即单周）进行CV会议，逢双周（下周即双周）进行NLP会议，因此下周的S3E7举行的将是NLP分会议，而下下周的S3E8举行的将是CV分会议。目前已完成主席选举，对相关领域感兴趣的会员和新人可以按时参加。

特此通知

## RSVP

注：“回复”操作，指的是回复本ISSUE留言

1. 如果对活动纪要有修订意见，请回复对本次沙龙纪补充
2. 如果参加下次沙龙活动，请回复下次自己的分享是 Oral（30分钟）还是Poster（5分钟）
3. 如果计划邀请新朋友参加下次沙龙活动，请让新朋友回复一句话的自我介绍

## 特别鸣谢CAD中心提供活动场地，以及宋美娜老师和实验室全体人员对本沙龙的支持与帮助~
