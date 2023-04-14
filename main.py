"""
爬取图片壁纸
url:https://pic.netbian.com/4kmeinv/
需要requests和bs4库
"""
#
# url = 'https://pic.netbian.com/4kmeinv/'

import requests
import os



def html(url):
    resp = requests.get(url)
    resp.encoding="gbk"
    print(resp.status_code)
    html = resp.text
    # print(html)
    return html

def download(html):
    #开始解析图片
    from bs4 import BeautifulSoup
    soup= BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"https://pic.netbian.com{src}"
        print(src)

        # 保存图片
        filename = os.path.basename(src)
        with open(f"pic/{filename}","wb") as f:
            re_img = requests.get(src)
            f.write(re_img.content)

# 爬取n页的pic，页数为n
n = int(input("请输入要爬取的页数n（n大于大于2）："))
urls = ['https://pic.netbian.com/4kmeinv/'] + [
f"'https://pic.netbian.com/4kmeinv/index_{i}'"
for i in range(2,n)]
for url in urls:
    print("---正在爬取:",url)
    html = html(url)
    download(html)