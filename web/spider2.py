# 爬取豆瓣top250
import requests
import json
from bs4 import BeautifulSoup


# 获取源码
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("访问失败")


# 解析源码
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml') # 创建BeautifulSoup对象，使用lxml解析库
    items = soup.find_all(name='li')  # 查询名称为li的元素，以列表形式输出
    for item in items[19:]:
    # 注意这里的[19:]，对网页源码分析后发现前19个li标签中并没有我们需要的数据，所以将其排除在外
        yield {
            # 利用find()定位我们需要的数据，并作为生成器元素
            'title': item.span.get_text(),
            'index': item.find(name='em').text,
            'image': item.find(name='a')['href'],
            'quote': item.find(class_="inq").text,
            'score': item.find(class_="rating_num").text
        }
        # 构造生成器，作为函数的返回结果


# 将数据转化为json字符串并写入到文件中
def write_to_file(content):
    with open("movies.txt", 'a', encoding='utf-8') as file:  # 以追加的权限打开文件movies.txt
        file.write(json.dumps(content, ensure_ascii=False) + '\n')  # ensure_ascii设为False，保证输出是中文形式，而不是ASCII编码
        # json.dumps()序列化时默认对中文使用ascii编码


def main(start):
    url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter'  # 定位top250的url
    html = get_html(url)
    for item in parse_html(html):
        print(item)
        write_to_file(item)


# 执行函数，完成爬取
if __name__ == '__main__':
    for i in range(10):
        main(i * 25)

