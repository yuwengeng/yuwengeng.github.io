## 小程序使用场景：
    1. 同App进行互补，提供同app类似的功能，比app操作更加简洁的轻应用
    2. 用户使用频率不高，但又不得不用的功能软件.
    小程序 => 相当于单页应用app
---
结构：入口文件——>一级页面——>二级页面。。。。

**启动过程：**
　　项目的启动根文件app.js   
        生命周期: onLaunch()只加载一次,有三大功能: 浏览器缓存进行存取数据；用登陆成功的回调；获取用户信息
　　当 app.js 执行结束后，小程序会按照开发者在 app.json 中定义的 pages 的顺序，逐一执行

js：模块化 import '相对路径'
    App()函数不能注册多个 App的生命周期是由微信客户端根据用户操作主动触发控制的 通过getApp()获取
        获取小程序的global 变量：var app = getApp()

　　Page（）页面构造函数，逻辑层通过Page实例（this）的 setData方法传递数据到渲染层setData（）传递数据实际是一个异步的过程，两个线程传输

wxml模板：
    <import src=''/>  // template引入，不能多层传递导入，include可以
　　- include 可以将目标文件中除了 <template/> <wxs/> 外的整个代码引入 相当于是拷贝到 include 位置 //如公共组件抽象到独立文件
    <include src="header.wxml"/>

    - template
        定义:<template name="">
        使用:<template is="" data="{{}}"/>  // 可以灵活传参

    - 自定义组件 （命名:小写字母 - _）
        结构类似一个页面，使用component要在配置文件说明
        - component样式不影响page样式 class样式默认隔离；component不允许使用id 标签 属性选择器
        - data：{}
        - page与component通信:
            properties:{} // 给组件传递数据，从page到组件
            externalClasses:[] //style 定义组件额外class；或者用？：切换style
            methods：{
                this.triggerEvent('发送给page事件的名称',{event.detail},{})
            } // 组件的事件传递给page 

    整个wxml页面，最底层的标签是<page></page> 小程序组件继承全局的部分样式font，color ，pages可以继承所有全局的 // pc为<html></html>
   <block wx:for> 循环代码块，block标签用来包裹循环多个语句，只接受控制属性；比view组件好
        wx:for-item='' 一般在多层嵌套中用来更改item，index变量名称
        wx:key="唯一值属性/*this"  // *this代表item本身
        保留当前的状态;
        提高性能 setData()后不渲染,根据key直接排序

### wxml: html属性拓展【属性：值为data/函数】  公用属性：hidden， data-* 自定义属性(传数据)，
      bind/catch事件='事件处理函数（event）'；
    event对象：{
        type:
        target: 触发事件的源组件
        currentTarget: **有事件绑定**的当前组件  
            data-index属性用法： event.currentTarget.dataset.index //用事件返回
        <!-- 正确获取 dataset 的姿势是使用 currentTarget 的 -->
    }

    text行内元素
        - selectable='{{true}}' 
        - <text decode="{{true}}"> <text> // 解码，开启识别转义字符
    button默认为block元素：
        - size="mini"
        - type="primary/default/warn"
        - plain 镂空
        - hover-class="" 点击样式变化
    view 块级容器
        - hover-stop-propagation="" 是否阻止父标签点击态变化
    image inline-block元素  默认大小320x240px
        - bindload="" 监听图片加载完成
        - lazy-load 
        - wx.chooseImage({}) 调用相册
    scroll-view
        - scroll-x
        - bindscroll
    swiper:轮播容器； swiper-item:轮播项目

    picker——选择器 -->
<!-- 　　　　mode：日期data，时间time，地区regin，自定义range -->

> VueJS中使用v-if控制元素是否渲染，使用v-show控制元素是否显示。微信小程序使用wx:if控制元素是否渲染，使用属性hidden控制元素显示

### wxss样式：
导入外联样式:  @import "common.wxss";
内联样式 框架组件上支持使用 style、class 属性来控制组件的样式：静态的样式应统一写到 class 中独立解析,style文件接收动态的样式在运行时会进行解析，请尽量避免将静态的样式写进 style 中，以免影响渲染速度。

小程序尺寸单位：只有iphone6上:1px = 1rpx   2个物理像素（rpx） = 1px
一般水平方向rpx，垂直方向px   ，混合使用：rpx自适应，px不变
字体大小用px

line-height = font-size消除文字上下空白

wxss:

- 设置全局字体样式app.wxss：
text{
font-family:MicroSoft yahei;
}
- 设置页面全屏样式及背景色：

page{
height:100%;
background:#b3d4db;
}
- 图片居中覆盖:
.audio{
    width:102rpx;
    height:110rpx;
    position: absolute;
    left: 50%;
    margin-left: -51rpx;//经典水平居中方式
    top:180rpx;
    margin-top: 20rpx;
    opacity:0.6;//透明度

### wxs：
在wxml中不能直接调用page/component中定义的函数
   导入： <wxs src="必须相对路径" module=""/>

- 两大核心:事件回调和数据驱动[setData() bind='event']
    - 小程序内，事件的绑定是通过在 WXML 标签增加 `bind*` 属性来实现(catch抓住 会阻止事件继续冒泡) 当事件触发时，处理函数会响应，传入 event 对象，通过 event 对象可以获取事件触发时候的一些信息，包括时间戳、detail 等。
    事件data传递: 因为小程序内的事件绑定都是在 WXML 中实现的，所以传递参数只能通过 WXML 上面的属性值来传递,传递到event对象里
> 事件捕获capture-bind、capture-catch，后者将中断事件流捕获阶段和取消冒泡阶段


云开发调用:
```
wx.cloud.init({
  env: 'tianqi-xxx' # 初始化时，需要传入 env 参数
})
- 云函数-在云端,相当于小程序后端  微信私有协议天然鉴权
- 云调用- 基于云函数免鉴权使用小程序开放接口
- HTTP API 对接第三方服务器

**云数据库**

增删改查:
- db.collection("**").add({
    data: {},
    success(){}
})
- 获取数据
    1. db.collection("**").get().then(res => {})
    2.                    .doc("id").get().then()
    3.                    .where({}).get().then()

- 删除多条数据:
    只能在服务端,云函数

-更新数据:
    1. 局部更新 update()
    2. 整体更新 set()

commend指令: 
    _ = db.commend; 指令操作句柄
    state:_.eq({

    })

### 增强操作- 云函数

先配置云函数根目录

[微信小程序api封装经验](http://www.wxapp-union.com/article-5861-1.html)