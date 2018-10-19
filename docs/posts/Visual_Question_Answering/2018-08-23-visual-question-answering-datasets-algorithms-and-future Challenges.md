---
title: Visual-Question-Learning(VQA)学习笔记
comments: true
mathjax: true
categories:
  - VQA
tags:
  - summarize

---

<!-- 论文基本信息：方便查阅和追踪 -->
<!-- 论文基本信息的获取：
1. 直接从论文pdf中获取
2. 从paperweekly首页上方搜索论文；若未检索到，点击推荐论文输入论文名即可自动获取信息-->
## 论文基本信息
1. 论文名：Visual Question Answering: Datasets, Algorithms, and Future Challenges

2. 论文链接：https://arxiv.org/pdf/1610.01465.pdf
<!-- Ex: https://arxiv.org/abs/1606.01541  -->

3. 论文源码
  - None
    
4. 关于作者
    - Kushal Kafle
    - Christopher Kanan

5. 关于笔记作者：
    - 朱正源,北京邮电大学研究生，研究方向为多模态与认知计算。  
    


## 论文推荐理由
<!-- Ex: 论文摘要的中文翻译
最近对话生成的神经模型为会话代理生成响应提供了很大的希望，但往往是短视的，一次预测一个话语而忽略它们对未来结果的影响。对未来的对话方向进行建模对于产生连贯，有趣的对话至关重要，这种对话需要传统的NLP对话模式借鉴强化学习。在本文中，我们将展示如何整合这些目标，应用深度强化学习来模拟聊天机器人对话中的未来奖励。该模型模拟两个虚拟代理之间的对话，使用策略梯度方法来奖励显示三个有用会话属性的序列：信息性，连贯性和易于回答（与前瞻性功能相关）。我们在多样性，长度以及人类评判方面评估我们的模型，表明所提出的算法产生了更多的交互式响应，并设法在对话模拟中促进更持久的对话。这项工作标志着基于对话的长期成功学习神经对话模型的第一步。
 -->
 视觉问答(Visual Question answering, VQA)是近年来计算机视觉和自然语言处理领域的一个热点问题。在VQA中，一个算法需要回答关于图像的基于文本的问题。自2014年发布第一个VQA数据集以来，已经发布了更多的数据集，并提出了许多算法。在这篇综述中，我们从问题的形成、现有数据集、评估指标和算法的角度，批判性地研究了VQA的当前状态。特别地，我们讨论了当前数据集在正确训练和评估VQA算法方面的局限性。然后，我们详尽地回顾了VQA的现有算法。最后，我们讨论了未来VQA和图像理解研究的可能方向。


## 视觉问答：数据集，算法和未来的挑战
<!-- Ex: ## 强化学习在对话生成领域的应用 -->


### 引言

#### VQA的研究价值
1. 大部分计算机视觉任务不能完整的理解图像
图像分类、物体检测、动作识别等任务很难获取到物体的**空间位置信息**并且根据它们的属性和关系进行**推理**。

2. 人类对**Grand Unified Theory**的痴迷追求
  - 目标识别任务：图像里面有什么？[分类]
  - 目标检测任务：图像里面有猫吗？[拉框]
  - 属性分类任务：图像里面的猫是什么颜色的？
  - 场景分类：图像是在室内吗？
  - 计数任务：图像里面有多少猫？
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvah1uwsvij208c04ogn4.jpg)

3. 通过视觉图灵测试：
  - 基准问题测试
  - 建立评价指标 


### VQA的数据集
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvajh4e1wbj20tz09eacb.jpg)


### VQA的评价标准
- Open-ended(OE): 开放式的
- Multiple Choice(MC): 选择式的

![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvb6r1njlkj20kp0dmjuj.jpg)


#### 流行的评价标准
选择式任务的评价标准直接使用正确率即可。但是开放式任务的评价标准呢？

1. Simple accuracy:
  1. Q: What animals are in the photo
    若`dogs`是正确答案，那么`dog`和`zebra`的惩罚竟然是一样的
  2. Q: What is in the tree
    若`bald eagle`是正确答案，`eagle`或是`bird`  与  `yes`的惩罚竟然也是一样的
2. Wu-Palmer Similarity
  1. 语义相似度
    `Black`、`White`两个单词的`WUPS score`是0.91。所以这可能会给错误答案一个相当高的分数。
  2. 只可以评价单词，句子不可使用

