---
title: 视频描述领域的第一篇深度模型论文
date: 2019-01-20 12:00 +0800
author: 824zzy
comments: true
mathjax: true
categories:
  - agi
tags:
  - video captioning 

header:
  teaser: /assets/2019/2019-01-20-zzy824.png
---

## 论文基本信息

1. 论文名：Translating Videos to Natural Language Using Deep Recurrent Neural Networks

2. 论文链接：<https://www.cs.utexas.edu/users/ml/papers/venugopalan.naacl15.pdf>

3. 论文源码：
    - [https://github.com/vsubhashini/caffe/tree/recurrent/examples/youtube](https://github.com/vsubhashini/caffe/tree/recurrent/examples/youtube )

4. 关于笔记作者：
    - 朱正源,北京邮电大学研究生，研究方向为多模态与认知计算。  

---

## 论文推荐理由

假设我们在未来已经实现了通用人工智能，当我们回首向过去看，到底哪个时代会被投票选为最重要的“Aha Moment”呢？

作为没有预知未来能力的普通人。为了回答这个问题，首先需要明确的一点就是：我们现在究竟处在实现通用人工智能之前的哪个位置？

一个常用的比喻便是，如果把从开始尝试到最终实现通用人工智能比作一条一公里的公路的话。大部分人可能会认为我们已经走了200米到500米之间。但是真实的情况可能是，我们仅仅走过了5厘米不到。

因为在通往正确道路的各种尝试中，有很大一部分会犯方向性错误。当我们在错误的道路上越走越远的时候，那么肯定无法到达终点。推倒现有成果重新来过便是不可避免的。我们需要时时刻刻保持谨小慎微，以躲避“岔路口”。

现在有理由相信（其实是因为不得不掩耳盗铃），我们正走在一条正确的道路上。如果非要说现在的技术有哪些让我感觉不那么符合我的直觉的地方的话，我肯定会抢着回答：We are not living in the books or images.

公元前五亿年前，当我们还是扁形虫的时候，那时候我们便会在未知的环境中为了生存下去作出连续的决策。

公元前两亿年前，我们进化成啮齿类动物，并且拥有了一套完整的操作系统。不变的是，不断连续变化的生存环境。

公元前四百万年前，原始人类进化出了大脑皮层之后，终于拥有了进行推理和思考的能力。但是这一切是在他们发明文字和语言之前。

现如今，当人类巨灵正在尝试创造出超越本身智能的超智能体时，却神奇的忽略了超智能体也应该生存在不断变化的、充满危险的世界之中。

回到最开始的问题，我一定会把票投在利用神经模型来处理视频流的模型上。

---

## Translating Videos to Natural Language Using Deep Recurrent Neural Networks

### 视频描述任务介绍

根据视频生成单句的描述，一例胜千言：

![img](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzcxfmvyxuj20si0hqqfg.jpg)

　　A monkey pulls a dog’s tail and is chased by the dog.

### 视频描述的前世

管道方法（PipeLine Approach）

1. 从视频中识别出`主语`、`动作`、`宾语`、`场景`
2. 计算被识别出实体的置信度
3. 根据最高置信度的实体与预先设置好的模板，进行句子生成

　在神经模型风靡之前，传统方法集中使用**隐马尔科夫模型识别实体**和**条件随机场生成句子**

### 神经模型的第一次尝试

![LSTM-YT模型](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzcwjf53bsj214x0ksajx.jpg)

- 从视频中，每十帧取出一帧进行分析

　![img](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzczmke1dbj20vg0astdq.jpg)
　人类眼睛的帧数是每秒24帧，从仿生学的观点出发，模型也不需要处理视频中所有的帧。再对视频帧进行缩放以便计算机进行处理。

- 使用CNN提取特征并进行平均池化（Mean Pooling）

　![img](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzczv0iwy6j20x40mktg0.jpg)

- 预训练的Alexnet[2012]:在120万张图片上进行预训练[ImageNet LSVRC-2012]，提取最后一层（第七层全连接层）的特征（4096维）。注意：提取的向量不是最后进行分类的1000维特征向量。
  
  ![Alexnet](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzd0iak8vhj216o0eqacn.jpg)

- 对所有的视频帧进行池化

- 句子生成

　![RNN生成句子](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzd06rquyyj20qk0nwgo6.jpg)

### 迁移学习和微调模型

- 在图片描述任务进行预训练

　![transfer-learning from image captioning](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fzd0skao7sj216c0jm0zn.jpg)

- 微调（Fine-tuning）
　需要注意的是，在视频描述过程中：
  - 将输入从图片转换为视频；
  - 添加了平均池化特征这个技巧；
  - 模型进行训练的时候使用了更低的学习率

### 实验细节

#### 数据集

- [Microsoft Research Video Description dataset](http://www.cs.utexas.edu/users/ml/clamp/videoDescription/)

> 1970条Youtobe视频片段：每条大约10到30秒，并且只包含了一个活动，其中没有对话。1200条用作训练，100条用作验证，670条用作测试。

![dataset](https://ws1.sinaimg.cn/mw690/ca26ff18ly1fzd1cmxyalj217g0lcdyf.jpg)

- [MSCOCO数据集下载](https://blog.csdn.net/daniaokuye/article/details/78699138)
- [Flickr30k数据集下载](https://blog.csdn.net/gaoyueace/article/details/80564642)

#### 评估指标

- SVO(Subject, Verb, Object accuracy)
- BLEU
- METEOR
- Human evaluation

#### 实验结果

- SVO正确率：

　![result on SVO](https://ws1.sinaimg.cn/mw690/ca26ff18ly1fzd5gnjzg6j20p20f8n0d.jpg)

- BLEU值和METEOR值

　![result on BLEU and METEOR](https://ws1.sinaimg.cn/mw690/ca26ff18ly1fzd5p0xo78j20nm0aotak.jpg)

### 站在2019年回看2015年的论文

以19年的后见之明来考察这篇论文，虽然论文没有Attention和强化学习加持的，但是也开辟了用神经模型完成视频描述任务的先河。

回顾一下以前提出的问题，如何才能实现：

  1. 常识推理。
  2. 空间位置。
  3. 根据不同粒度回复问题。

答案很有可能在我们身上，大脑皮质中的前额皮质掌管着人格（就是你脑中出现的那个声音，就是他）。大脑皮质虽然仅仅是大脑最外层的两毫米厚的薄薄一层（[没错，我确定就是两毫米](https://zh.wikipedia.org/wiki/%E5%A4%A7%E8%84%91%E7%9A%AE%E8%B4%A8)）,但是它起到的作用却是史无前例的。

以大脑皮质作为启发，最少我们也需要让人工大脑皮质也“生存”在一个类似于现实世界中的环境当中。因此视频是一个很好的起点，但也仅仅是个起点。

### 引用与参考

- [Neuralink and the Brain’s Magical Future](https://waitbutwhy.com/2017/04/neuralink.html)
- [Translating Videos to Natural Language Using Deep Recurrent Neural Networks -- Slides](https://www.cs.utexas.edu/~vsub/pdf/Translating_Videos_slides.pdf)
- [A Walk-through of AlexNet](https://medium.com/@smallfishbigsea/a-walk-through-of-alexnet-6cbd137a5637)
- [Collecting Multilingual Parallel Video Descriptions Using Mechanical Turk](https://www.cs.utexas.edu/users/ml/clamp/videoDescription/#data)
- [大脑皮质](https://zh.wikipedia.org/wiki/%E5%A4%A7%E8%84%91%E7%9A%AE%E8%B4%A8)
