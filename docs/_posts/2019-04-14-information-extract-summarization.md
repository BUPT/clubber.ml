## 论文基本信息
1. 论文名：Natural Language Processing for Information Extraction

2. 论文链接：http://arxiv.org/abs/1807.02383



---

## Natural Language Processing for Information Extraction

### Information Extraction Tasks
1. Parts-of-Speech (POS) tagging
   
    marking words with Parts-of-Speech labels such as noun, verb, adjective, preposition

2. Parsing
   
    Constituency parsers 

    ![](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g222rf6n8kj20qa0jago0.jpg)

    Dependency Parsing 

    ![](http://ww1.sinaimg.cn/mw690/b3beb1ffgy1g222s7sa8rj20p40cmmz3.jpg)

3. Named Entity Recognition (NER)
   
    The task is to find Person (PER), Organization (ORG), Location (LOC) and Geo-Political Entities (GPE)

    2015, NER using Word2Vec features

    2016, CharNER(Character based named entity recognition),cross-lingual NER, LSTM-CRF


4. Named Entity Linking (NEL), Named Entity Disambiguation (NED), Named Entity Normalization (NEN)

    determining the identity of entities 

    2015, Personalized Page Rank

    2016, language independent entity linking (LIEL) system(trained on one language works for number of different languages.)


5. Coreference Resolution (CR)

    determining which noun phrases (including pronouns, proper names and common names) refer to the same entities in documents 

    open-source platforms: BART, Illinois Coreference Package, Stanford CoreNLP

    #### joint models :

    CR- NER (Haghighi and Klein, 2010; Singh et al., 2013)

    CR-NEL (Hajishirzi et al., 2013)

    NER-CR-NEL (Durrett and Klein, 2014) 

    CCR-NEL (Dutta et al., 2015).


6. Temporal Information Extraction (Event Extraction)
   
    identifying information which can be ordered in a temporal order in text

7. Relation Extraction (RE)

    detecting and classifying pre-defined relationships between entities identified
    
    2016, Seq2Seq(reduce the need of annotated data), attention based CNN

8. Knowledge Base Reasoning and Completion, link prediction
   
    determining the relationship between entities
    Knowledge Graph

    2015, Relational machine learning

    (1) statistical relational learning. (2) path ranking methods. (3) embedding-based models


### Information Extraction Tools

1. Public IE tools:
   
   GATE(General Architecture for Text Engineering), OpenNLP (Apache OpenNLP-Java machine learning toolkit for NLP), Stanford NER, GExp, Mallet (Machine learning for language toolkit), Natural Language Toolkit (Suite of Python libraries for NLP).


2. Commercial IE tools:
   
   Altensity, Open Calais, ClaraBridge, SAS Text Analytics, Business Objects, IBM Intelligent Minerand, Lingpipe.

3. Specialized IE tools:
   
   Ariadne Genomics Medscan Reader for biomedical documents, RINX for resumes.


### Current challenges and future research

1. Open Information Extraction (OpenIE)
2. BioIE
3. Business Analytics
4. Text IE in Images and Videos
5. Web Harvesting