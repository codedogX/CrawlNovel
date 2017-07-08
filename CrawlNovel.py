import requests
from requests import RequestException
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return  None
    except RequestException:
        print('请求页面出错',url)

def write_to_file(content):
    with open('我当道士那些年.txt','a',encoding='utf-8') as f:
        f.write(content)
        f.close()

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    items = soup.select('#content')
    for item in items:
        print(item.text)
        write_to_file(item.text)

if __name__ == '__main__':
    for i in range(1001,2668):
        i = i * 10
        url = 'https://www.yite.cc/book/wddsnxn/{}.html'.format(i)
        html = get_html(url)
        parse_html(html)