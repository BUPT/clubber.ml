---
title: "Pull Request Manual"
permalink: /manuals/pull-request/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/conversational-ai.jpg
#   actions:
#     - label: "Download"
#       url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [**boost.ai**](https://www.boost.ai/articles/2018/10/17/six-ways-conversational-ai-will-enhance-your-company)"
excerpt: "How to send Pull Request"
toc: true
toc_label: "Pull Request Manual"
toc_icon: "tasks"  # corresponding Font Awesome icon name (without fa prefix)
---

## Pull Request Check List

参加 AMC 沙龙需要提交 Pull Request。

在 <https://github.com/BUPT/ai-ml.club/blob/master/docs/_pages/papers.md> 项目中，以 Pull Request 的形式，将自己想讲解的论文进行修订。

注意：请在各自的 Pull Request 的描述中，引用本会议纪要的 issue URL，以便于会议纪要进行追踪。

轮值主席在收到大家的PR后，在会议通知发送之前进行Merge。

注意：

1. 在各自的 Pull Request 的描述中，**引用本会议纪要的 issue URL**，以便于会议纪要进行追踪。
1. 在 Pull Request 中，说明自己是属于 Oral 还是 Poster.
1. Pull Request 需要至少一个人 review approve 之后，才能 merge
1. Pull Request 需要通过 CI (Continous Integration) testing 之后，才能被 merge
1. CI 对文件名的要求：`/$[a-z0-9\-\.]+$/` 注意我们统一用 - 而不用 _
1. CI 对图片的要求：尺寸不能超过1MB；同时如果宽度超过了 1920 ，那么需要用 `./scripts/fit-image.sh` 处理一下，压缩到 1920 宽度的分辨率，以加快网页加载速度
1. Pull Request 如果是 Oral 或者 Poster 的报名，那么必需要以 `/^(🗣|📰)/` 开头，请大家注意标题要符合模板

有任何问题，大家可以随时在群里面提出讨论。

## Contributing

1. Fork it
1. Create your paper branch (git checkout -b my-new-paper)
1. Commit your changes (git commit -am 'Added some paper')
1. Push to the branch (git push origin my-new-paper)
1. Create a new Pull Request
