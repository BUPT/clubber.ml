---
title: 基于分层强化学习的视频描述
date: 2019-03-10 11:49:46
author: 824zzy
comments: true
mathjax: true
categories:
  - VideoCaptioning
tags:
  - reinforcement_learning

header:
  teaser: /assets/2019/seminar-2-2-santabarbla.jpg
---

## 论文基本信息
1. 论文名：Video Captioning via Hierarchical Reinforcement Learning

2. 论文链接：https://ieeexplore.ieee.org/document/8578541/

3. 论文源码：
    - None
    
4. 关于笔记作者：
    - 朱正源,北京邮电大学研究生，研究方向为多模态与认知计算。  

---

## 论文推荐理由
视频描述中细粒度的动作描述仍然是该领域中一个巨大的挑战。该论文创新点分为两部分：1. 通过层级化的强化学习框架，使用高层manager识别粗粒度的视频信息并控制描述生成的目标，使用低层的worker识别细粒度的动作并完成目标。2. 提出Charades数据集。



---

# Video Captioning via Hierarchical Reinforcement Learning

![](https://ws1.sinaimg.cn/large/ca26ff18gy1g0xt4i7vsnj20qs0k47lv.jpg)

## Framework of model

1. Work processing
  - **Pretrained CNN** encoding stage we obtain: 
  video frame features: $v={v_i}$, where $i$ is index of frames.
  - Language Model encoding stage we obtain:
    Worker : $h^{E_w}={h_i^{E_w}}$ from low-level **Bi-LSTM** encoder
    Manager: $h^{E_m}={h_i^{E_m}}$ from high **LSTM** encoder
  - HRL agent decoding stage we obtain:
    Language description:$a_{1}a_{2}...a_{T}$, where $T$ is the length of generated caption.

2. Details in HRL agent:
    1. High-level manager:
      - Operate at lower temporal resolution.
      - Emits a goal for worker to accomplish.
    2. Low-level worker
      - Generate a word for each time step by following the goal.
    3. Internal critic 
      - Determin if the worker has accomplished the goal

3. Details in Policy Network:
    1. Attention Module:
       1. At each time step t: $c_t^W=\sum\alpha_{t,i}^{W}h^{E_w}_i$
       2. Note that attention score $\alpha_{t,i}^{W}=\frac{exp(e_{t, i})}{\sum_{k=1}^{n}exp(e_t, k)}$, where $e_{t,i}=w^{T} tanh(W_{a} h_{i}^{E_w} + U_{a} h^{W}_{t-1})$
    2. Manager and Worker:
       1. Manage: take $[c_t^M, h_t^M]$ as input to produce goal. Goal is obtained through a MLP.
       2. Worker: receive the goal $g_t$ and take the concatenation of $c_t^W, g_t, a_{t-1}$ as input, and outputs the probabilities of $\pi_t$ over all action $a_t$.
    3. Internal Critic:
       1. evaluate worker's progress. Using an RNN struture takes a word sequence as input to discriminate whether end.
       2. Internal Critic RNN take $h^I_{t-1}, a_t$ as input, and generate probability $p(z_t)$.

4. Details in Learning:
   1. Definition of Reward: 
   $R(a_t)$ = $\sum_{k=0} \gamma^{k} f(a_{t+k})$ , where　 $f(x)=CIDEr(sent+x)-CIDEr(sent)$ and $sent$ is previous generated caption.
   1. Pseudo Code of HRL training algorithm:
```py
import training_pairs
import pretrained_CNN, internal_critic
for i in range(M):
    Initial_random(minibatch)
    if Train_Worker:
        goal_exploration(enable=False)
        sampled_capt = LSTM() # a_1, a_2, ..., a_T
        Reward = [r_i for r_i in calculate_R(sampled_caption)]
        Manager(enable=False)
        worker_policy = Policy_gradient(Reward)
    elif Train_Manager:
        Initial_ramdom_process(N)
        greedy_decoded_cap = LSTM()
        Reward = [r_i for r_i in calculate_R(sampled_caption)]
        Worker(enable=False)
        manager_policy = Policy_gradient(Reward)
``` 

### All in one
![](https://ws1.sinaimg.cn/large/ca26ff18gy1g0xt54v9puj21ao0p27c8.jpg)


### 数据集
1. [MSR-VTT](http://ms-multimedia-challenge.com/2017/challenge)
> 该数据集包含50个小时的视频和26万个相关视频描述。


1. [Charades](https://mila.quebec/en/publications/public-datasets/m-vad/)
> Charades Captions:室内互动的9848个视频，包含157个动作的66500个注解，46个类别的物体的41104个标签，和共27847个文本描述。

### 实验结果
1. 实验可视化
![](https://ws1.sinaimg.cn/large/ca26ff18gy1g0xs2qfw1rj220k0hce5u.jpg)

1. 模型对比
![](https://ws1.sinaimg.cn/mw690/ca26ff18gy1g0xs1f57tkj21120hwgpl.jpg)


