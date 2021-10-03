---
title: 'spider'
date: 2018-11-26 17:08:58
tags:
- '爬虫'
- 'python'

categories:
- '爬虫'
---

 HTML 用于展示数据，而 XML 用于结构化、传输和存储数据 XML 文档必须有一个根元素；
     嵌套的 HTML 元素,结构化的一种文档结构 ——> W3C 针对其指定了一个标准化的模型DOM 
### json数据
获取方式:
     ajax请求接口
     切换移动h5端
     app抓包获取
     
json模块：⽤于字符串和 python 数据类型间进⾏转换
     js：JSON.stringify   JSON.parse
 > 只有基本数据类型才能转换成JSON格式字符串
### python封装http库：# 请求的是源代码

    标准urllib库
    第三方库request
1. urllib库：
     1. request模块：
          urlopen()函数
               urllib的params需urlencode转换类型
               data参数：请求方式变为post  get方式一般需拼接query_string
                    bytes(urllib.parse.urlencode(form_data).encode()) 
                    # data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.  
               超时处理：timeout
                    read() 返回二进制代码 data=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
          urlretrieve(图片的源地址,保存文件的文件名)  ——打开并保存url内容 重新请求url响应 就实现了请求图片、新建文件、写入文件三个步骤的功能。
          Request类 :构造request请求对象  (url, data=None, headers={},origin_req_host=None, unverifiable=False,method=None)
          Handler类
     response:
          read()  读取字节类型
          geturl()    获取请求url
          getheaders()
          getcode()
          readlines()     

     2. error模块：
          URLError类（作用于request模块的异常）
          HTTPError类(子类)
               三个属性code reason headers

               解析异常：AttributeError：
               标签为None
     3. parse模块：（处理url）
          解析urlparse() (根据url的6个部分解析)
          构造urlunparse() params接受长度为6的可迭代对象
              urlsplit()
          合并urljoin()  # url自动修正拼接完整  
               - 拼接完整url
                    if item['href'] is not None:
                         item['href'] = urllib.parse.urljoin(response.url, item['href'])

          url编码转换：url中若出现 $ 空格 中文等，就要对其进行编码
               1.字符串：urllib.parse.quote(str)  url编码
                  unquote() url解码  # requests.utils.unquote(str,encoding='utf-8', errors='replace')
               2.字典：  urllib.parse.urlencode(dict) 转化为url参数

2. requests库 - 添加/修改请求头
  - GET（url,params,headers[cookies=],timeout）   使用 cookies 参数，首先需要将 Cookie 值处理为字典的形式：
     params:dict => query-data  
     headers = {
          cookie,
     }
     当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
     iter_content：一块一块的遍历要下载的内容
     iter_lines：一行一行的遍历要下载的内容
     使用上面两个函数下载大文件可以防止占用过多的内存，因为每次只下载小部分数据。

          示例代码：
          1 r = requests.get(url_file, stream=True)
          2 f = open("file_path", "wb")
          3 for chunk in r.iter_content(chunk_size=512):
          4     if chunk:
          5         f.write(chunk)

  - post(url,data{},headers,cookies,files={'avator':open(r'1.jpg','wb')})   

     1. 处理登录：声明一个session会话，自动处理cookies
            操作session获取数据： session.cookies.save()
            res.cookies.get_dict()

     2. 证书验证（https协议）
          1. 设置认证verify=False
          2. 指定cert=（path）

     3. 代理设置
          (proxies=..)

     4. requests异常处理：
          from requests.exceptions import RequestException
     5. auth 内网认证
          auth = ('user','pass')

    res方法：
    - 获取服务器的原始套接字响应:r.raw  请求：(,stream=True)
          边下载边存硬盘:for chunk in r.iter_content(chunk_size=1024):
     
     r.json() 获取json数据  相当于content = response.content  results = json.loads(content)

     获取cookies字典：response.cookies.get_dict()

     **response属性**（6）响应头响应体相关:  r.request.headers
   - r.status_code

        http请求的返回状态，200表示连接成功，404表示连接失败没有对应资源
        301/302 永久/临时重定向
        403 没有权限访问 400：客户端请求语法错误 404：请求的资源没有找到
        500 服务器错误 503 服务器正在维护

   - r.text

        http响应**解码**后的str形式，根据r.encoding

   - r.encoding  从HTTP header中猜测的响应内容编码方式
   - r.apparent_encoding  从内容分析出的响应内容的编码方式（备选编码方式）
          # 乱码解决方案   设置编码: res.encoding=res.apparent_encoding

   - r.content .decode()

        HTTP响应内容的编码二进制形式bytes类型

   - r.headers

        http响应内容的头部内容

> 利用 XPath css
选择器来提取定位某个节点，然后再调用相应方法获取它的正文内容或者属性

3个解析库：bs，lxml，pyquery

