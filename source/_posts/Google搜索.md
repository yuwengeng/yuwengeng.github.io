---
title: 'Google搜索'
date: 2018-11-26 17:08:58
tags:
- '搜索·奇技淫巧'

categories:
- '搜索'
---

搜索引擎使用whoosh，是一个纯python实现的全文搜索引擎，小巧简单

	- **词条垂直搜索整理计划**
	- 
	- PageRank算法: 充分利用入链数量假设和入链质量假设 得到拟合函数进行计算得分, 
	- 
	- 资源算法: 依据资源下载量 和 时间 进行计算得分

### 元搜索引擎
自己没搜索引擎，又想要大规模的数据源，怎么办？可以对百度搜索和谷歌搜索善加利用，以小搏大，站在巨人的肩膀上。有很多的应用场景可以很巧妙地借助百度搜索和谷歌搜索来实现，比如网站的新闻采集，比如技术、品牌的新闻跟踪，比如知识库的收集，比如人机问答系统等，我之前做的一个准确率达百分之九十几的人机问答系统的数据源，其中一部分就是充分利用了百度搜索和谷歌搜索。
[使用Searx搭建一个私人的搜索引擎平台](https://www.moerats.com/archives/875/)
### 元搜索引擎结果合成算法
（https://www.oschina.net/p/searx）

关键词: 
  puppeteer爬虫技巧
  前端可视化
  .....


**notes**
	- 百度搜号码归属地
	- time in NYC   

### 总结：搜索的三个层次

利用搜索框输入关键词
掌握基本逻辑关系组配关键词，以及利用高级检索
利用指令（语法）检索
  仅在标题，内容，URL和/或网站上查找术语链接
习惯英文搜索 阅读，增加另一95%天地

1. 多个关键词逻辑规则  
  ( Google用减号“-”表示逻辑“非”操作,空格表示与逻辑 OR表示或逻辑 ) 
  "严格匹配"  模糊分组匹配
  不区分英文字母大小写
  括号“()”是分组符号

- site选项用于控制搜索结果所属的域名
    "搜索引擎 技巧 site:edu.cn"

- “吉泽明步 intitle:在线 inurl:play OR video”   
- ​intext:(密码 | 验证码 | 系统 | 帐号)
  allintext:* *    搜索站点中是否含相关关键字的网页

- 二进制文档检索 filetype:(pdf|doc|xls|ppt|rtf|all)  zip rar chm
- link:www.newhua.com  //找到更多符合你兴趣的网站
    搜索链接到某个URL的网页  (只能单独使用)
- cache:url   //网页快照 需要默认谷歌搜索
- define:搜索    //名词解释定义查询

- Insubject: 搜索Googlegroup的主题行
- inanchor或allinanchor

- num range：在数字之间加上两个句号并添加度量单位：10..35 斤、300..500 元、2010..2011 年

合集索引目录:
 allintitle:"Index Of" 粉笔 分享 heroku 搭建和使用（实用 小项目）
              gitchat 
              关键词：网页特效源码   成语 podcast

http://fis.io/ajax-google-custom-search-engine.html自定义搜索实现
百度:
  不支持intext  
  (密码 | 验证码 | 系统 | 帐号)


合集博客论坛:
  inurl:blog OR bbs   
  site:blog.sina.com.cn   
  intitle:(blog|论坛|group)
  "site:blogspot.com 前端"    //谷歌博客搜索

合集RSS:
  inurl:rss | feed
  
合集custom google search:
  intext:cse.google.com/cse/publicurl
  inurl:sites.google.com/view

索引垂直领域网站：果壳 知乎 卫计委 协和 湘雅 好大夫 丁香鱼 百科名医

Google自定义搜索引擎网址导航 https://www.cse123.com/%E9%A6%96%E9%A1%B5

gg-罗网：https://cse.google.com/cse?cx=001026332474729733297:elhdjihv5ea
gg-云盘： https://cse.google.com/cse?cx=001026332474729733297:3t2scsclace

Plus：https://cse.google.com/cse?cx=018413290510798844940:k69bxcfofe0

*.Google.com Hack Attack                https://cse.google.com/cse/publicurl?cx=017648920863780530960:lddgpbzqgoi
App Store Custom Search Engine          https://cse.google.com/cse/publicurl?cx=006205189065513216365:aqogom-kfne
Better Chrome Web Store Search Engine   https://cse.google.com/cse/publicurl?cx=006205189065513216365:pn3lumi80ne
Facebook Photo Search Engine            https://cse.google.com/cse/publicurl?cx=013991603413798772546:jyvyp2ppxma

Find Pasted Code                    https://cse.google.com/cse/publicurl?cx=013991603413798772546:nxs552dhq8k

Github with Awesome-List Search Engine  https://cse.google.com/cse/publicurl?cx=017261104271573007538:fqn_jyftcdq
Google CSE Finder                       https://cse.google.com/cse/publicurl?cx=011081986282915606282:fa52ldjw5to
Google Docs CSE                         https://cse.google.com/cse/publicurl?cx=013991603413798772546:rse-4irjrn8#gsc.tab=0
Google Domain Hacker                    https://cse.google.com/cse/publicurl?cx=005797772976587943970:ca2hiy6hmri
Google Drive Folder Search Engine       https://cse.google.com/cse/publicurl?cx=013991603413798772546:nwzqlcysx_w
Google Maps Search Engine               https://cse.google.com/cse?cx=013991603413798772546:mofb1uoaebi
Google+ Photos Search Engine            https://cse.google.com/cse/publicurl?cx=006205189065513216365:uo99tr1fxjq
Instagram Deep Photo Search             https://cse.google.com/cse/publicurl?cx=017261104271573007538:ffk_jpt64gy
Mailing List Archives Search Engine     https://cse.google.com/cse/publicurl?cx=013991603413798772546:sipriovnbxq
Robots.txt, XML & Sitemap Search        https://cse.google.com/cse?cx=013991603413798772546:zu7epjqvunu
SEARCH BY FILETYPE                      https://cse.google.com/cse/publicurl?cx=013991603413798772546:mu-oio3a980
SEO Resources Search Engine             https://cse.google.com/cse/publicurl?cx=005797772976587943970:i7q6z1kjm1w
Short URL Search Engine                 https://cse.google.com/cse/publicurl?cx=017261104271573007538:magh-vr6t6g
Super OSINT Search Engine               https://cse.google.com/cse/publicurl?cx=006290531980334157382:qcaf4enph7i
The Photo Album Finder                  https://cse.google.com/cse/publicurl?cx=013991603413798772546:bldnx392j6u
The Search Engine Finder                https://cse.google.com/cse?cx=016621447308871563343:nyvaorurd5l
TIKTOK Search Engine                    https://cse.google.com/cse?cx=011444696387487602669:aqf7d9w73om
Tweet Archive Hacker                    https://cse.google.com/cse/publicurl?cx=005797772976587943970:kffjgylvzwu

Twitter List Finder                     https://cse.google.com/cse/publicurl?cx=016621447308871563343:u4r_fupvs-e
Twitter Photo Search Engine             https://cse.google.com/cse/publicurl?cx=006290531980334157382:_ltcjq0robu

Webcam Custom Search Engine             https://cse.google.com/cse/publicurl?cx=013991603413798772546:gjcdtyiytey
Wikispaces Search Engine                https://cse.google.com/cse/publicurl?cx=005797772976587943970:afbre9pr2ly
WordPress Content Snatcher              https://cse.google.com/cse/publicurl?cx=011081986282915606282:w8bndhohpi0
































## 什么是IPFS： 
InterPlanetary File System ，缩写 IPFS，旨在创建持久且分布式存储和共享文件的网络传输协议，它是一种内容可寻址的对等超媒体分发协议。在IPFS网络中的节点将构成一个分布式文件系统。

原理用基于内容的地址替代基于域名的地址，也就是用户寻找的不是某个地址而是储存在某个地方的内容，不需要验证发送者的身份，而只需要验证内容的哈希，IPFS是点对点的超媒体协议，可以让网络更快、更安全、更开放。它是一个面向全球的、点对点的分布式版本文件系统。数据在IPFS上的存储都是以碎片的形式存储的，每个碎片的大小是256k，（最后的一个碎片如果不够256k，或文件整体大小小于256kb，将直接作为碎片处理，不再占用新的block）。网络中的节点会对你的碎片进行存储。当你检索数据时，会将所有碎片收集起来，通过文件管理系统按序组合碎片得到你的文件。
[https://kongyixueyuan.com/witbook/24/447]

### GitHub Actions (云端自动化流)

> Github Action 提供的虚拟环境： 2core CPU · 7 GB RAM 内存 · 14 GB SSD 硬盘空间

使用限制：

  每个仓库只能同时支持20个 workflow 并行。
  每小时可以调用1000次 GitHub API 。
  每个 job 最多可以执行6个小时。
  免费版的用户最大支持20个 job 并发执行，macOS 最大只支持5个。
  私有仓库每月累计使用时间为2000分钟，超过后$ 0.008/分钟，公共仓库则无限制。

教程:
(http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.htm)
(https://mp.weixin.qq.com/s/ybiLN1IbyyeEOefp5WGrEg)

持续集成由很多操作组成，比如抓取代码、运行测试、登录远程服务器，发布到第三方服务等等。GitHub 把这些操作就称为 actions。
  [actions官方市场](https://github.com/marketplace?type=actions)
  (https://github.com/sdras/awesome-actions)

```yaml
name: Build and Deploy
on: [push]  #触发 workflow 的事件数组  除了代码库事件也支持外部事件触发，或者定时运行(https://help.github.com/en/articles/events-that-trigger-workflows)。
  <!-- 设置定时运行计划，在周一到周五的 02:00 国际标准时间，等于北京时间减去 8 个小时 -->
  minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12 or JAN-DEC)
│ │ │ │ ┌───────────── day of the week (0 - 6 or SUN-SAT)
  schedule:
  - cron: 0 2 * * 1-5
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest #运行所需要的虚拟机环境
    steps:
    - name: Checkout
      uses: actions/checkout@v1.1.0
      with:
        submodules: recursive
    - name: Build and Deploy
      uses: renzhaosy/hexo-deploy-action@master
      env:  #action所需的环境变量配置
        PERSONAL_TOKEN: ${{ secrets.GH_TOKEN }}
        PUBLISH_REPOSITORY: dev4mobile/dev4mobile.github.io 
          # The repository the action should deploy to.
        BRANCH: master 
          # The branch the action should deploy to.
        PUBLISH_DIR: ./public # The folder the action should deploy.
```
``` 发送邮件的 action
- name: 'Send mail'
  uses: dawidd6/action-send-mail@master
  with:
    server_address: smtp.163.com
    server_port: 465
    username: ${{ secrets.MAIL_USERNAME }}
    password: ${{ secrets.MAIL_PASSWORD }}
    subject: CSDN Report
    body: file://email.txt
    to: shenkebug@qq.com
    from: GitHub Actions
    content_type: text/plain
```