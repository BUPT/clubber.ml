---
title: 对象差分注意力机制
comments: true
mathjax: true
categories:
  - VQA
tags:
  - attention

---



<!-- 论文基本信息：方便查阅和追踪 -->
<!-- 论文基本信息的获取：
1. 直接从论文pdf中获取
2. 从paperweekly首页上方搜索论文；若未检索到，点击推荐论文输入论文名即可自动获取信息
-->

## 论文基本信息
1. 论文名：Object-Difference Attention: A Simple Relational Attention for Visual Question Answering

2. 论文链接：http://www.acmmm.org/2018/accepted-papers/

3. 论文源码：
    - None
    
4. 关于作者：
    - 吴晨飞，北邮AI Lab博士

5. 关于笔记作者：
    - 朱正源,北京邮电大学研究生，研究方向为多模态与认知计算。  
    

## 论文推荐理由
<!-- Ex: 论文摘要的中文翻译
最近对话生成的神经模型为会话代理生成响应提供了很大的希望，但往往是短视的，一次预测一个话语而忽略它们对未来结果的影响。对未来的对话方向进行建模对于产生连贯，有趣的对话至关重要，这种对话需要传统的NLP对话模式借鉴强化学习。在本文中，我们将展示如何整合这些目标，应用深度强化学习来模拟聊天机器人对话中的未来奖励。该模型模拟两个虚拟代理之间的对话，使用策略梯度方法来奖励显示三个有用会话属性的序列：信息性，连贯性和易于回答（与前瞻性功能相关）。我们在多样性，长度以及人类评判方面评估我们的模型，表明所提出的算法产生了更多的交互式响应，并设法在对话模拟中促进更持久的对话。这项工作标志着基于对话的长期成功学习神经对话模型的第一步。
-->

注意机制极大地促进了视觉问答技术(VQA)的发展。注意力分配在注意力机制中起着至关重要的作用，它根据对象(如图像区域或定界框)回答问题的重要性对图像中的对象(如图像区域或包围盒)进行不同的权重。现有的工作大多集中在融合图像特征和文本特征来计算注意力分布，而不需要比较**不同的图像对象**。作为注意力的一个主要属性，**分离度**取决于不同对象之间的比较。这种比较为更好地分配注意力提供了更多的信息。为了实现对目标的可感知性，我们提出了一种对象差分注意(ODA)方法，通过在图像中实现不同图像对象之间的差值运算来计算注意概率。实验结果表明，我们基于ODA的VQA模型得到了最先进的结果。此外，还提出了一种关系注意的一般形式。除了ODA之外，本文还介绍了其他一些相关的注意事项。实验结果表明，这些关系关注在不同类型的问题上都有优势。


## 对象差分注意力机制：视觉问答中一个简单的关系注意力机制
<!-- Ex: ## 强化学习在对话生成领域的应用 -->


### 引言
#### 本文术语
<!-- 针对论文中不常用的术语进行简短的解释，方便读者理解 -->
1. 序列编码的方式：
    1. **RNN**: $y_t=f(y_{t-1},x_t)$
    2. **CNN**: $y_t=f(x_{t-1},x_t,x_{t+1})$
    3. **Attention**: $y_t=f(x_t, A, B), if A = B = X: Self Attention$

2. 注意力机制的例子
$$Attention(Q,K,V)$$

3. 应用于VQA的注意力机制编年史：
    1. one-step linear fusion
    2. multi-step linear fusion
    3. bilinear fusion
    4. multi-feature attention

4. Mutan机制



