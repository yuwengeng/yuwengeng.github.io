---
title: 'hexo使用'
date: 2018-11-26 17:08:58
---
hexo clean   hexo g
hexo s  hexo d #将本地数据部署到远端服务器(如github)  hexo d -g 
hexo generate -d
hexo list <type> # 列出网站资料

### 更新hexo
npm i hexo-cli -g
npm update hexo -g#升级

更新插件：
npm update

  <script type="text/javascript" src="../../source/image.js"></script>  
hexo优化压缩  npm install hexo-all-minifier --save

- 自定义hexo new生成md文件 选项在/scaffolds/post.md文件中添加：

> body{ 必应图片api
      background:url('https://api.uixsj.cn/bing/bing.php');
}


>多行
>>嵌套引用
<!-- more --> 
自动截断

// 隐藏   
<details>
hhhh
</details>


强制换行
在行末使用空格（两个以上） + 换行（Enter）
<br> 换行
<https://api.uixsj.cn/bing/bing.php> 单纯链接   
[]()                                  超链接

` ` :单行代码

表格：
|表头 |     |    |
|-----|:---:|:---|  冒号代表对齐方式

> 任务列表
- [ ] 纯牛奶
- [x] 西瓜
- [ ] 鸡蛋
- [x] 保鲜膜
- [ ] 猪肉（暂时买不起）

<center>中间 </center>

---  分割线可以用三个以上的星号、减号或者底线来标识

[TOC] 目录DD

[TOC] ml



### collab

Colab不仅可以运行Python代码，只要在命令前面加一个"  ！"，这条命令就变成了linux命令，比如我们可以" ! ls"查看文件夹文件，还可以!pip安装库。以及运行py程序!python2 temp.py





