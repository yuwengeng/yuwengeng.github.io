from elasticsearch import Elasticsearch

# es增删改查操作
2
# 插入数据 es.create()
def InsertDatas():
	# 默认host为localhost,port为9200.但也可以指定host与port
    es = Elasticsearch()
    es.create(index="my_index",doc_type="test_type",id=11,ignore=[400,409],body={"name":"python","addr":'河北省'})
    # 查询结果
    result = es.get(index="my_index",doc_type="test_type",id=11)
    print('单条数据插入完成：\n',result)
# InsertDatas()

# 批量插入数据
def AddDatas():
    es = Elasticsearch()
    datas = [{
            'name': '美国留给伊拉克的是个烂摊子',
            'addr': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'
            },{
            "name":"python",
            "addr":'四川省'
            }]
    for i,data in enumerate(datas):
        es.create(index="my_index",doc_type="test_type",
          id=i,ignore=[400,409],body=data)
    # 查询结果
    result = es.get(index="my_index",doc_type="test_type",id=0)
    print('\n批量插入数据完成：\n',result['_source'])
# AddDatas()

# 3 更新数据 update()
def UpdateDatas():
    es = Elasticsearch()
    es.update(index="my_index",doc_type="test_type",
          id=11,ignore=[400,409],body={"doc":{"name":"python1","addr":"深圳1"}}) # 键名doc标识不能忘记
    # 更新结果
    result = es.get(index="my_index",doc_type="test_type",id=11)
    print('\n数据id=11更新完成：\t',result['_source']['name'])

# 删除数据 - 指定文档的索引、文档类型和文档ID即可
def DeleteDatas():
    es = Elasticsearch()
    result = es.delete(index='my_index',doc_type='test_type',id=11)
    print('\n数据id=11删除完成：\t')

# 条件查询 es.search
def ParaSearch():
    es = Elasticsearch()
    query1 = es.search(index="my_index", body={"query":{"match_all":{}}}) # match_all获取索引中的所有文档
    print('\n查询所有文档\n',query1)
    query2 = es.search(index="my_index", body={"query":{"term":{'name':'python'}}}) # term
    print('\n查找名字Python的文档:\n',query2['hits']['hits'][0])