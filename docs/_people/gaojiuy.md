---
layout: author
title: "Jiuyi Gao"
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/amc-banner.jpg
  caption: Photo credit [**buguroo**](<"https://www.buguroo.com/en/blog/topic/ai">)
excerpt: "CNN Visualization"
author: gaojiuy
toc: true
toc_sticky: true
toc_label: "Author Profile"
toc_icon: "address-card"  # corresponding Font Awesome icon name (without fa prefix)

---

Gao is a first year Master student at BUPT, major in Management Science and Engineering, CNN Visualizaiton.

## Talks

- [S2E19 Learning Deep Features for Discriminative Localization](<"https://ai-ml.club/events/seminar-meeting-minutes-2-19/">)
- [S2E18 On PixelWise Explanations for NonLinear Classifier Decisions by Layer-Wise Relevance Propagation](<"https://ai-ml.club/events/seminar-meeting-minutes-2-18/">)

## Attribution Method

There are many methods to explain the predictions of DNNs,and I focus on the problem of assigning an *attribution* value, sometimes also called "relevance" or "contribution", to each input feature of a network.

More formally, consider a DNN that takes an **input** x = [$x_1$, ..., $x_N$] ∈ $R^N$ and produces an **output** S(x) = [$S_1(x)$, ..., $S_C(x)$],
where C is the total number of output neurons.

Given a specific target neuron c, the goal of an attribution method is to determine the **contribution**
$R_c$ = [$R_1^c$, ..., $R_N^c$] ∈ $R^N$ of each input feature $x_i$ to the output $S_c$.

For a **classification task**, the target neuron of interest is usually the output neuron associated with the correct class for a given sample. When the attributions of all input features are arranged together to have the same shape of the input sample which are called attribution maps.

The attribution maps are usually displayed as heatmaps where red color indicates features that contribute **positively** to the activation of the target output, and blue color indicates features that have a **suppressing** effect on it.

## Contact

- Github: <https://github.com/gaojiuy>
- Email: <jiuyigao@163.com>
