---
title: 对话AI的论文列表
date: 2018-08-09 12:31:31
comments: true
mathjax: true
categories: 
    - AI
tags: 
    - chatbot 
    - conversationalAI
    - nlp
    - paper
---

> 论文列表格式  
> &emsp;论文发表年份： 论文题目&论文链接：第一作者（第一作者所属学校/机构），代码链接

## Overview
### Existing Models of Dialog System
#### Task-Oriented Dialog
- 13: [**POMDP-Based Statistical Spoken Dialog Systems: A Review**](https://ieeexplore.ieee.org/document/6407655/): Steve Young(Cambridge University)
- 11: [**Spoken Language Understanding: Systems for Extracting Semantic Information from Speech**](https://www.wiley.com/en-us/Spoken+Language+Understanding:+Systems+for+Extracting+Semantic+Information+from+Speech-p-9780470688243): Book!
- 11:[**Data-Driven Response Generation in Social Media**](http://www.aclweb.org/anthology/D11-1054): Alan Ritter(University of Washington Seattle)
- 15: [**A Neural Network Approach to Context-Sensitive Generation of Conversational Responses**](https://www.aclweb.org/anthology/N/N15/N15-1020.pdf): Alessandro Sordoni(Universite de Montreal)

- 15: [**A Neural Conversational Model**](https://arxiv.org/pdf/1506.05869.pdf): Oriol Vinyals(Google), [**code**](https://github.com/Conchylicultor/DeepQA) via tensorflow
- 15: [**Neural Responding Machine for Short-Text Conversation**](https://www.aclweb.org/anthology/P15-1152): Lifeng Shang(Noah's Ark Lab), [**code**](https://github.com/stamdlee/DeepLearningFramework) via theano and tensorflow

### Traditional NLP component stack
#### Challenge of NLP
- 09: [**SPEECH and LANGUAGE PROCESSING An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition Second Edition**](https://www.cs.colorado.edu/~martin/slp.html): book 

### Deep Semantic Similarity Model(DSSM)
#### application scenarios
1. Web search
	- 13: [**Learning deep structured semantic models for web search using clickthrough data**](http://dl.acm.org/citation.cfm?id=2505665): Po-Sen Huang(University of Illinois at Urbana-Champaign), [**code**](https://github.com/wangtianqi1993/DL-WebSearch) via tensorflow
	- 14: [**A Latent Semantic Model with Convolutional-Pooling Structure for Information Retrieval**](http://dl.acm.org/citation.cfm?doid=2661829.2661935): Yelong Shen(Microsoft Research)
	- 16: [**Deep Sentence Embedding Using Long Short-Term Memory Networks: Analysis and Application to Information Retrieval**](https://arxiv.org/abs/1502.06922): Hamid Palangi, [**code**](https://github.com/zhaosm/dssm-lstm)
2. Entity linking
	- 14: [**Modeling Interestingness with Deep Neural Networks**](http://anthology.aclweb.org/D/D14/D14-1002.pdf): Jianfeng Gao(Microsoft Research)
3. Image captioning
	- 15: [**From Captions to Visual Concepts and Back**](https://arxiv.org/abs/1411.4952): Hao Fang&Li Deng(Microsoft Research)
4. Machine Translation
    - [**Learning Continuous Phrase Representations for Translation Modeling**](http://aclweb.org/anthology/P/P14/P14-1066.pdf): Jianfeng Gao(Microsoft Research)
5. Online recommendation
	- [**duplicate**] 14: [**Modeling Interestingness with Deep Neural Networks**](http://anthology.aclweb.org/D/D14/D14-1002.pdf): Jianfneg Gao(Microsoft Research)

#### Framework of Model
- [**duplicate**] 13: [**Learning deep structured semantic models for web search using clickthrough data**](http://dl.acm.org/citation.cfm?id=2505665): Po-Sen Huang(University of Illinois at Urbana-Champaign), [**code**]
    - [**duplicate**] 14: [**A Latent Semantic Model with Convolutional-Pooling Structure for Information Retrieval**](http://dl.acm.org/citation.cfm?doid=2661829.2661935): Yelong Shen(Microsoft Research)
- 16: [**Deep Sentence Embedding Using Long Short-Term Memory Networks: Analysis and Application to Information Retrieval**](https://arxiv.org/abs/1502.06922): Hamid Palangi, [**code**](https://github.com/zhaosm/dssm-lstm)
- [Sent2Vec](http://aka.ms/sent2vec): software by microsoft

#### Go beyound DSSM
- [**duplicate**] 15: [**From Captions to Visual Concepts and Back**](https://arxiv.org/abs/1411.4952): Hao Fang&Li Deng(Microsoft Research)

-----

## Question answeriing(QA) and Machine Readiing Comprehension(MRC)
### Open-Domain Question Answering
#### Knowledge Base-QA
1. Symbolic approach via Large-scale knowledge graphs
    - 98: [MindNet: acquiring and structuring semantic information from text](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/COLING-98-richardson-dolan-vanderwende.pdf): Stephen D.Richardson(Microsoft Research)
    - 13: [Semantic Parsing on Freebase from Question-Answer Pairs](http://www.aclweb.org/anthology/D13-1160): Jonathan Berant(Stanford University)
    - 15: [Attention with Intention for a Neural Network Conversation Model](https://arxiv.org/pdf/1510.08565.pdf): Kaisheng Yao(Microsoft Research)
    - 14: [Knowledge-Based Question Answering as Machine Translation](http://www.aclweb.org/anthology/P14-1091): Junwei Bao(Harbin Institute of Technology)
    - 15: [Semantic Parsing via Staged Query Graph Generation: Question Answering with Knowledge Base](http://aclweb.org/anthology/P15-1128):Wen-tau Yih(Microsoft Research)
1. **ReasoNet** with Shared Memory
    - [**duplicate**] 16: [Link Prediction using Embedded Knowledge Graphs](https://arxiv.org/pdf/1611.04642.pdf?): Yulong Shen（Microsoft&Google Research）
    - 17: [ReasoNet: Learning to Stop Reading in Machine Comprehension](https://arxiv.org/pdf/1609.05284.pdf):Yelong Shen(Microsoft Research)
  
2. Search Controller in **ReasoNet** 
    - [**duplicate**] 16: [Link Prediction using Embedded Knowledge Graphs](https://arxiv.org/pdf/1611.04642.pdf?): Yulong Shen（Microsoft&Google Research）
3. **ReasoNet** in symbolic vs neural space
    - Symbolic is comprehensible but not robust
	    - 11: [Random Walk Inference and Learning in A Large Scale Knowledge Base](http://www.cs.cmu.edu/~tom/pubs/lao-emnlp11.pdf):Ni Lao(Carnegie Mellon University)
        - 98: [MindNet: acquiring and structuring semantic information from text](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/COLING-98-richardson-dolan-vanderwende.pdf):Stephen D.Richardson(Microsoft Research)
    - Neural is robust but not comprehensible
        - [**duplicate**] 16: [Link Prediction using Embedded Knowledge Graphs](https://arxiv.org/pdf/1611.04642.pdf?): Yulong Shen（Microsoft&Google Research）
        - 15: [EMBEDDING ENTITIES AND RELATIONS FOR LEARNING AND INFERENCE IN KNOWLEDGE BASES](https://arxiv.org/abs/1412.6575):Bishan Yang(Cornell University), [TensorFlow code](https://github.com/thunlp/OpenKE/blob/master/models/DistMult.py), [PyTorch code](https://github.com/thunlp/OpenKE/blob/OpenKE-PyTorch/models/DistMult.py)
    - Hybrid is robust and  comprehensible
        - 18: [M-Walk: Learning to Walk in Graph with Monte Carlo Tree Search](https://arxiv.org/pdf/1802.04394.pdf):Yelong Shen(Microsoft Research&Tecent AI Lab)
	    - 18: [DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning](https://arxiv.org/abs/1707.06690):Wenhan Xiong(University of California,Santa Barbara), [code1](https://github.com/xwhan/DeepPath) [code2](https://github.com/arunarn2/DeepPathwithTensorforce)
	    - 18: [GO FOR A WALK AND ARRIVE AT THE ANSWER: REASONING OVER PATHS IN KNOWLEDGE BASES USING REINFORCEMENT LEARNING](https://arxiv.org/abs/1711.05851):Rajarshi Das(University of Massachusetts,Amherst), 
5. Multi-turn KB-QA
    ~~- Programmed Dialogue policy
	    - 15: [A Probabilistic Framework for Representing Dialog Systems and Entropy-Based Dialog Management through Dynamic Stochastic State Evolution](https://arxiv.org/pdf/1504.07182.pdf):Ji Wu(IEEE)~~
    - Trained via RL Dialogue policy
	    - 16: [A Network-based End-to-End Trainable Task-oriented Dialogue System](https://arxiv.org/abs/1604.04562):Tsung-Hsien Wen(Cambridge University), [Theano code](https://github.com/shawnwun/NNDIAL)
	    - 17: [Towards End-to-End Reinforcement Learning of Dialogue Agents for Information Access](https://arxiv.org/abs/1609.00777):Bhuwan Dhingra(Carnegie Mellon University), [Theano code](https://github.com/MiuLab/KB-InfoBot)

#### Text-QA
1. MS MARCO
    - 16: [MS MARCO: A Human Generated MAchine Reading COmprehension Dataset](https://arxiv.org/abs/1611.09268):Tri Nguyan(Microsoft AI&Research)
2. SQuAD
    - 16: [SQuAD: 100,000+ Questions for Machine Comprehension of Text](https://nlp.stanford.edu/pubs/rajpurkar2016squad.pdf):Pranav Rajpurkar(Stanford University)
 
### Neural MRC Models
#### BiDAF
- 16: [BI-DIRECTIONAL ATTENTION FLOW FOR MACHINE COMPREHENSION](https://arxiv.org/pdf/1611.01603.pdf):Minjoon Seo(University of Washington)
    - [code1](https://github.com/imraviagrawal/ReadingComprehension)
    - [code2](https://github.com/bentrevett/bidaf) 
    - [code3](https://github.com/akhil-vader/MachineComprehension_SQuAD) 
    - [code4](https://github.com/RamkishanPanthena/Machine-Comprehension-using-SQuAD-Dataset)

#### SAN
- 18: [Stochastic Answer Networks for Machine Reading Comprehension](https://arxiv.org/pdf/1712.03556.pdf): Xiaodong Liu(Microsoft Research,Redmond), [code](https://github.com/kevinduh/san_mrc)

#### **Neural MRC Models on SQuAD**
1. Encoding: map each text span to a semantic vector
    - Word Embedding
        - 14: [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf):Jeffrey Pennington(Stanford University)
            - [code:midi-glove](https://github.com/brangerbriz/midi-glove)
            - [code:wiki-glove](https://github.com/fdurant/wiki_glove)
        - 13: [Distributed Representations of Words and Phrases and their Compositionality](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf):Tomas Mikolov(Google Inc.)
            - [code1](https://github.com/brijml/mikolov_word2vec)
            - [code2](https://github.com/shuuchen/keras_word2vec)
   - Context Embedding
    1. capture context info for each word
        - 16: [context2vec: Learning Generic Context Embedding with Bidirectional LSTM](http://aclweb.org/anthology/K16-1006):Oren Melamud(Bar-Ilan University)
        - 18: [Deep contextualized word representations](https://arxiv.org/abs/1802.05365):Matthew E.Peters(Allen Institute for Artificial Intelligence), [code](https://github.com/zqhZY/ner_elmo)
        - 18: [QANET: COMBINING LOCAL CONVOLUTION WITH GLOBAL SELF-ATTENTION FOR READING COMPREHENSION](https://arxiv.org/pdf/1804.09541.pdf):Adams Wei Yu(CMU&Google Brain)
            - [code1](https://github.com/ni9elf/QANet)
            - [code2](https://github.com/BangLiu/QANet-PyTorch)
    2. Context Embedding via BiLSTM/ELmo
        - [**duplicate**] 18: [Deep contextualized word representations](https://arxiv.org/abs/1802.05365):Matthew E.Peters(Allen Institute for Artificial Intelligence), [code](https://github.com/zqhZY/ner_elmo)
        - 17: [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107):Bryan McCann(SalesForce)
        - 16: [duplicate][context2vec: Learning Generic Context Embedding with Bidirectional LSTM](http://aclweb.org/anthology/K16-1006):Oren Melamud(Bar-Ilan University)
    3. Context Embedding
        - [**duplicate**] 18: [QANET: COMBINING LOCAL CONVOLUTION WITH GLOBAL SELF-ATTENTION FOR READING COMPREHENSION](https://arxiv.org/pdf/1804.09541.pdf):Adams Wei Yu(CMU&Google Brain)
            - [code1](https://github.com/ni9elf/QANet)
            - [code2](https://github.com/BangLiu/QANet-PyTorch)
   
   - Query-context/Content-query attention

2. Reasoning: rank and re-rank semantic vectors
    - Multi-step reasoning for Text-QA
        - [**duplicate**] 17: [ReasoNet: Learning to Stop Reading in Machine Comprehension](https://arxiv.org/pdf/1609.05284.pdf):Yelong Shen(Microsoft Research)

    - Stochastic Answer Net
        - [**duplicate**] 18: [Stochastic Answer Networks for Machine Reading Comprehension](https://arxiv.org/pdf/1712.03556.pdf): Xiaodong Liu(Microsoft Research,Redmond), [code](https://github.com/kevinduh/san_mrc)

----------

## Task-oriented dialogues
### overview
#### A Example Dialogue with Movie-Bot
- [source code](https://github.com/MiuLab/TC-Bot)
#### Conversation as Reinforcement Learning
- 00: [A Stochastic Model of Human-Machine Interaction for Learning Dialog Strategies](http://www.thepieraccinis.com/publications/2000/IEEE_TSAP_00.pdf): Esther Levin(IEEE)
- 00: [Optimizing Dialogue Management with Reinforcement Learning: Experiments with the NJFun System](https://web.eecs.umich.edu/~baveja/Papers/RLDSjair.pdf):Satinder Singh(AT&T Labs)
- 07: [Partially observable Markov decision processes for spoken dialog systems](http://svr-www.eng.cam.ac.uk/~sjy/papers/wiyo07-j.pdf):Jason D.Williams(AT&T Labs)
#### Dialogue System Evaluation(Simulated Users)
1. Agenda based
    - 09: [The Hidden Agenda User Simulation Model](https://ieeexplore.ieee.org/document/4806280/):Jost Schatzmann(IEEE)
    - [source code](https://github.com/MiuLab/TC-Bot) 
2. Model based
    - 16: [A Sequence-to-Sequence Model for User Simulation in Spoken Dialogue Systems](https://arxiv.org/abs/1607.00070): Layla El Asri(Maluuba Research)
    - 17: [End-to-End Task-Completion Neural Dialogue Systems](https://arxiv.org/pdf/1703.01008.pdf):Xiujun Li(Microsoft Research&National Taiwan University)

### traditional approache
#### Decison-theoretic View of Dialogue Management
- [**duplicate**] 00: [Optimizing Dialogue Management with Reinforcement Learning: Experiments with the NJFun System](https://web.eecs.umich.edu/~baveja/Papers/RLDSjair.pdf):Satinder Singh(AT&T Labs)
- 00: [A Stochastic Model of Human-Machine Interaction for Learning Dialog Strategies](http://www.thepieraccinis.com/publications/2000/IEEE_TSAP_00.pdf): Esther Levin(IEEE)
- 00: [Learning Optimal Dialogue Strategies: A Case Study of a Spoken Dialogue Agent for Email](http://www.aclweb.org/anthology/P98-2219): Marilyn A.Walker(ATT Labs Research)
- 02: [Automatic learning of dialogue strategy using dialogue simulation and reinforcement learning](https://dl.acm.org/citation.cfm?id=1289246):Konrad Scheffler(Cambridge University)

#### Language Understanding Uncertainty: POMDP as a principled framework
- 00: [Spoken Dialogue Management Using Probabilistic Reasoning](http://www.mit.edu/~nickroy/papers/acl00.pdf): Nicholas Roy(Carnegie Mellon University)
- 01: [Spoken Dialogue Management as Planning and Acting under Uncertainty](http://www.wytsg.org:88/reslib/400/180/110/020/010/130/L000000000233767.pdf):Bo Zhang(Tech. of China)
- 07: [Partially observable Markov decision processes for spoken dialog systems](http://svr-www.eng.cam.ac.uk/~sjy/papers/wiyo07-j.pdf):Jason D.Williams(AT&T Labs)

#### scaling up Dialogue Optimization
1. Use approxmiate POMDP algorithms leveraging problem-specific structure
    - 00: [Automatic learning of dialogue strategy using dialogue simulation and reinforcement learning](http://www.mit.edu/~nickroy/papers/acl00.pdf):Konrad Scheffler(Cambridge University)
    - 07: [Partially observable Markov decision processes for spoken dialog systems](http://svr-www.eng.cam.ac.uk/~sjy/papers/wiyo07-j.pdf):Jason D.Williams(AT&T Labs)
2. Use Reinforcement Learning algorithms with function approximation
    - 08: [Hybrid Reinforcement/Supervised Learning of Dialogue Policies from Fixed Data Sets](http://www.aclweb.org/anthology/J08-4002): James Henderson
    - 09: [Reinforcement Learning for Dialog Management using Least-Squares Policy Iteration and Fast Feature Selection](https://pdfs.semanticscholar.org/a950/d7836e101e7d649791714d8383a804a6f671.pdf): Lihong Li(Rutgers University)
    - 14: [Incremental on-line adaptation of POMDP-based dialogue managers to extended domains](http://mi.eng.cam.ac.uk/~sjy/papers/gktb14.pdf):M.Gasic[Cambridge University]


### Natural language understanding and dialogue state tracking
#### Language Understanding
1. DNN for Domain/Intent Classification
    - 15:  [Recurrent Neural Network and LSTM Models for Lexical Utterance Classification](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/RNNLM_addressee.pdf): Suman Raviuri(University of California,Berkeley)

2. Slot filling
    - 16: [Multi-Domain Joint Semantic Frame Parsing using Bi-directional RNN-LSTM](https://www.csie.ntu.edu.tw/~yvchen/doc/IS16_MultiJoint.pdf): Dilek Hakkani-Tur(Microsoft Research)

3. Further details on NLU
    - [ppt](https://www.csie.ntu.edu.tw/~yvchen/doc/OpenDialogue_Tutorial_IJCNLP.pdf)
    - E2E MemNN for Contectual LU: [End-to-End Memory Networks with Knowledge Carryover for Multi-Turn Spoken Language Understanding](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/IS16_ContextualSLU.pdf): Yun-Nung Chen(National Taiwan University )
    - [**duplicate**] LU Importance: 17: [End-to-End Task-Completion Neural Dialogue Systems](https://arxiv.org/pdf/1703.01008.pdf):Xiujun Li(Microsoft Research&National Taiwan University)

#### Dialogue State Tracking(DST)
1. DSTC(Dialog State Tracking Challenge)
    - [DSTC1 official website](https://www.microsoft.com/en-us/research/event/dialog-state-tracking-challenge/)
    - [DSTC2&3 official website](http://camdial.org/~mh521/dstc/)
    - [DSTC4 official website](http://www.colips.org/workshop/dstc4/)
    - [DSTC5 official website](http://workshop.colips.org/dstc5/)
2. Neural Belief Tracker
    - 16: [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777): Nikola Mrksic(University of Cambridge)

3. NN-Based DST
    - 13: [Deep Neural Network Approach for the Dialog State Tracking Challenge](http://www.anthology.aclweb.org/W/W13/W13-4073.pdf): Matthew Henderson(University of Cambridge)
    - 15: [Multi-domain Dialog State Tracking using Recurrent Neural Networks](https://arxiv.org/abs/1506.07190): Nikola Mrksic(University of Cambridge)
    - [**duplicate**] 16: [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777): Nikola Mrksic(University of Cambridge)



### Deep RL for dialogue policy learning
#### Two main classed of RL algorithms
1. Value function based:
    - 15: [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236): Volodymyr Minh
        - [code1](https://github.com/devsisters/DQN-tensorflow) by tensorflow
        - [code2](https://github.com/pianomania/DQN-pytorch) by pytorch
    - 16: [Towards End-to-End Learning for Dialog State Tracking and Management using Deep Reinforcement Learning](https://arxiv.org/pdf/1606.02560.pdf): Tiancheng Zhao(Carnegie Mellon University)
2. Policy based:
    - 92: [Simple statistical gradient-following algorithms for connectionist reinforcement learning](https://doi.org/10.1007/BF00992696): Ronald J.Williams
    - 17: [On-line Active Reward Learning for Policy Optimisation in Spoken Dialogue Systems](http://www.aclweb.org/anthology/P/P16/P16-1230.pdf): Pei-Hao Su(University of Cambridge)
#### Domain Extension and Exploration(BBQ network)
- 18: [BBQ-Networks: Efficient Exploration in Deep Reinforcement Learning for Task-Oriented Dialogue Systems](https://arxiv.org/pdf/1608.05081.pdf): Zachary Lipton(Carnegir Mellon University)

#### Composite-task Dialogues
1. A Hierarchical Policy Learner
    - 98: [Reinforcement Learning with Hierarchies of Machines](http://papers.nips.cc/paper/1384-reinforcement-learning-with-hierarchies-of-machines.pdf): Ronald Parr(UC Berkeley)
    - 17: [Composite Task-Completion Dialogue Policy Learning via Hierarchical Deep Reinforcement Learning](https://arxiv.org/abs/1704.03084): Baolin Peng(Microsoft Research)
2. Integrating Planning for Dialogue Policy Learning
    - 18: [Deep Dyna-Q: Integrating Planning for Task-Completion Dialogue Policy Learning](https://arxiv.org/abs/1801.06176): Baolin Peng(Microsoft Research) , [code](https://github.com/MiuLab/DDQ)

### Decision-theoretic View of Dialogue Management
#### Hybrid Code Networks
- 17: [Hybrid Code Networks: practical and efficient end-to-end dialog control with supervised and reinforcement learning](https://arxiv.org/abs/1702.03274): Jason D. Williams(Microsoft Research)
#### Differentiating KB Accesses
- [**duplicate**] 17: [Towards End-to-End Reinforcement Learning of Dialogue Agents for Information Access](https://arxiv.org/abs/1609.00777):Bhuwan Dhingra(Carnegie Mellon University)
#### An E2E Neural Dialogue System
- [**duplicate**] 17: [End-to-End Task-Completion Neural Dialogue Systems](https://arxiv.org/pdf/1703.01008.pdf):Xiujun Li(Microsoft Research&National Taiwan University)

----------

## Fully data-driven conversation models and chatbots
### Historical overview
#### Response retrival system
- 10: [Filter, Rank, and Transfer the Knowledge: Learning to Chat](https://aritter.github.io/chat.pdf): 
Alan Ritter(University of Washington)

#### Response generation using Statistical Machine Translation
- 11:  [Data-Driven Response Generation in Social Media](http://www.aclweb.org/anthology/D11-1054): Alan Ritter(University of Washington)
  
#### First neural response generation systems
1. Neural Models for Response Generation
    - 15: [A Neural Network Approach to Context-Sensitive Generation of Conversational Responses](https://www.aclweb.org/anthology/N/N15/N15-1020.pdf): Alessandro Sordoni(University de Montreal)
    - 15: [A Neural Conversational Model](https://arxiv.org/pdf/1506.05869.pdf): Oriol Vinyals(Google .Inc)
    - 15: [Neural Responding Machine for Short-Text Conversation](https://www.aclweb.org/anthology/P15-1152): Lifeng Shang(Noah's Ark Lab), [code](https://github.com/stamdlee/DeepLearningFramework)
2. Neural conversation engine: 
    - 16: [A Diversity-Promoting Objective Function for Neural Conversation Models](http://arxiv.org/abs/1510.03055): Jiwei Li(Stanford University)

### challenges and remedies
#### Challenge: The blandness problem
- [**duplicate**] 16: [A Diversity-Promoting Objective Function for Neural Conversation Models](http://arxiv.org/abs/1510.03055): Jiwei Li(Stanford University)
#### Challenge: The consistency problem
1. Solution: Personalized Response Generation
    - Microsoft Personality chat:speaker embedding LSTM: [A Persona-Based Neural Conversation Model](https://arxiv.org/abs/1603.06155): Jiwei Li(Stanford University), [code](https://github.com/fionn-mac/A-Persona-Based-Neural-Conversation-Model) via Pytorch
2. Personal modeling as multi-task learning
    - 17: [Multi-Task Learning for Speaker-Role Adaptation in Neural Conversation Models](https://arxiv.org/abs/1710.07388): Yi Luan(University of Washington)
3. Improving personalization with multiple losses
    - 16: [Conversational Contextual Cues: The Case of Personalization and History for Response Ranking](https://arxiv.org/pdf/1606.00372.pdf): Rami Al-Rfou(Google .Inc)
#### Challenge: Long conversational context
1. It can be challenging for LSTM/GRU to encode very long context
    - 18: [Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context](https://arxiv.org/abs/1805.04623): Urvashi Khadelwal(Stanford University)
2. Hierarchical Encoder-Decoder(HRED), [code](https://github.com/urvashik/lm-context-analysis)
    - 16: [Building End-to-End Dialogue Systems Using Generative Hierarchical Neural Network Models](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/11957/12160): Iulian V.Serban(University de Montreal), [code](https://github.com/hsgodhia/hred)
3. Hierarchical Latent Variable Encoder-Decoder(VHRED)
    - 17: [A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialogues](http://www.cs.toronto.edu/~lcharlin/papers/vhred_aaai17.pdf): Iulian V. Serban

### Grounded conversation models
#### A Knowledge-Grounded Neural Conversation Model
- 15: [End-To-End Memory Networks](https://arxiv.org/pdf/1503.08895.pdf): Sainbayar Sukhbaatar(New York University)
    - [code1](https://github.com/carpedm20/MemN2N-tensorflow) via Tensorflow
    - [code2](https://github.com/domluna/memn2n) via Tensorflow
    - [code3](https://github.com/vinhkhuc/MemN2N-babi-python) for bAbI QA tasks
- 17: [A Knowledge-Grounded Neural Conversation Model](https://arxiv.org/abs/1702.01932): Marjan Gahzvininejad(USC)
#### Grounded E2E Dialogue Systems
- 16: [Visual Dialog](https://arxiv.org/abs/1611.08669): Abhishek Das(Georgia Institute of Tehhnology)
    - [code1](https://github.com/batra-mlp-lab/visdial) via Lua
    - [code2](https://github.com/jiasenlu/visDial.pytorch) via Pytorch
- 17: [Image-Grounded Conversations: Multimodal Context for Natural Question and Response Generation](https://arxiv.org/abs/1701.08251): Nasrin Mostafazadeh(University of Rochster)
- 18: [Emotional Dialogue Generation using Image-Grounded Language Models](https://www.microsoft.com/en-us/research/uploads/prod/2018/04/huber2018chi.small_.pdf):Bernd Huber(Harvard University)

### Beyond supervised learning(Deep Reinforcement Learning for E2E Dialogue)
- 16: [Deep Reinforcement Learning for Dialogue Generation](https://arxiv.org/abs/1606.01541):Jiwei Li(Stanford University)
    - [code1](https://github.com/liuyuemaicha/Deep-Reinforcement-Learning-for-Dialogue-Generation-in-tensorflow) via Tensorflow
    - [code2](https://github.com/agsarthak/Goal-oriented-Dialogue-Systems) via keras
    - [code3](https://github.com/jiweil/Neural-Dialogue-Generation) by Jiwei Li



### Data and evaluation
#### Conversational datasets(for social bots, E2E dialogue research)
- 15: [A Survey of Available Corpora for Building Data-Driven Dialogue Systems](https://arxiv.org/abs/1512.05742): Iulian Vlad Serban(Universite de Montreal)
#### Evaluating E2E Dialogue Systems via Autumatic evaluation
1. Machine-Translation-Based Metric
    - 02: [BLEU: a Method for Automatic Evaluation of Machine Translation](https://www.aclweb.org/anthology/P02-1040.pdf): Kishore Papineni(IBM), [code](https://github.com/abidasari/NLPHW4)
    - 02: [Automatic Evaluation of Machine Translation Quality Using N-gram Co-Occurrence Statistics](http://www.mt-archive.info/HLT-2002-Doddington.pdf): George Doddington
2. Sentence-level correlation of MT metrics:
    - 16: [How NOT To Evaluate Your Dialogue System: An Empirical Study of Unsupervised Evaluation Metrics for Dialogue Response Generation](https://aclweb.org/anthology/D16-1230): Chia-Wei Liu(McGill University)
    - 15: [Accurate Evaluation of Segment-level Machine Translation Metrics](http://www.aclweb.org/anthology/N15-1124): Yvette Graham(The University of Melbourne)

#### The importance of sample size
- [**duplicate**] 02: [BLEU: a Method for Automatic Evaluation of Machine Translation](https://www.aclweb.org/anthology/P02-1040.pdf): Kishore Papineni(IBM), [code](https://github.com/abidasari/NLPHW4)
- 06: [Statistical Significance Tests for Machine Translation Evaluation](http://homepages.inf.ed.ac.uk/pkoehn/publications/bootstrap2004.pdf): Philipp Kowehn(MIT)

#### Corpus-level Correlation
- [**duplicate**] 02: [BLEU: a Method for Automatic Evaluation of Machine Translation](https://www.aclweb.org/anthology/P02-1040.pdf): Kishore Papineni(IBM), [code](https://github.com/abidasari/NLPHW4)
- [**duplicate**] 06: [Statistical Significance Tests for Machine Translation Evaluation](http://homepages.inf.ed.ac.uk/pkoehn/publications/bootstrap2004.pdf): 

### Chatbot in public 
#### Social Bots: commercial systems
1. For end users
    - Replika.ai system description: [replika_ai](https://github.com/lukalabs/replika-research/blob/master/scai2017/replika_ai.pdf): Slides
    - XiaoIce:
	15:[Chatting With Xiaoice](https://www.nytimes.com/interactive/2015/07/27/science/chatting-with-xiaoice.html): News
2. For bot developers
    - [**duplicate**] Microsoft Personality chat:speaker embedding LSTM: [A Persona-Based Neural Conversation Model](https://arxiv.org/abs/1603.06155): Jiwei Li(Stanford University), [code](https://github.com/fionn-mac/A-Persona-Based-Neural-Conversation-Model) via Pytorch
    - Microsoft Personality chat's API: [Project Personality Chat's url](https://labs.cognitive.microsoft.com/en-us/project-personality-chat) 

#### Open Benchmarks
1. Alexa Challenge
    - website: [Alexa Prize Proceedings](https://developer.amazon.com/alexaprize/proceedings)

2. Dialogue System Technology Challenge(DSTC)
    - [DSTC7](http://workshop.colips.org/dstc7)
    - Visual-Scene: [DSTC7-Audio-Visual-Scene-Aware-Dialog-AVSD-Challenge 2018](https://github.com/hudaAlamri/DSTC7-Audio-Visual-Scene-Aware-Dialog-AVSD-Challenge)
    - background article:
	[DSTC7-End-to-End-Conversation-Modeling 2018](https://github.com/DSTC-MSR-NLP/DSTC7-End-to-End-Conversation-Modeling)
    - Registration Link:
	[DSTC7 Registration](http://workshop.colips.org/dstc7/call.html)
