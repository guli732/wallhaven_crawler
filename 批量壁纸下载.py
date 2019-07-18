import os
import re
import urllib.parse
import urllib.request


def img_download(count):
    pattern = re.compile(r'<li><figure .*?>.*?<a class="preview" href="(.*?) .*?"></a>.*?</figure></li>', re.S)
    lt = pattern.findall(count)
    for i in lt:
        file_name = i + '.jpg'
        urllib.request.urlretrieve(i, file_name)


def request_get(url, headers, page):
    page_url = url + str(page)
    request = urllib.request.Request(url=page_url, headers=headers)
    return request


def main():
    page_start = int(input("请输入开始页码:"))
    page_end = int(input("请输入结束页码:"))
    url = 'https://wallhaven.cc/toplist?page='
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }
    for page in range(page_start, page_end + 1):
        resquest = request_get(url, headers, page)
        count = urllib.request.urlopen(resquest).read()
        img_download(count)


if __name__ == "__main__":
    main()
