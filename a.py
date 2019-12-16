#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

url = 'https://www.ivsky.com/tupian/tiankong_t811/index_2.html'

import requests, os, time, re, queue, socket
from bs4 import BeautifulSoup

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
'Referer': 'https://www.ivsky.com/bizhi/swords_of_legends_two_v58346/pic_916937.html',
'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
'Cookie': 'Hm_lvt_862071acf8e9faf43a13fd4ea795ff8c=1576379369; BDTUJIAID=be57b2683d07d3f8d5048a8df8b7ffd4; Hm_lpvt_862071acf8e9faf43a13fd4ea795ff8c=1576381563'
}

# url = 'https://www.ivsky.com'
def home_page(url):
    # 首页
    # url = 'https://www.ivsky.com'
    res = requests.get(url, headers=header)
    # print(type(res.status_code ))
    lxml = BeautifulSoup(res.text, 'lxml')
    return lxml


def Picture_book(lxml):
    # 图片大全
    titles = lxml.select('body > div:nth-child(4) > div > div:nth-child(2)')[0].find_all('a')
    'body > div:nth-child(4) > div > div:nth-child(2)'
    # print(titles)
    url = 'https://www.ivsky.com/tupian/'
    dic = Page_title(titles, '图片大全', url=url)
    return dic


def Page_title(title, name, url):
    # 页面标题url
    dic = {}
    i = 1
    for page in title:
        page_url = page.get('href')
        dic['img_name'] = page.get_text() + '第%s链接' % i
        dic['location'] = f'首页-{name}-' + page.get_text()
        # print(page_url, title)
        dic['img_url'] = url + page_url.split('/')[-2]
        i += 1
        path = fr'./图片链接/{name}.txt'
        with open(path, mode='a', encoding='utf-8') as f:
            f.write(str(dic))
            f.write('\n')
    return dic

def Desktop_Daquan(lxml):
    # 桌面大全
    titles = lxml.select('body > div:nth-child(4) > div > div:nth-child(3)')[0].find_all('a')
    'body > div:nth-child(4) > div > div:nth-child(2)'
    # print(titles)
    url = 'https://www.ivsky.com/bizhi/'
    dic = Page_title(titles, '桌面大全', url=url)
    return dic
    pass

# lxml = home_page(url)
# dic = Picture_book(lxml)
# Desktop_Daquan(lxml)
# print(dic)
#

def Parsing_page(lxml):

    # global i
    # 解析页面
    i = 1
    # print(lxml)
    title = lxml.select('body > div:nth-child(3) > div.left > ul')[0].find_all('img')
    dic = []
    di = {}

    for page in title[1:]:

        page_url = page.get('src').split(r'/t/')[-1]
        title = page.get('alt')
        # print(page_url, title)
        di['img_name'] = title + ' - 第%s张' % str(i)
        di['location'] = '城市旅游-北京-中国万里长城图片'
        di['img_url'] = 'https://www.ivsky.com/img/tupian/pic/' + page_url
        path = r'./txt' + '/' +  '天堂图.txt'
        with open(path, mode='a', encoding='utf-8') as f:
            f.write(str(di))
            f.write('\n')
        print(di)
        dic.append(di)
        # print(di)
        i += 1
        print(i)
    print(dic)
    return dic
# lxml = home_page(url)
# dic = Parsing_page(lxml)
# print(dic)

# {'img_name': '中国万里长城图片 - 第2张',
# 'location': '城市旅游-北京-中国万里长城图片',
# 'img_url': 'https://www.ivsky.com/img/tupian/pic/201812/11/the_great_wall-003.jpg'}
# {'img_name': '空中多彩的热气球图片 - 第2张', 'location': '城市旅游-北京-中国万里长城图片', 'img_url': 'https://www.ivsky.com/img/tupian/pic/201904/26/reqiqiu-015.jpg'

def Small_taxonomy(lxml, location, ind, img_na,name):
    # 小分类
    title = lxml.select(f'#sline{ind}')[0].find_all('a')
    # print(title)  #sline1 > div #sline2 > div #sline3 > div #sline4 > div
    #                #sline1 #sline2
    dic = {}
    for page in title[1:]:
        page_url = page.get('href')

        img_name = page.get_text()
        dic['img_name'] = img_name
        dic['location'] = location + '-' + img_name

        dic['img_url'] = 'https://www.ivsky.com' + page_url
        path = fr'./分类链接/{name}/{img_na}.txt'
        with open(path, mode='a', encoding='utf-8') as f:
            f.write(str(dic))
            f.write('\n')

        # print(dic)
    return dic

def home_page(url):
    # 首页
    # url = 'https://www.ivsky.com'
    time.sleep(1)


# print(type(res.status_code ))
    try:
        res = requests.get(url, headers=header,timeout=5)
        if res.status_code == 200:
            print(res.status_code)
            return res
        if res.status_code == 404:
            return 404
    except Exception as e:
        print('由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败', e)


    print('继续请求=================', url)
    res = home_page(url)
    return res


def Parsing_page(lxml, location,name):

    # 解析页面
    # print(lxml)
    global l
    title = lxml.select('body > div:nth-child(3) > div.left > ul')[0].find_all('img')
    # print(title)
    # # for i in url:
    # img = url[0].find_all('img')
    # src = img.get('src')
    # print(src)
    dic = {}
    for page in title[1:]:
        page_url = page.get('src').split(r'/t/')[-1]
        titl = page.get('alt')
        # print(page_url, title)
        dic['img_name'] = titl + f' - 第{l}张'
        dic['location'] = location + '-' +titl
        dic['img_url'] = 'https://www.ivsky.com/img/tupian/pic/' +page_url
        l += 1
        with open(fr'./txt/{name}.txt', mode='a', encoding='utf-8') as f:
            f.write(str(dic))
            f.write('\n')
    return dic
    # {'img_name': '其他类别第19链接',
    # 'location': '首页-图片大全-其他类别',
    # 'img_url': 'https://www.ivsky.com/tupian/qita'}


while True:
    txt_list = os.listdir('./分类链接/桌面大全/')

    for index,txt in enumerate(txt_list): print('%s:%s'%(index,txt))
    # print(len(txt_list))
    # for j in range(len(txt_list)):
    #
    #     txt_name = input(j)

    txt_name = 0
    name = txt_list[int(txt_name)].split('第')[0]
    print(name)
    print('输入完成，请等待')
    urls = []
    ind = 1

    for i in open('./分类链接/桌面大全/%s' % txt_list[int(txt_name)], 'r', encoding='utf-8').readlines():
        if not i == '\n':

            img = eval(i.split('\n')[0])
            location = str(img['location'])
            img_na = img['img_name']
            data = 1
            l = 1
            while True:
                url = img['img_url'] + f'index_{data}.html'
                print(url)
                res = home_page(url)
                if res == 404:
                    print('页面不存在')
                    break
                # print(lxml)




                # elif res == 443:
                #     print(444444444444444444444444444444444444)
                elif res.status_code == 200:
                    lxml = BeautifulSoup(res.text, 'lxml')
                    Parsing_page(lxml,location,name)
                    # Small_taxonomy(lxml, location, ind, img_na, name=name)
                    print('请求成功+++++++++++++++++++++++++++++++++++++')
                #
                # ind += 1
                # time.sleep(1)
                data += 1

    txt_name += 1

