---
title: People
permalink: /people/
layout: splash
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
| ![{{ author[1].name }}]({{ author[1].avatar }}){:height="88px" width="88px"} | [{{ author[1].name }}](/people/{{ author[0] }}/) | {{ author[1].bio }} |
{%- endfor %}
|        |      |     |

## Members

| Members | Name | Bio |
| ------- | ---- | --- |
{%- for author in site.data.authors %}
  {%- if author[1].membership != 'member' %}
    {%- continue %}
  {%- endif %}
| ![{{ author[1].name }}]({{ author[1].avatar }}){:height="88px" width="88px"} | [{{ author[1].name }}](/people/{{ author[0] }}/) | {{ author[1].bio }} |
{%- endfor %}
|        |      |     |

## Newbies

| Name | Bio |
| ---- | --- |
{%- for author in site.data.authors %}
  {%- if author[1].membership %}
    {%- continue %}
  {%- endif %}
| {{ author[1].name }} | {{ author[1].bio }} |
{%- endfor %}
|        |      |     |
