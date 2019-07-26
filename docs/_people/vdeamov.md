---
title: "Vincent Duan (段嘉铭)"
layout: author
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/amc-banner.jpg
#   actions:
#     - label: "Download"
#       url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [**buguroo**](https://www.buguroo.com/en/blog/topic/ai)"
excerpt: "Computer Vision"
author: VDeamoV
toc: true
toc_sticky: true
toc_label: "Author Profile"
toc_icon: "address-card"  # corresponding Font Awesome icon name (without fa prefix)
---

Duan is a first year Master student at BUPT, major in Computer Vision, Few Shot Learning, GAN

## Open Source Projects

- Few-shot-Playground - PyTorch's few-shot method implementated for the latest method. (under construction)

## Talks

- [S2E19 Finding Task-Relevant Features for Few-Shot Learning by Category Traversal](https://ai-ml.club/events/seminar-meeting-minutes-2-19/)
- [S2E15 Progressive Pose Attention Transfer for Person Image Generation](https://ai-ml.club/events/seminar-meeting-minutes-2-15/)
- [S2E13 TADAM: Task dependent adaptive metric for improved few-shot learning](https://ai-ml.club/events/seminar-meeting-minutes-2-13/)
- [S2E09 Histograms of Oriented Gradients for Human Detection](https://ai-ml.club/events/seminar-meeting-minutes-2-9/)
- [S2E07 Low-shot Learning via Covariance Preserving Adversarial Augmentation Networks](https://ai-ml.club/events/seminar-meeting-minutes-2-7/)
- [S2E05 Learning to Compare: Relation Network for Few-Shot Learning](https://ai-ml.club/events/seminar-meeting-minutes-2-5/)
- [S2E02 Travelgan-Image-to-Image-Translation-by-Transformation-Vector-Learning](https://ai-ml.club/events/seminar-meeting-minutes-2-2/)

## QA for Few-Shot

1. I am new for few-shot, can u briefly describe how do few-shot model works and why it is few-shot despite it trained by a large dataset?
This question is a very interesting, however very fundamentral question. In general, differ from traditional image-classification model, few-shot model learn the ability to generalize how to classifiy between the classes, so they can correctly classify the unseen classes with a few samples.
More details you can see in one of my blogs [here](https://vdeamov.github.io/fewshotlearning/2019/03/26/few_shot_summery_01/).

2. SOTA data?
Most method are compare on the mini-imagenet, Prototypical Network, Relation Network these classic method **with 4 layer of simple Conv** can achieve about 65 ~ 68% Top1 acc.
Recent years, lots of new work change the backbone to **Resnet 34** and Prototypical Network can achieve 74% with ResNet34. This must be emphasis, because many papers didn't mention it, so they will lead to some mis-understand, such as GNN or some novel method improved 10 per or even 15 per acc.

## Contact

- Linkedin: <https://www.linkedin.com/in/jaming-d-204041116/>
- Github: <https://github.com/vdeamov>
- Email: <vincent.duan95@gmail.com>
- Blog: <https://vdeamov.github.io>
