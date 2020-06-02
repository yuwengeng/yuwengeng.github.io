---
title: 'Scrapy框架'
date: 2018-11-26 17:08:58
tags:
- '爬虫'

categories:
- 'scrapy'
- '爬虫'
---

## 经典爬虫框架：
    1. url 管理器：Scheduler调度器
        主要两个变量：已爬取url集合，未爬取集合；
        去重：内存去重；
              缓存数据库去重，布隆算法过滤

    2. 下载器：

logging模块：保存持久化日志信息

## scrapy框架: 任务分离固定明确
> 框架中数据流：request，response，item
    > item会内部返回给pipline 在管道间传递 ,先在settings中开启pipline
    Spider opened 开启
    
scrapy shell url 进行快速调试
    scrapy check 检查代码是否有错误
    scrapy list列出所有可用的爬虫
    scrapy fetch url 源代码下载下来并显示出来

### spider主程序：

 - 被继承的基类scrapy.Spider中:
    属性：

    方法：
    1. start_requests() 这个方法必须返回一个可迭代对象
    2. parse(response)  默认的回调函数
         从生成器取尽第一部分的 request，然后再获取第二部分的 item，取到 item 了，就会放
         到对应的 pipeline处理；
          取尽之后，parse()⼯作结束，引擎再根据队列和 pipelines 中的内容去执⾏相
          应的操作；
          8. 程序在取得各个⻚⾯的 items 前，会先处理完之前所有的 request 队列⾥的请求
          ，然后再提取 items。
          7. 这⼀切的⼀切，Scrapy 引擎和调度器将负责到底。
          yield 返回Request，dict None BaseItem 
    
     - CrawlSpider类: 自动匹配响应的规律url，构造二次Request ，url自动修正[parse.urljoin()]；  定义rules匹配规则；  follow=True提取的url响应中继续跟进匹配；
            Rule(LinkExtractor(allow=re,restrict_css(),restrict_path()),callback='parse')
    scrapy genspider -t crawl 
        使用场景：
            url规律能被正则或xpath匹配
            实现自动翻页
### settings：
    LOG_LEVEL = "WARNING"  debug info  #设置scrapy日志等级
    数据库初始化:
    REDIS_URL = "redis://127.0.0.1:6379"


### requests对象：scrapy.Request()类实例化

    - Request类常用参数：
        callback，
        dont_filter=True不过滤，默认对url去重
        meta:元数据字典 item{}，在不同解析函数中传递item数据  注意item层级多时 用deepcopy()防止同一引用污染。
        headers,
        cookies={} # cookies只能单独设置，不在headers

        priority=0，请求优先级
    
    - scrapy post请求模拟登录:
        scrapy.FormRequest(url,formdata,callback) 
        
            # 自动从响应中找到form表单字段进行登录
            FormRequest.from_response(
                response,
                formdata,# 只需写user poassword 
                formid=None,
                formname=None,
            )

 
### response对象：

        shell: 【response.加tab】
            res.body相当于res.content
            res.url 发起请求的url
            res.text
            res.meta{}
    selector选中元素方法：xpath，css ，返回selector对象list
    
    提取数据对象data属性：
    extract()方法 序列化选中内容为Unicode 字符串 并返回字符串列表
    extract_first():直接返回字符串

### Item：
    初始化要爬取的Item类 实例化后为dict类型，以便为字段赋值

### item pipeline管道处理组件:
    必有process_item(self,item,spider)方法，必须返回item，以便继续处理

    初始化数据库连接:
    - open_spider(self,spider) # 相当于爬之前先开盖
    - close_spider(self,spider)

    - scrapy 保存信息的最简单的⽅法主要有四种，-o 输出指定格式的⽂件 【json csv xml jsonl】




### 中间件

1. Downloader middleware： 用于修改request和response （ 代理池，UA库，）
    process_request(request,spider)被调用

    process_response(request, response, spider)
    process_exception(request, exception, spider)
    ---
    <!-- class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        ua = random.choice(spider.settings.get("USER_AGENT_LIST"))
        request.headers["User-Agent"] = ua

    class CheckUserAgent: # 检查ua
        def process_response(self, request, response, spider):
            # print(dir(response.request))
            print(request.headers["User-Agent"])
            return response -->
   - 重写RandomUserAgentMiddlware：
    from fake_useragent import UserAgent 
    # 引入开源库
    class RandomUserAgentMiddlware(object):

        def __init__(self, crawler):
            super(RandomUserAgentMiddlware, self).__init__()
            self.ua = UserAgent()
            #可读取在settings文件中的配置，来决定开源库ua执行的方法，默认是random，也可是ie、Firefox等等
            self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

        @classmethod
        def from_crawler(cls, crawler):
            return cls(crawler)

        #更换用户代理逻辑在此方法中
        def process_request(self, request, spider):
            def get_ua():
                return getattr(self.ua, self.ua_type)

            <!-- print  get_ua()2 -->
            request.headers.setdefault('User-Agent', get_ua())

    添加代理：request.meta['proxy'] = 
2. Spider Middleware

### 异步加多线程

### 分布式爬虫-多台主机协同爬取

> 爬取队列 Queue必须始终为一个，也就是共享爬取队列 ；这样才能保证 Scheduer 从队列里调度某个 Request 之后，其他Scheduler 不会重复调度此 Request ，就可以做到多个 Schduler 同步爬取 这就是分布式爬虫的基本雏形
**分布式架构**

 1. 维护爬取队列

     Redis 支持的这几种数据结构存储各有优点：
    列表有 lpush （） lpop （） rpush （） rpop （）方法，我们可以用它来实现先进先出式爬取队列，也可以实现先进后出栈式爬取队列
    集合的元素是无序的且不重复的，这样我们可以非常方便地实现随机排序且不重复的爬取队列
    有序集合带有分数表示，而 Scrapy的Request 也有优先级的控制，我们可以用它来实现带优先级调度的队列
    
    我们需要根据具体爬虫的需求来灵活选择不同的队列

 2. 如何去重

    > Scrapy 有自动去重，它的去重使用了 Python 中的集合，生成哈希指纹（忽略request headers） 
    scrapy单个Request队列放在内存中
    分布式去重则把各个主机的request都存在一个redis数据库集合中，由此判断去重

 3. 防止中断，断点续爬
    
    保存队列在本地
    scrapy crawl spider -s JOB_DIR=crawls/spider

### RedisSpider()
部分修改
from scrapy_redis.spiders import RedisSpider
redis_key="" #带爬取队列,从中读取start_url

自定义request:
    def make_request_from_data(self, data): # RedisSpider内置方法,data来自redis
    def start_requests(self):

# redis-cli:
keys *
lpush key_name url

    


