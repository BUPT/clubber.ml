---
layout: post
title:  paperweekly笔记模板
categories: 
  - Paper
tags: 
  - note
excerpt: 
---

<!-- 论文基本信息：方便查阅和追踪 -->
<!-- 论文基本信息的获取：
1. 直接从论文pdf中获取
2. 从paperweekly首页上方搜索论文；若未检索到，点击推荐论文输入论文名即可自动获取信息
-->

## 论文基本信息
1. 论文名：paper_title
<!-- Ex: 论文名：Zero-shot Recognition via Semantic Embeddings and Knowledge Graphs. -->

2. 论文链接：paper_link
<!-- Ex: https://arxiv.org/abs/1606.01541  -->

3. 论文源码：
    - code_link1
    - code_link2
<!--
    Ex:
    - https://github.com/liuyuemaicha/Deep-Reinforcement-Learning-for-Dialogue-Generation-in-tensorflow
    - https://github.com/agsarthak/Goal-oriented-Dialogue-Systems
-->
    
4. 关于作者：
<!-- 建议从google schoolar获取详细信息 -->
    - first_author: position, times_cited
    - second_author: position, times_cited

5. 关于笔记作者：
    - your_name,your_schoole,your_research_direction
<!-- 
    Ex:
    - 朱正源,北京邮电大学研究生，研究方向为多模态与认知计算。  
-->
    

## 论文推荐理由
<!-- Ex: 论文摘要的中文翻译
最近对话生成的神经模型为会话代理生成响应提供了很大的希望，但往往是短视的，一次预测一个话语而忽略它们对未来结果的影响。对未来的对话方向进行建模对于产生连贯，有趣的对话至关重要，这种对话需要传统的NLP对话模式借鉴强化学习。在本文中，我们将展示如何整合这些目标，应用深度强化学习来模拟聊天机器人对话中的未来奖励。该模型模拟两个虚拟代理之间的对话，使用策略梯度方法来奖励显示三个有用会话属性的序列：信息性，连贯性和易于回答（与前瞻性功能相关）。我们在多样性，长度以及人类评判方面评估我们的模型，表明所提出的算法产生了更多的交互式响应，并设法在对话模拟中促进更持久的对话。这项工作标志着基于对话的长期成功学习神经对话模型的第一步。
-->



## 论文中文名（paper's title）
<!-- Ex: ## 强化学习在对话生成领域的应用 -->


### 引言
#### 预备知识
<!-- 针对论文中不常用的术语进行简短的解释，方便读者理解 -->
- First term: your_annotation
- Second term: your_annotation


#### 论文写作动机
<!-- 当前研究领域存在的问题
Ex:
标准的Seq-to-Seq模型用于对话系统时常常使用MLE作为模型的评价标准，但这往往导致下面两个主要缺点：
系统倾向于产生一些普适性的回应，也就是dull response，这些响应可以回答很多问题但却并不是我们想要的，我们想要的是有趣、多样性、丰富的回应；
系统的回复不具有前瞻性，有时会导致陷入死循环，导致对话轮次较少。也就是产生的响应没有考虑对方是否容易回答的情况。
-->


#### 论文思路亮点
<!-- 论文解决问题的主要思路：
Ex:
首先使用Seq-to-Seq模型预训练一个基础模型，然后根据作者提出的三种Reward来计算每次生成的对话的好坏，并使用policy network的方法提升对话响应的多样性、连贯性和对话轮次。
-->



### 解决问题的方法
#### 子标题






### 实验结果分析
#### 评估指标
<!-- Ex:
1. 对话的长度，作者认为当对话出现dull response的时候就算做对话结束，所以使用对话的轮次来作为了评价指标：
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fuf0a67z3dj20fi051q3c.jpg)

2. 不同unigrams、bigrams元组的数量和多样性，用于评测模型产生回答的丰富程度：
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fuf0boign2j20e104a3z0.jpg)
-->


#### 实验结果评价



### 总结
<!-- 可根据论文的结论部分撰写 -->

### 引用与参考
<!--
Ex:
1. https://www.paperweekly.site/papers/notes/221
2. https://scholar.google.com/
-->
