---
title: 'Google搜索'
date: 2018-11-26 17:08:58
tags:
- '搜索·奇技淫巧'

categories:
- '搜索'
---

搜索引擎使用whoosh，是一个纯python实现的全文搜索引擎，小巧简单

### 元搜索引擎
自己没搜索引擎，又想要大规模的数据源，怎么办？可以对百度搜索和谷歌搜索善加利用，以小搏大，站在巨人的肩膀上。有很多的应用场景可以很巧妙地借助百度搜索和谷歌搜索来实现，比如网站的新闻采集，比如技术、品牌的新闻跟踪，比如知识库的收集，比如人机问答系统等，我之前做的一个准确率达百分之九十几的人机问答系统的数据源，其中一部分就是充分利用了百度搜索和谷歌搜索。
[使用Searx搭建一个私人的搜索引擎平台](https://www.moerats.com/archives/875/)
### 元搜索引擎结果合成算法

（https://www.oschina.net/p/searx）

[一个便捷的 V2EX 站内搜索引擎](https://github.com/Bynil/sov2ex)

**生活经验**
- 百度搜号码归属地
- time in NYC   

总结：搜索的三个层次
利用搜索框输入关键词
掌握基本逻辑关系组配关键词，以及利用高级检索
利用指令（语法）检索

1. 多个关键词   ( Google用减号“-”表示逻辑“非”操作,空格表示与逻辑 OR或 ) ( 用短语句子做关键字，必须加英文引号，否则空格会被当作“与”操作符 )

- site选项用于控制搜索结果所属的域名
    "搜索引擎 技巧 site:edu.cn"
    site:blogspot.com 前端    谷歌博客搜索

- “吉泽明步 intitle:在线 inurl:play”    => 限制关键词包含在 网页title 和限定url链接

- 二进制文档 进行检索
    *** filetype:pdf   // doc，xls，ppt，rtf，all
    简历.pdf

- link:www.newhua.com  //找到更多符合你兴趣的网站
    搜索链接到某个URL的网页  (只能单独使用)

- cache:url   //查看失效的网页历史 需要默认谷歌搜索
- define:搜索    //名词解释

## 什么是IPFS： 
InterPlanetary File System ，缩写 IPFS，旨在创建持久且分布式存储和共享文件的网络传输协议，它是一种内容可寻址的对等超媒体分发协议。在IPFS网络中的节点将构成一个分布式文件系统。

原理用基于内容的地址替代基于域名的地址，也就是用户寻找的不是某个地址而是储存在某个地方的内容，不需要验证发送者的身份，而只需要验证内容的哈希，IPFS是点对点的超媒体协议，可以让网络更快、更安全、更开放。它是一个面向全球的、点对点的分布式版本文件系统。数据在IPFS上的存储都是以碎片的形式存储的，每个碎片的大小是256k，（最后的一个碎片如果不够256k，或文件整体大小小于256kb，将直接作为碎片处理，不再占用新的block）。网络中的节点会对你的碎片进行存储。当你检索数据时，会将所有碎片收集起来，通过文件管理系统按序组合碎片得到你的文件。
[https://kongyixueyuan.com/witbook/24/447]

### GitHub Actions (云端自动化流)

(http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.htm)
持续集成由很多操作组成，比如抓取代码、运行测试、登录远程服务器，发布到第三方服务等等。GitHub 把这些操作就称为 actions。
[actions官方市场](https://github.com/marketplace?type=actions)
(https://github.com/sdras/awesome-actions)
```yaml
name: Build and Deploy
on: [push]  #触发 workflow 的事件数组  除了代码库事件，GitHub Actions 也支持外部事件触发，或者定时运行(https://help.github.com/en/articles/events-that-trigger-workflows)。
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
      env:  #该步骤所需的环境变量配置
        PERSONAL_TOKEN: ${{ secrets.GH_TOKEN }}
        PUBLISH_REPOSITORY: dev4mobile/dev4mobile.github.io # The repository the action should deploy to.
        BRANCH: master # The branch the action should deploy to.
        PUBLISH_DIR: ./public # The folder the action should deploy.
```