#### 论文写作动机
<!-- 当前研究领域存在的问题
Ex:
标准的Seq-to-Seq模型用于对话系统时常常使用MLE作为模型的评价标准，但这往往导致下面两个主要缺点：
系统倾向于产生一些普适性的回应，也就是dull response，这些响应可以回答很多问题但却并不是我们想要的，我们想要的是有趣、多样性、丰富的回应；
系统的回复不具有前瞻性，有时会导致陷入死循环，导致对话轮次较少。也就是产生的响应没有考虑对方是否容易回答的情况。
-->
1. 现有的工作大多集中在融合图像特征和文本特征来计算注意力分布，而**忽略了**比较不同的图像对象之间的差异。
    ![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvisv9uyyhj20i10cw46l.jpg)
    如上图，想要回答出问题`图中最高的花是什么？`，我们建立的模型就需要不仅仅关注潜在答案`玫瑰`，也应该关注`兰花`。
2. 如何合理分配现有问题的注意力？


### 解决问题的方法
#### 玫瑰例子
对于回答`图中最高的花是什么？`，一共分几步？
1. 找到图中所有的花。
2. 比较不同的花对于正确答案的重要性。

正确的答案就会在**比较**的过程中产生。若以这个例子作为启发，一种新型的注意力机制的思路便产生了：ODA在问题的指导下，通过将每个图像对象与其他所有对象进行对比，计算出图像中物体的注意注意力分布。

#### 模型细节
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjiq8dptpj20pw0bdgqo.jpg)

1. 将数据Embedding
    1. $V^f=RCNN(image)$,其中$v^f$是一个$m\times{d_v}$维的embedding，代表拉出的$m$个框。
    2. $Q^f=GRU(question)$，其中$Q^f$代表$d_q$维的问题embedding。
    3. $V=relu(Conv1d(V^f))$
    4. $Q=relu(Linear(Q^f))$

2. 对象差分注意力
$$\hat{V}=softmax([(V_i-V_j)\odot{Q}]_{m\odot{md}}W_f)^{T}V$$
该模型的优点：
    1. 通过对比(差分))，我们可以选择更重要的对象。
    2. 计算复杂度相对与传统注意力机制模型（Mutan）低。
    3. ”即插即用“的特性使得该模型十分容易应用到其他领域。
3. 决策阶段
    1. 通过对$\hat{V}$计算$p$次，并且将结果拼接在一起。
    $$\hat{Z}=[\hat{V}^{1};\hat{V}^{2};...;\hat{V}^{p}]$$
    
    > 可以参考Attention is all you need模型的multi-head
    2. 将图片的特征和问题的特征相结合
    $$H=\sum^s_{s=1}(\hat{Z}W_v^{(s)}\odot{QW_q^{(s)}})$$
    3. 预测
    $$\hat{a}=\sigma(W_{h}H)$$

#### 扩展：相关性注意力
针对模型中$(V_i-V_j)\odot{Q}$部分进行扩展，可以得到不同类型的注意力机制
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjt8ggw48j20dk06emya.jpg)



### 实验结果分析
#### 数据集
- VQA1.0 dataset
- VQA2.0 dataset
- COCO-QA dataset


#### 评估指标
- 针对VQA1.0和VQA2.0，使用准确率：
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjtavlwoxj209701hgli.jpg)
- 针对COCO_QA使用：
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjtbn6b1pj207m00tdfo.jpg)

#### 实验结果评价
- 在VQA1.0上与最先进的模型对比
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjtf0nyn4j20qs0c8wh1.jpg)
- 在VQA2.0上与最先进的模型对比
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjtfgxjdxj20ht05qmy9.jpg)
- 在VQA3.0上与最先进的模型对比
![](http://ww1.sinaimg.cn/large/ca26ff18ly1fvjtg34t3dj20mm05twfl.jpg)

### 总结
从感性的角度来说，对象差分注意力机制符合人类根据图片回答问题的思考过程。未来的研究方向应该是通过对世界的常识性知识建立一个世界模型，通过先验知识减少计算量和对大量带有标签的数据的依赖性。



### 引用与参考
<!--
Ex:
1. https://www.paperweekly.site/papers/notes/221
2. https://scholar.google.com/
-->
1. https://kexue.fm/archives/4765