### bs4（网页解析库，支持多种解析器'html.parser' 'lxml'）
     初始化一个soup对象，指定解析库
          > bs自动将输入文档转 Unicode 编码，输出文档转换为 UTF-8 编码 你不需考虑编码方式（bs将HTML文档转为DOM树）
     
          soup = BeautifulSoup(open('index.html'),'html.parser') #打开本地 HTML ⽂件的⽅式来创建对象


     方法：
     1. soup.find_all(tag, attributes, recursive, text, limit限制个数, keywords)   // 'class_'防止冲突
          参数值可以是字符串 或正则re.compile('')
          返回list类型的html源码,find方法返回bs.BeautifulSoup对象
        
        在 BeautifulSoup 中每个元素都有一个 get_text() 获取文本   取属性：get（属性名）
        - 取标签: soup.p标签：默认只取第一个 soup.p.string取文本
        - 获取属性：
        soup.attrs # 返回标签属性dict  
        element.text提取text文本内容
        soup.a['href']   

        获取属性们：
          ···
          nameList = bs.find_all(text='the prince',attrs=｛’id＇：’list'｝)
          ['the prince', 'the prince', 'the prince', 'the prince', 'the prince', 'the prince', 'the prince']
          ···
          
          bs节点会包括'\n' ' ',一般不用  replace.('\xa0'*8,'\n\n')替换8个空格为回车分段(HTML中为&nbsp)
        - 获取直接子节点: div.contents                
          处理同辈节点(siblings)和父辈节点(parents):
               next_sibling　next_siblings 返回后面的兄弟节点　　previous_siblings　　返回前面的兄弟节点

     2. soup.select('css选择器'，limit=1)     //select选择器返回list； css选择器更简洁
          
          - css选择器：标签名与类名、id 名组合   
          h1::text  ::attr(属性)获取标签属性 伪类选择器  [xpath @属性]

            li:nth-child(3)选取第三个li元素
            li:nth-child(2n) 第偶数个
            a[title]选取有title属性的a元素
            .container.wrapper 表示同一标签class
            ul p 选取所有子元素，包括嵌套不相关
            ul + p 选取ul后面第一个p元素(下一个)   ~所有兄弟
            div#container > ul 第一个子元素
         
    * soup.prettify() 以标准缩进输出代码


  *** lxml解析html代码和文件
        parse_text: etree.HTML(text)  #直接读取字符串
        parse_file：etree.parse()     #文件读取
        # 按字符串序列化 HTML文档
        result = etree.tostring(html)

     - Xpath：在xml文档中选取元素属性的路径表达式
     
          下一级xpath加  .//选中文档所有子孙标签  ./    
          //*[@class='']    
          / 选中直接子节点  //开头遍历所有  //选中文档所有子孙标签  
          */@属性：获取元素对应属性值  tag（）获取标签名   text（）获取文本    
          
          下标a[1]  li[last()-1] 可以找到倒二个元素  /a/..定位父节点
          
          模糊查询/[contains()]   
          a[text()='下一页'] ：class名称相同时用

    四个基本方法：
     .extract（） 序列化该节点为 Unicode 字符串并返回 list
     .css(): 返回该表达式所对应的所有节点的 selector list，语法同 BeautifulSoup4
     .re(): 返回 Unicode 字符串 list 正则只有\d才能提取数字




 ### pyquery选择器  from pyquery import PyQuery as pq
     方法：
     find()查找子孙节点  children（）查找所有子节点
     多个节点.items()方法 返回一个generator

     html() attr() 返回第一个节点
     text() 返回所有text 中间空格分开，str类型


## js动态渲染问题：

1. 模拟Ajax异步数据爬取(返回json类型）
     Type：xhr
2. 模拟浏览器运行的库，如 Selenium Splash PyV8 Ghot pyputeer等

cookies池，代理池，UA（from fake_useragent import UserAgent）

协程的优势：
     最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
     第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多


### 实战经验：
     简单数据，直接用正则提取   
     # def write_to_file(content) :
          with open (’result.txt ’,’a ’, encoding=’ utf-8') as f:   # 写入文件有中文，指定编码格式
               f.write(json.dumps(content ，ensure_ascii=False) +’\n')   ## json.dumps() 序列化时默认使⽤的 ascii 编码

     # json.dump(item,open('sfda.json','w'),ensure_ascii=False)  

     
# 代码片段
- 处理src: 
 item['img_list'] = [requests.utils.unquote(i).split('src=')[-1] for i in item['img_list']]

- # 去掉列表中的空字符串和字符串的空白
 content = [i.strip() for i in content if len(i.strip())>0] 

- scrapy带cookies请求,转换cookies为dict
 def start_requests(self):
        cookies = "anonymid=jqpacc0i4eh2re; depovince=ZGQT; _r01_=1; JSESSIONID=abcM4DE98_8lS_2hu7hLw;"
        cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}









### selemium 浏览器自动化

        from selenium import webdriver
        driver = webdriver.Chrome()
        drive.get('')   //打开特定网页
        drive.page_source  //打开网页源码
     获取源代码page_source
          获取节点属性等信息
     查找节点：（通过XPath/CSS选择器）
          单个节点/多个节点find_element() 返回的是WebElement类型
           * 查找单个节点
               ``` python
               from selenium import webdriver
               browser = webdriver.Chrome()
               browser.get('https://www.taobao.com')
               input_ first = browser.find_element_by_id('q')
               input_second = browser.find_element_by css_selector   ('#q’)
               input_third = browser_find_element_by_xpath('//*[@id ＝ 飞”］’）
               print(input_first, iput_second, input_third)
               browser.close()
               ```
               另一种参数的灵活方式：
               `find_element(By.ID, id ）`

               * 多个节点
               `find_elements(By.CSS_SELECTOR,'.service-bd li') `

     节点交互：
          动作链ActionChains

          输入文字时用 `send_keys()`方法，清空文字时用` clear()`方法，点击按钮时用 `click()`方法


     (万能方法)模拟运行js：execute_script ()

     切换框架：switch_to.frame()

     加载等待：
          隐式等待browser.implicitly_ wait(10)
     显式等待：

puppeteer && pyppeteer