3. $Accuracy_{VQA}=min(\frac{n}{3}, 1)$
  同样是语义相似度，大致正确就ok: 人为构造一个答案集合，$n$是算法和人类拥有的相同的答案数量。



### VQA的算法
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvbaa7e7d4j20qr098n45.jpg)
存在的算法大致结构均包括：
  1. 提取图像特征
  2. 提取问题特征
  3. 利用特征产生结果的算法

#### Baseline和模型性能
1. 瞎猜最有可能的答案。“yes”/"no"
2. MLP(multi-layer percepton)

![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvbapjz9zkj20ky0lradq.jpg)

#### 模型架构一览
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvbasmehclj20qg0l278r.jpg)

1. 基于贝叶斯和问题导向的模型
2. 基于注意力机制的模型
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvbb0ttq7cj20r60dj7bs.jpg)
3. 非线性池化方法

- MULTI-WORLD: A multi-world approach to question answering about real- world scenes based on uncertain input, NIPS2014
- ASK-NEURon: Ask your neurons: A neural-based ap- proach to answering questions about images, ICCV2015
- ENSEMSBLE: Exploring models and data for image question answering, NIPS2015
- LSTM Q+I: VQA: Visual question answering, ICCV2015
- iBOWIMG: Simple baseline for visual question answering, arxiv
- DPPNET: Image question answering using convolutional neural network with dynamic parameter prediction, CVPR2016
- SMem: Ask, attend and answer: Exploring question-guided spatial attention for visual question answering, ECCV2016
- SAN: Stacked attention networks for image question answering, CVPR2016
- NMN: Deep compositional question answering with neural module networks, CVPR2016
- FDA: A focused dynamic attention model for visual question answering, arxiv2016
- HYBRID: Answer-type prediction for visual question answering, CVPR2016
- DMN+: Dynamic memory networks for visual and textual question answering, ICML2016
- MRN: Multimodal residual learning for visual qa, NIPS2016
- HieCoAtten: Hierarchical question-image co-attention for visual question answering, NIPS2016
- RAU_ResNet: Training recurrent answering units with joint loss minimization for VQA, arxiv2016
- DAN: Dual attention networks for multimodal reasoning and matching, arxiv2016
- MCB+Att: Multi-modal compact bilinear pooling for visual question answering and visual grounding, EMNLP2016
- MLB: Hadamard product for low-rank bilinear pooling, arxiv2016
- AMA: Ask me anything: Free-form visual question answering based on knowledge from external sources, CVPR2016
- MCB-ensemble: Multi-modal compact bilinear pooling for visual question answering and visual grounding, EMNLP2016


### VQA仍然存在很多问题
虽然VQA已经取得了长足的进步，但是现有的算法仍然距离人类有巨大的差距。
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvbbxjxinej20n10gvmzr.jpg)

现有问题有：
1. 现有的VQA系统太依赖于问题而不是图片内容，并且语言的偏差会严重影响VQA系统性能。
  1. 只需要问题或者图片就能猜出来答案，甚至一个差的数据集(通常包含具有偏差的问题)会降低VQA系统的性能。也即越具体的问题越好！[do->play->sport play]
2. 算法性能的提升是否真的来自于注意力机制？
  1. 通过多全局图片特征（预训练的VGG-19,ResNet-101）也能达到很好的效果。
  2. 注意力机制有时候会误导VQA系统。

### 总结
可以回答任意关于图片的问题的算法将会是人工智能的里程碑。

#### 研究方向潜力股
1. 更**大**更**无偏**更**丰富**的数据集:每个问题权重不应该一样；问题的质量应该更高；答案不应该是二元的；多选题应当被淘汰
2. 更加巧妙地模型评估方式
3. 重点：可以对图片内容进行**推理**的算法！
  1. 常识推理。
  2. 空间位置。
  3. 根据不同粒度回复问题。
  



<!-- TODO: ### 批注版论文 
> 1. 黄色表示研究领域的问题
> 2. 紫色表示论文叙述内容的重点
> 3. 绿色表示该论文的解决思路
> 4. 蓝色表示该论文的公式以及定义 -->

### 引用与参考
<!--
Ex:
1. https://www.paperweekly.site/papers/notes/221
2. https://scholar.google.com/
-->
