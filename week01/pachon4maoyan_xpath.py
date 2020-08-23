import requests
from lxml import etree

url = 'https://maoyan.com/films?showType=3'

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'h-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'uuid_n_v=v1; uuid=45319EB0E2B111EA863A01C32E2271F626ECC3FB407644D2BA77C9876A0E9067; _csrf=4b38ccc207c7cc9b31284463dca83f89ec553457526daa85b6eb20d0855d5478; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597906159; mojo-uuid=c719f60a047b13950f1c1e7687282a9b; _lxsdk_cuid=1740aa104f3c8-0682490fe12b5e-3323767-e1000-1740aa104f3c8; _lxsdk=45319EB0E2B111EA863A01C32E2271F626ECC3FB407644D2BA77C9876A0E9067; mojo-session-id={"id":"ab6d8d6ba89e6c162e56654332b75811","time":1597906158844}; mojo-trace-id=8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597906502; __mta=242465469.1597906158944.1597906292572.1597906502528.6; _lxsdk_s=1740aa104f4-85-d42-aff%7C%7C14',
'Host': 'maoyan.com',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

# 获取文本数据
html = requests.get(url=url,headers=headers).text
# print(html)

# xpath解析数据
tree = etree.HTML(html)

dd_list = tree.xpath('//*[@id="app"]/div/div[2]/div[2]/dl')

urls = []
mylist = []

for link in dd_list:
    links = link.xpath('.//a/@href')[::3][:10]
#     print(f'links:  {links}')
    for link in links:
        url = 'https://maoyan.com' + link
        urls.append(url)
#         print(url)
        # 获取文本数据
        html = requests.get(url=url,headers=headers).text
        # print(html)

        # xpath解析数据
        tree = etree.HTML(html)
        
        # 电影名：八佰
        movie_name = tree.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')[0]
        print(movie_name)
        
        # 电影类型：剧情/战争/历史
        # /html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]
        movie_type = tree.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
        # print(f'movie_type: {movie_type}')
        
        movie_type1 = ''
        for i in movie_type:
            movie_type1 = movie_type1 + r'/' + i.strip()
        
        movie_type = movie_type1[1:]
        print(movie_type)
        
        # 上映时间：2020-08-21，长度为 10
        # /html/body/div[3]/div/div[2]/div[1]/ul/li[3]
        show_time = tree.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')[0][:10]
        print(show_time)
        
        list = [movie_name,movie_type,show_time]
        
        mylist.append(list)
        # print(mylist)


# 将采集的数据保存到csv文件中
import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
# movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)
movie1.to_csv('./movie1.csv', encoding='gbk', index=False, header=False)               






