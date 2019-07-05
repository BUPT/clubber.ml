---
title: "Blog Manual"
permalink: /manuals/blog/
layout: splash
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/AMC-banner.jpg
#   actions:
#     - label: "Download"
#       url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [**buguroo**](https://www.buguroo.com/en/blog/topic/ai)"
excerpt: "AI ML Club"
toc: true
toc_label: "Unique Title"
toc_icon: "heart"  # corresponding Font Awesome icon name (without fa prefix)
---

## Blog Manual

A check list for publish the blog.

### 沙龙博客

地址：<https://ai-ml.club>

大家所做沙龙分享内容，可以通过如下方式上传到我们的博客。

#### 上传地址

<https://github.com/BUPT/ai-ml.club/tree/master/docs/_posts>

#### 添加作者信息

所有作者的基本资料，都保存在这个文件中：<https://github.com/BUPT/ai-ml.club/blob/master/docs/_data/authors.yml>

如果你还不在这个文件中的话，那么将自己添加进去即可，如下格式为例：

```yml
qhduan:
  name        : "段清华"
  bio         : "人工智障工程师"
  avatar      : "https://avatars0.githubusercontent.com/u/3895924?s=460&v=4"
  links:
    - label: "Website"
      icon: "fas fa-fw fa-link"
      url: "http://qhduan.com"
```

其中，最核心的就是第一行的 `qhduan:` 中的 **qhduan** ，这个是你的作者id，在博客中的 `author: qhduan` 中需要引用。

其他内容格式可以参考文件中其他部分。

#### 上传格式

1. 选择论文笔记所属分类（Category），可以参考之前的[分类列表](https://bupt.github.io/ai-ml.club/categories/)
2. 选择论文笔记所带标签（Tag），可以参考之前的[分类列表](https://bupt.github.io/ai-ml.club/tags/)
3. 沙龙活动会议纪要命名格式为：`XXXX-XX-XX-seminar-meeting-minutes-${season}-${episode}.md`。其中`${season}`是沙龙活动第几季；`${episode}`是沙龙活动在本季的活动编号，顺序递增。
4. 论文笔记命名格式为： XXXX-XX-XX-paper-title-in-lower-case.md。"XXXX-XX-XX"为年月日；为了统一规范论文名一律小写。
5. 上传博客文章所需文件（如图片、PDF等），所有文件都必须存放在`docs/assets/${year}/`目录下（${year}是四位数字年份）
6. 所有上传文件，需要符合以下命名规则：
    1. 文件名全部小写，有空格的地方用`-`连接；
    2. 如果是沙龙活动纪要相关文件，则文件名前缀按照`seminar-${season}-${episode}-`命名。其中`${episode}`是沙龙活动的编号
        1. 授蛋仪式照片：`seminar-${season}-${episode}-chairman-appointment.jpg`
        2. 沙龙演讲照片：`seminar-${season}-${episode}-talk-${talker-name}.jpg`。其中`${talker-name}`是演讲人姓名拼音
        3. 合影照片：`seminar-${season}-${episode}-group-photo.jpg`
    3. 其他文件，尽量文件名和Blog Post的文件名一致，便于后续维护工作识别
7. 在添加图片到git之前，运行`make fit-image`将图片尺寸进行调整。

#### Blog Post 文件模板

最好的模板，就是在目录中寻找之前的博客文章 Markdown 源文件，然后拷贝之后做适合自己的修改。

下面介绍一下基本结构：

``` js
---
title: 这里是 Blog 的标题
date: 日期。请按照 "2019-01-06 12:00 +0800" 的格式填写，为了方便可以只修改年月日即可。
author: ${your_github_username}
comments: true
mathjax: true
categories:
  - *
tags:
  - *
  - *
---
```

Example:

```yaml
---
title: 胶囊（Capsule）网络
date: 2019-01-06 12:00 +0800
author: 824zzy
comments: true
mathjax: true
categories:
  - classicial paper
tags:
  - capsule
---
```

#### 发布

对博客的添加修改，可以通过Pull Request的方式提交。Pull Request被Merge之后，在线网站会在几分钟内自动更新。

如有任何疑问，可以联系当任轮值主席或副主席咨询。
