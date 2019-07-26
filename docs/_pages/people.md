---
title: People
permalink: /people/
layout: authors
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/amc-banner.jpg
#   actions:
#     - label: "Download"
#       url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [**buguroo**](https://www.buguroo.com/en/blog/topic/ai)"
excerpt: "AI ML Club Members"
---

## Chairs

| Chairs | Name | Bio |
| ------ | ---- | --- |
{%- for author in site.data.authors %}
  {%- if author[1].membership != 'chair' %}
    {%- continue %}
  {%- endif %}
| ![{{ author[1].name }}]({{ author[1].avatar }}){:height="88px" width="88px"} | [{{ author[1].name }}](/people/{{ author[0] | slugify | downcase }}/) | {{ author[1].bio }} |
{%- endfor %}
|        |      |     |

## Members

| Members | Name | Bio |
| ------- | ---- | --- |
{%- for author in site.data.authors %}
  {%- if author[1].membership != 'member' %}
    {%- continue %}
  {%- endif %}
| ![{{ author[1].name }}]({{ author[1].avatar }}){:height="88px" width="88px"} | [{{ author[1].name }}](/people/{{ author[0] | slugify | downcase }}/) | {{ author[1].bio }} |
{%- endfor %}
|        |      |     |

## Newbies

> Please set `membership` attribute in `_data/author.yml` to level up from _Newbies_.

| Name | Bio |
| ---- | --- |
{%- for author in site.data.authors %}
  {%- if author[1].membership %}
    {%- continue %}
  {%- endif %}
| {{ author[1].name }} | {{ author[1].bio }} |
{%- endfor %}
|        |      |     |

## Nobody

> There's no such name in `_data/author.yml`, please feel free to help yourself adding it.

| Name |
| ---- |
{%- assign authors = site.posts | map: 'author' | uniq %}
{%- for author in authors %}
  {%- if author == nil %}
    {%- continue %}
  {%- endif %}
  {%- if site.data.authors[author] %}
    {%- continue %}
  {%- endif %}
| {{ author }} |
{%- endfor %}
| |
