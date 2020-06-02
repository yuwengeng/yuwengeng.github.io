---
title: 'javascript笔记'
date: 2018-11-26 17:08:58
tags:
- 'js'
- '前端'

categories:
- 'js'
---

JavaScript是世界上最流行的脚本语言，因为你在电脑、手机、平板上浏览的所有的网页，以及无数基于HTML5的手机App，交互逻辑都是由JavaScript驱动的。

字典：《权威指南》《高级程序设计》

js 运行三部曲：1 语法分析 → 2 预编译 → 3 解释执行

变量名可以包括英文字母、_、$、数字

多变量声明：
    var a,
        b,
        c;
内存堆栈：重新赋值不会覆盖，会新开辟空间

imply global 暗示全局变量：即任何变量，如果变量未经声明就赋值，此变量就为全局对象(window)所有。
　　函数内赋值也不例外
function test () {
      var a = b = 3;  // b为全局变量
}
　　

　　switch case语句会执行case语句不严格，需要break停止 ：用处：多个确定值判断

<!-- more -->

字符编码：

　　ASCII字符以\x##形式的十六进制表示 用\u####表示一个Unicode字符

2 / 0; // Infinity
0 / 0; // NaN

唯一能判断NaN的方法是通过isNaN()函数
要比较两个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值：
Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; // true
自动类型转换：

　　任何数据类型加字符串都等于字符串

例 var a = 1 + “a” + 1 + 1; //打印 1a11
例 var a = 1 + 1 + “a” + 1 + 1; //打印 2a11，从左向右运算
例 var a = 1 + 1 + “a” +( 1 + 2); //打印 2a3
　　很多实践中推荐禁止使用“ ==”，而要求程序员进行显式地类型转换后，用 === 比较。

==比较，它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果；

===比较，它不会自动转换数据类型，先判断数据类型。

+= 累加 ， *= 幂乘：阶乘：mul*=i , 2次幂乘：mul*=2

js独创自动类型转换：方便计算

js类型识别：
　　typeof（） 可以识别标准类型，其他都是object，function共6种； typeof（var）=> undefined

　　Object.prototype.toString 识别内置对象类型

null 是 JavaScript 关键字（变量），undefined不是关键字，是数据类型(字符串)

Number类型：


Javascript 只有一种数字类型(即 64位 IEEE 754 双精度浮点 double)。
    // double 有 52 位表示尾数，足以精确存储大到 9✕10¹⁵ 的整数。
非整数的Number类型无法用 ==（===也不行） 来比较，0.1+0.2不能=0.3
正确的比较方法是使用JavaScript提供的最小精度值：

  console.log( Math.abs(0.1 + 0.2 - 0.3) <= Number.EPSILON);
例 var a = 0 / 0； //答案是 NaN，应该得出一个数字类型的数，但是没法表达，
就用 NaN (NaN 是 Not a Number，不是数，但是是数字类型
例 var a = 1 / 0; //是 infinity
例 var a = -1 / 0; /是-infinity
JavaScript中有 +0 和 -0，在加法类运算中它们没有区别，但是除法的场合则需要特别留意区分，“忘记检测除以-0，而得到负无穷大”的情况经常会导致错误，而区分 +0 和 -0 的方式，正是检测 1/x 是 Infinity 还是 -Infinity。



 堆栈空间分配区别：

　　1、栈（操作系统）：由操作系统自动分配释放 ，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈；
　　2、堆（操作系统）： 存储复杂类型(对象)，一般由程序员分配释放， 若程序员不释放，由垃圾回收机制回收，分配方式类似于链表。
- 注意：JavaScript中没有堆和栈的概念，此处我们用堆和栈来讲解，目的方便理解和方便以后的学习。

String：

字符串的最大长度，实际上是受字符串的编码长度影响的。

　　多行字符串：`  `     模板字符串： ${ 变量}

　　常用方法：toUpperCase() toLowerCase() indexOf() subString()

 复制字符串：document.write('jspang|'.repeat(3));

json 转数组：  Array.from（）用于将对象转为真正的数组。
　　arr=Array.from(json);
Array.of()方法：把一堆文本或者变量转换成数组
   字符串与数组转换：

 　　string.split(separator,limit)    默认的是加个 [] ；   str.split('') 分隔每个元素

　　 arr.join()  把arr每个元素转换为str，再连接   //  默认逗号连接　（如果Array的元素不是字符串，将自动转换为字符串后再连接）

 　　arr.toString()：元素用逗号隔开

　　

数组可以包括任意数据类型. Array也是对象　方法：indexOf（） push（）sort()排序  删：pop（） unshift()shift()

 slice()切片:该方法并不会修改数组，而是返回一个子数组。
 concat()方法可以接收任意个元素和Array 返回了一个新的Array
 改：reverse() 会改变原来的数组，而不会创建新的数组。　
 splice()方法是修改Array的“万能方法”，用于插入、删除或替换数组的元素 // 它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素，返回删除的元素。

　　　　array.splice(index,howmany,item1,.....,itemX)  // 未规定howmany，则删除从 index 开始到原数组结尾的所有元素。

注意：和concat()不同，splice并不将他插入的参数展开。也就是如果插入一个数组，他就是插入数组本身，还不是数组的元素。
而concat()插入数组的话，就会把数组展开，插入数组中的元素，不过当插入的数组里
还有数组的时候，就不会展开了。

直接给Array的length赋一个新的值会导致Array大小的变化：

　通过索引赋值时，索引超过了范围，同样会引起Array大小的变化：

var arr = [1, 2, 3];
arr[5] = 'x';
arr; // arr变为[1, 2, 3, undefined, undefined, 'x']
var a = [1,2,3];
delete a[1];  //  a = [1,empty,3]
a.length;  // 3
　　

　es6新增数据类型: symbol 全局标记声明，它是一切非字符串的对象key的集合，js key可以是字符串或者 Symbol类型

声明方式：使用全局Symbol（）函数



JavaScript 语言设计上试图模糊对象和基本类型之间的关系，我们日常代码可以把对象的方法在基本类型上使用（. 运算符提供了装箱操作，它会根据基础类型构造一个临时对象，使得我们能在基础类型上调用对应对象的方法）  js中基本类型与对象不同，各自独立

 Objects：



宿主对象（host Objects）：由JavaScript宿主环境提供的对象，它们的行为完全由宿主环境决定。

内置对象（Built-in Objects）：由JavaScript语言提供的对象。

　　固有对象（Intrinsic Objects ）：由标准规定，随着JavaScript运行时创建而自动创建的对象实例。
　　原生对象（Native Objects）：可以由用户通过Array、RegExp等内置构造器或者特殊语法创建的对象。
　　普通对象（Ordinary Objects）：由{}语法、Object构造器或者class关键字定义类创建的对象，它能够被原型继承。


键都是字符串类型，可以不加引号 值可以是任意数据类型 。 属性名尽量使用标准的变量名，用[ ]访问带有特殊符号的属性必须加引号

对象：无序集合。  数组：有序集合

　　要判断一个属性是否是xiaoming自身拥有的，而不是继承得到的，可以用hasOwnProperty()方法：

var xiaoming = {
    name: '小明'
};
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false
　　for ... in循环，把一个对象的所有属性依次循环出来：

　　要过滤掉对象继承的属性，用hasOwnProperty()来实现：

var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    if (o.hasOwnProperty(key)) {
        console.log(key); // 'name', 'age', 'city'
    }
}
Map:

　　初始化Map需要一个二维数组，或者直接初始化一个空Map。Map具有以下方法：

var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
Set: add() delete()

iterable：Array、Map和Set都属于iterable类型。

　遍历：for ···· of 遍历iterable类型，只循环集合本身的元素

　　 使用iterable内置的forEach方法，它接收一个函数，每次迭代就自动回调该函数。以Array为例：

'use strict';
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) { // element: 指向当前元素的值 // index: 指向当前索引 // array: 指向Array对象本身 console.log(element + ', index = ' + index); });



函数：

函数定义：命名函数表达式，匿名函数表达式
参数: 　
js天生不定参，　函数的实参也可以是任意的数据类型.  JavaScript允许传入任意个参数而不影响调用.  python参数不可以。

(函数中用的严格模式，参数不能用默认值；)

 函数的参数如果特别多的话，可以使用 arguments实参列表 实参列表出生时有几个就有几个 但arguments值与形参相互映射  获取函数实参：rest参数只能写在最后，前面用...标识

获得形参个数：(fun.length)

 js默认return返回undefined类型 Python默认None   js中 null应用场景： 表示对象不存在

作用域：

一般局部变量退出作用域之后会销毁，（但是内部的函数被保存到外部，生成闭包，依旧继承着上级作用域 ）全局变量关闭网页或浏览器才会销毁

作用域链[[scope ]] :隐式属性： 由外到内一级级继承GO， AO对象

 闭包:

　　内部的嵌套函数被保存到外部，生成闭包，依旧继承着上级作用域
函数定义内容在预编译之后才执行：函数定义不会对变量有影响，只是占用了空间

arr[i] = function (){
console.log(i);  // 变量i不会相互影响
}
　　

预编译：

没有函数嵌套：考虑全局预编译，（全局预编译 全局变量，函数挂载到GO对象）

function add (n){
   return n+1;
}
function add (n){
   return n+3;
}  // 函数名称相同则覆盖　　
再函数预编译（先提升变量声明，再提升内部function整体；再执行函数体【先看自己的 AO再看全局的 GO】）

（函数）预编译的四部曲：  预编译发生在函数执行的前一刻

1.创建 AO 对象 Activation Object(执行期上下文)，每一次执行都重新产生AO

2.找形参和变量声明，将变量和形参名作为 AO 属性名，值为 undefined

AO{

a : undefined,

b : undefined }

3.把实参值传到形参里

4.找函数声明，其函数体赋予给值，函数名为属性 （先看自己的 AO，再看全局的 GO）



立即执行函数：（函数立即释放）只有表达式可以立即执行；加上运算符如（）变表达式


function test（a,b）{
　　console.log('1')
}（1,2）;   // 不打印，会解析成函数定义和一个表达式

　


面向对象

 内置对象：Math/Array/Number/String/Boolean...

构造函数：
 任何函数都可以当成构造函数 ，只要把一个函数通过new的方式来进行调用
 自定义构造函数：`function CreateFunc(){ }`

创建对象：

1. 对象字面量 {}

2. 构造函数的方法来创建对象：  new 构造函数（）

构造函数内部原理：

1.在函数体最前面隐式的加上 var this = {} 空对象

2.执行 this.xxx = xxx;

3.隐式的返回 return this

如果函数返回了一个复杂数据类型的值，那么本次函数的返回值就是该值

        function fn3(){
            return [1,3,5];
        }
　　　　　var f3=new fn3();   //f3还是fn3的实例吗？错
        //f3值为[1,3,5]
构造函数（大驼峰式命名）： 构造函数默认有prototype属性 指向原型对象（继承原型对象共有东西）

　　原型对象默认有constructor属性指向构造函数
　　实例对象默认__proto__属性 指向原型对象：以便实例对象没有的属性会到原型查找

 包装类：new Number() new String()  new Boolean()

　　var num = 4；

　　num.len = 3; //系统隐式的加上 new Number(4).len = 3; 然后 delete

　　console.log(num.len);   =>undefined
继承：



