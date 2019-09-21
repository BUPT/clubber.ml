![AMC - AI ML Club Logo](https://ai-ml.club/assets/images/amc-logo.png)

[![Colab Notebook](https://img.shields.io/badge/Google_Colab-Notebook-brightgreen.svg)](https://colab.research.google.com/drive/1AO3bwIgzfy63ty8OSSgUPRG1PIii3oo_)
[![BUPT CAD Project](https://img.shields.io/badge/👀-BUPT_CAD_Project-blue.svg)](https://github.com/bupt/awesome-cad)
[![Build Status](https://travis-ci.com/BUPT/ai-ml.club.svg?branch=master)](https://travis-ci.com/BUPT/ai-ml.club)

Welcome to Artificial Intelligence & Machine Learning CLUB!

Here are all of friends for Code, Paper, and Beers! 🍻

We have weekly offline meetups, you will be welcome to join if you are interested.

- Paper Index: <https://ai-ml.club/papers>
- Meetup Announcements & Minutes: <https://ai-ml.club/categories/#events>
- Join Us 💖 by reading the **Newcomer Manual**: <https://ai-ml.club/manuals/newcomer/>

![paper oral](https://bupt.github.io/conversational-ai-club/images/paper-oral-screen.jpg)
> [第十一次沙龙：朱正源Oral](https://github.com/BUPT/ai-ml.club/issues/28)

![paper poster](https://bupt.github.io/conversational-ai-club/images/paper-poster-board.jpg)
> [第十二次沙龙：李童俊Poster](https://github.com/BUPT/ai-ml.club/issues/31)

![group photo](https://bupt.github.io/conversational-ai-club/images/group-photo.jpg)
> [第七次沙龙：会员合影](https://github.com/BUPT/ai-ml.club/issues/16)

![group photo - 1st year annual](https://user-images.githubusercontent.com/12370338/50087797-24c9a980-023c-11e9-9d3f-05a7fcf4689f.jpeg)
> [第十九次沙龙：第一界年会](https://github.com/BUPT/ai-ml.club/issues/44)

![group photo - laker beer](docs/assets/2019/seminar-2-10-group-photo-beer.jpg)
> [第二季第10次俱乐部 After Party: Beers at Lakers Bar](https://ai-ml.club/events/seminar-meeting-minutes-2-10/)

## TOOLS

- [GitXiv — Collaborative Open Computer Science](http://www.gitxiv.com) - arXiv + Github + Links + Discussion
- [Web interface for browsing, search and filtering recent arxiv submissions](http://www.arxiv-sanity.com/library)

## Development

We are using [GitHub Pages](https://pages.github.com/) to host our blog, powered by [Jekyll] with the nice and flexible two-column Jekyll theme [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/).

### Git

We are using Github LFS (Large File Storage) to store `docs/assets/**/*`.

Here's a good start for learning how to use LFS: [Git LFS Tutorial](https://github.com/git-lfs/git-lfs/wiki/Tutorial)

If you want to check out the repository fast, use the following command to `clone`:

```shell
GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:BUPT/ai-ml.club.git
```

Learn more about `GIT_LFS_SKIP_SMUDGE` from [here](https://stackoverflow.com/a/42021818/1123955)

### Install

```sh
# Setup ruby environment first
sudo apt install ruby
sudo gem install bundle

# Install the blog requirements
make install

# Install the NPM dependencies
npm install
```

### Serve

```sh
make serve
```

### Local Test

```sh
npm test
# If ERROR occurs please check out
# 1. node version >= 10
# 2. you have installed the lastest typescript
```

### Image Resizing

```sh
# Mac
brew install imagemagick

# Linux
apt install imagemagick

./scripts/fit-image.sh
```

> Or you can use your local picture resize tools to make the file size lower than 200kb.
> The 1920 * 1080 with 8 bit sRGB is prefered.
> Also, aware the rules just under this content. The teasor image size should be right of 500 * 300. Resize it before your uploading.

### VsCode Markdown Linting

```shell
code --install-extension DavidAnson.vscode-markdownlint
```

Learn more from <https://github.com/DavidAnson/vscode-markdownlint>

### Rules

1. Attachments & Image files: all files need to be saved under the folder `docs/assets/2019/` (2019 is the current year), and you can expect the url of your file is under the url `https://ai-ml.club/assets/2019/`
1. Author Information: all the author information is saved in the file `docs/_data/author.yml`, please free free to add & modify it by yourself. See: <https://mmistakes.github.io/minimal-mistakes/docs/authors/>
1. Add a teasor image with size 500x300 to your post by add the following `YAML Front Matter` to your post:

    ```yaml
    header:
      teaser: /assets/2019/my-awesome-post-teaser-500x300.jpg
    ```

## Super Chairs

- Corresponding Chair （通讯主席）: [Meina SONG (宋美娜)](https://baike.baidu.com/item/%E5%AE%8B%E7%BE%8E%E5%A8%9C/4444673) Ph.D, Professor, School of Computer Science, BUPT
- Academic Chair （学术主席）: [Da XIAO (肖达)](https://scss.bupt.edu.cn/info/1063/1162.htm)，博士毕业于清华大学计算机科学与技术系，现为北京邮电大学网络空间安全学院讲师，彩云科技首席科学家，集智俱乐部核心成员。目前研究兴趣包括深度学习、人工智能、认知科学。曾在集智俱乐部发起并主持“脑与Deep Learning读书会”、“高级认知Deep Learning读书会”等线下活动。
- Industry Chair (产业主席）: [Xin HE (贺新)](https://ai-ml.club/people/newip/)，曾工作于千寻位置网络科技有限公司，阿里巴巴（中国），惠普，上海贝尔阿尔卡特等公司。曾任职项目经理、部门经理、资深经理、千寻位置网副总经理。负责过通信OSS研发、High Tech行业应用研发、YunOS系统框架研发、汽车行业经销商业务系统研发等。对软件研发与管理都有深入实战经验。其中DBS项目软件项目通过CMMI5级认证，千寻位置网的北斗魔盒项目获得智能终端墨菲斯奖。

## CO-FOUNDERS

- [Huan LI (李卓桓)](https://ai-ml.club/people/huan/), CS Ph.D, BUPT
- [Zhengyuan ZHU (朱正源)](https://ai-ml.club/people/824zzy/), Master, BUPT

## Contributors

[![Open Collective Backers](https://opencollective.com/ai-ml-club/backer/badge.svg?label=open%20collective%20backers&color=blue)](https://opencollective.com/ai-ml-club/)
[![Open Collective Sponsors](https://opencollective.com/ai-ml-club/sponsors/badge.svg?label=open%20collective%20sponsors&color=blue)](https://opencollective.com/ai-ml-club/)

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].
<a href="https://github.com/BUPT/ai-ml.club/graphs/contributors"><img src="https://opencollective.com/ai-ml-club/contributors.svg?width=890&button=false" /></a>

## Backers

[![Backers on Open Collective](https://opencollective.com/ai-ml-club/backers/badge.svg)](#backers)

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/ai-ml-club#backer)]

<a href="https://opencollective.com/ai-ml-club#backers" target="_blank"><img src="https://opencollective.com/ai-ml-club/backers.svg?width=890"></a>

## Sponsors

[![BUPT CAD Project](https://img.shields.io/badge/👀-BUPT_CAD_Project-blue.svg)](https://github.com/bupt/awesome-cad)
[![Sponsors on Open Collective](https://opencollective.com/ai-ml-club/sponsors/badge.svg)](#sponsors)

The AI ML CLUB are sponsored by the professor [Meina Song](https://github.com/HoneyCatty) who's in charge of [CAD Center](https://github.com/bupt/cad) from [BUPT](https://github.com/bupt/) CS department. We really appreciate for letting us to use the great 821 meeting room in every sunday evening because it's very convenience for the members come from BUPT.

> “CAD欢迎大家，很荣幸能成为大家办活动的场地，也很高兴能跟各位才俊在一个社群。任何需要，联系我们。”  
> － [Meina SONG](https://github.com/HoneyCatty), professor of CAD Center, BUPT. [link](https://github.com/BUPT/ai-ml.club/issues/93#issuecomment-487449444)

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/ai-ml-club#sponsor)]

<a href="https://opencollective.com/ai-ml-club/sponsor/0/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/1/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/2/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/3/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/4/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/5/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/6/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/7/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/8/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/ai-ml-club/sponsor/9/website" target="_blank"><img src="https://opencollective.com/ai-ml-club/sponsor/9/avatar.svg"></a>

## COPYRIGHT & LICENSE

- Code & Docs © 2018-2019 Contributors
- Code released under the Apache-2.0 License
- Docs released under Creative Commons
