import requests
from bs4 import BeautifulSoup
import os

def get_favicon_and_title(url):
    if not url.startswith('http'):
        url = 'http://' + url
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string.strip()
        favicon_url = url + 'favicon.ico'
        return title, favicon_url
    except Exception as e:
        print("Error:", e)
        return None, None

def write_to_file(title, favicon_url, count):
    with open('website_info.md', 'a', encoding='utf-8') as file:
        file.write("No.{}\n".format(count))
        file.write("标题: {}\n".format(title))
        file.write("![{}]({})\n".format(title, favicon_url))
        file.write("图标URL: {}\n\r".format(favicon_url))

def main():
    # 打开文本文件 例子:
    #https://www.djangoproject.com/
    #Flask - https://flask.palletsprojects.com/
    #https://flask.palletsprojects.com/
    #https://flask.palletsprojects.com/
    with open('urls.txt', 'r') as file:
        # 读取文件内容
        text_content = file.read()

    # 按换行符分割文本内容
    lines = text_content.split('\n')

    # 提取每行中的网址
    urls = []
    for line in lines:
        # 查找是否有网址
        start_index = line.find('https://')
        if start_index == -1:
            start_index = line.find('http://')
        if start_index != -1:
            # 截取网址
            end_index = line.find(' ', start_index)
            if end_index == -1:
                url = line[start_index:]
            else:
                url = line[start_index:end_index]
            urls.append(url)

    # 打印提取出的网址
    count = 0
    for url in urls:
        # while True:
        #url = input("输入网址:")
        title, favicon_url = get_favicon_and_title(url)

        if title and favicon_url:
            count += 1
            write_to_file(title, favicon_url, count)
            print(f"{count}.{title}网站标题和favicon已写入到文件website_info.md中")
            print(url)
        else:
            print("无法获取网站标题和favicon")

        # cont = input("是否继续输入网址？(y/n): ").lower()
        # if cont != 'y':
        #     break

if __name__ == "__main__":
    main()