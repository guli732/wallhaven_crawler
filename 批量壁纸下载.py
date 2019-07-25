import os
import re
import time
import urllib.parse
import urllib.request
import urllib.error


def img_download(countent, headers):
    lt = re.findall(r'<li><figure.*?>.*?<a class="preview" href="(.*?)" .*?></a>.*?</figure></li>', countent, flags=re.S)
    dirname = 'wallhaven'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    download_src = 'https://w.wallhaven.cc/full/'
    for img_src in lt:
        img_src = download_src + img_src[-6:-4] + '/wallhaven-' + img_src[-6:] + '.jpg'
        file_name = dirname + '/' + img_src[-10:]
        request = urllib.request.Request(url=img_src, headers=headers)
        try:
            response = urllib.request.urlopen(request)
            print("%s开始下载" % file_name)
            with open(file_name, 'wb') as f:
                f.write(response.read())
            print("%s下载完成" % file_name)
        except urllib.error.HTTPError as e:
            print(e)


def request_get(url, headers, page):
    page_url = url + str(page)
    request = urllib.request.Request(url=page_url, headers=headers)
    return request


def main():
    print("*" * 8, "壁纸批量下载", "*" * 8)
    page_start = int(input("请输入开始页码:"))
    page_end = int(input("请输入结束页码:"))
    url = 'https://wallhaven.cc/toplist?page='
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }
    for page in range(page_start, page_end + 1):
        print("开始传输第%s页数据" % page)
        resquest = request_get(url, headers, page)
        countent = urllib.request.urlopen(resquest).read().decode()
        img_download(countent, headers)
        print("第%s页数据传输完成" % page)
        print()
        print()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
