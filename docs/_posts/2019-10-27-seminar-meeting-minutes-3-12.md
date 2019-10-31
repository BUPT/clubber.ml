---
title: 第三季12场 AI ML Club 活动纪要
author: hwfan
date: 2019-10-27 19:00 +0800
comments: true
mathjax: true
categories: 
  - events
tags:
  - 
header:
  teaser: /assets/2019/seminar-3-12/seminar-3-12-after-party.jpg
---

<< 本次沙龙通知: [#396](https://github.com/BUPT/ai-ml.club/issues/396)  <<

## 第三季12场 AMC 沙龙活动纪要

- 日期：2019年10月27日 19:00-22:00
- 地点：北邮科研楼821
- 轮值主席：范弘炜 @[hwfan](https://github.com/hwfan)
- 轮值副主席：高久怡 @[gaojiuy](https://github.com/gaojiuy)
- 会员：吴凤民、张博涵、石珅达、段嘉铭、侯正罡
- 新人：苏子宸、范佳玮、康晓阳
- 本次活动全程直播于哔哩哔哩弹幕网，内容配图为现场直播画面

本届沙龙内容（按发言顺序，由主席指定顺序）

## 沙龙内容

### Oral

- 范弘炜 @[hwfan](https://github.com/hwfan)

  >介绍了研究生高效阅读论文的一些策略，这些策略由滑铁卢大学的学者S. Keshav总结，并发布于ArXiv。Keshav认为，研究生阅读论文应该遵从一种“三段论”，由浅及深地阅读。在第一个阶段，应该通过标题、摘要、封面图、小标题等线索判断文章自身的贡献与质量，对论文的基本情况有大概的认识。在第二个阶段，决定了深入研读之后，应该向论文中的“硬骨头”，如实验结果、算法细节等下手，并试图找出其中自己不理解的部分并记录。在最后一个阶段，应该尝试对论文进行思想实验，发现其中可能存在问题和创新点的部分，以辅助自己的研究，必要的时候可以自行复现。除了阅读文献的技巧外，作者还提供了一些对做文献综述有所帮助的提示，最主要是要找到一个可靠的研究综述，如果无法找到，则应该发现所研究领域论文的共同引用，将之作为经典文献，从而由内而外地找到领域的边界。

  [How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)

  （因故未能留下含本人的照片，以会议之后作同一讲解的含本人照片代替）
    ![范弘炜]({{ '/assets/2019/seminar-3-12/seminar-3-12-fanhongwei.jpg'| relative_url }})

### Poster

- 张博涵 @[ltg001](https://github.com/ltg001)

  >介绍了对源代码的生成模型的一种改进方案，该方案被发表在ICLR2019上。源代码生成是一个有趣的结构化预测问题，需要推理硬语法和语义约束以及自然的，可能的程序。研究者针对此问题提出了一种新颖的模型，使用图表示生成输出的中间状态，并结合注意力机制进行推理，提升了现有方法在该问题上的性能表现。
  
  [Generative Code Modeling With Graphs](https://arxiv.org/pdf/1805.08490.pdf)
  ([Github](https://github.com/Microsoft/graph-based-code-modelling))

  ![张博涵]({{ '/assets/2019/seminar-3-12/seminar-3-12-ltg001.jpg'| relative_url }})

  <div class="zoom-container" style="
      position: relative;
      padding-bottom:56.25%;
      padding-top:30px;
      height:0;
      overflow:hidden;
  ">
    <iframe
      src='{{ '/assets/js/viewer-js/' | relative_url }}#{{ '/assets/2019/seminar-3-12/ltg001.pdf' | relative_url }}'
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

- 吴凤民 @[Leona08](https://github.com/Leona08)
  
  >介绍了个人条件期望（ICE）图方法，用于可视化监督学习算法估算的模型。ICE图突出显示了协变量范围内拟合值的变化，表明了异质性可能存在的位置和程度，并使用了一种类似于剪枝的模式，减小对隐变量的搜索空间，因此提升了性能。

  [A peek into the black box: exploring classifiers by randomization](https://arxiv.org/pdf/1309.6392.pdf)

  ![吴凤民]({{ '/assets/2019/seminar-3-12/seminar-3-12-leona.jpg'| relative_url }})

- 石珅达 @[CyFeng16](https://github.com/CyFeng16)

  >介绍了一个被称为“神经网络速写”的新兴领域及其重要论文。简而言之，“速写”是将神经网络各个组分贡献出的“知识”进行有效集中并归纳总结的过程。使用“速写”的方法，我们可以通过类似于压缩感知的模式，找到不同知识之间的知识图谱，从而将神经网络的训练转化为知识图谱提取的过程。

  [Recursive Sketches for Modular Deep Learning](https://arxiv.org/abs/1905.12730)

  ![石珅达]({{ '/assets/2019/seminar-3-12/seminar-3-12-cyfeng.jpg'| relative_url }})

## 授蛋仪式

授蛋仪式
![授蛋]({{ '/assets/2019/seminar-3-12/seminar-3-12-chairman-appointment.jpg'| relative_url }})

## 集体合照

![合照]({{ '/assets/2019/seminar-3-12/seminar-3-12-group-photo.jpg' | relative_url }})

## 俱乐部讨论内容

1. 时长问题：时长控制的责任应该到人。如果在规定时间内，讲者由于回答提问或节奏掌控失常而无法正常结束，责任应该由讲者本人承担，讲者可以
选择在下次活动中优先讲解，或完全地结束本次讲解。
2. 客座讲者：对于CV分会的NLP讲者时间如何把握仍然是一个问题。讲者如果没有给予足够的时间，是很难在其他领域的会议上讲解好本领域的内容的。但这种增强泛化能力的设定仍然是需要保留的，因此剩下的就是时间这些细节上的问题。

## After Party

![AfterParty]({{ '/assets/2019/seminar-3-12/seminar-3-12-after-party.jpg' | relative_url }})

## RSVP

注：“回复”操作，指的是回复本ISSUE留言

1. 如果对活动纪要有修订意见，请回复对本次沙龙纪补充
2. 如果参加下次沙龙活动，请回复下次自己的分享是 Oral（30分钟）还是Poster（5分钟）
3. 如果计划邀请新朋友参加下次沙龙活动，请让新朋友回复一句话的自我介绍

## 特别鸣谢CAD中心提供活动场地，以及宋美娜老师和实验室全体人员对本沙龙的支持与帮助~
