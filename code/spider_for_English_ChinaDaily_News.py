# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import datetime
from multiprocessing import Pool

# 用request和BeautifulSoup处理网页
def requestOver(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    if("gb2312" in response.text):
        response.encoding = 'gb2312'
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# 从网页下载标题和内容到txt文档
def download(title, url):
    soup = requestOver(url)
    tag = soup.find('div', class_="left_zw")
    if(tag == None):
        return 0
    title = title.replace(':', '')
    title = title.replace('"', '')
    title = title.replace('|', '')
    title = title.replace('/', '')
    title = title.replace('\\', '')
    title = title.replace('*', '')
    title = title.replace('<', '')
    title = title.replace('>', '')
    title = title.replace('?', '')
    content = ""
    for p in tag.findAll('p'):
        if (p.string != None):
            content = content + p.string
    filename = r'/Users/renee/Downloads/datachinanews.txt'
    with open(filename, 'a', encoding='utf-8', errors='ignore') as file_object:
        file_object.write('           ')
        file_object.write(title)
        file_object.write(tag.get_text())
    print('正在爬取新闻:' + title + " " + url)

# 爬虫具体执行过程
def crawlAll(url):
    soup = requestOver(url)
    for s in soup.findAll("div", class_="content_list"):
        for tag in s.findAll("li"):
            sp = tag.findAll("a")
            if("国际" in str(sp)):
                title = list(sp)[1].string
                urlAll = "http://www.chinanews.com" + str(list(sp)[1])[9:str(list(sp)[1]).find("shtml")+5]
                try:
                    download(title, urlAll)
                except Exception:
                    print("新闻爬取失败")


if __name__ == '__main__':
    pool = Pool(4)
    collection = set()
    url1 = "http://www.chinanews.com/scroll-news/"
    date = "2022/0926"
    url2 = "/news.shtml"
    p1 = []
    # 3650：十年的新闻数据
    for i in range(365*14):
        date1 = datetime.datetime.strptime(date, "%Y/%m%d")
        date2 = datetime.timedelta(days=-1)
        date = (date1 + date2).strftime("%Y/%m%d")
        target_url = url1 + date + url2
        p1.append(target_url)
        print(target_url)
    pool.map(crawlAll, p1)
    pool.close()
    pool.join()


