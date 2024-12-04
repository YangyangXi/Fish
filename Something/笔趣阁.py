import requests
from lxml import etree
import concurrent.futures
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


def fetch_chapter(i):
    url = f'https://www.bqgda.cc/books/158555/{i}.html'
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        e = etree.HTML(response.text)
        title = e.xpath('//h1/text()')[0]
        info = e.xpath('//div[@id="chaptercontent"]/text()')
        if len(info) > 1:
            info.pop(-2)
        info = '\n'.join(info)
        return title, info
    except Exception as e:
        print(f"Error fetching chapter {i}: {e}")
        return None, None


def save_to_file(title, info):
    with open('./十日终焉.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')


def main():
    filename = './十日终焉.txt'
    if os.path.exists(filename):
        os.remove(filename)
# 因为不知道小说具体会有多少章节，所以我设置了个1200章，可以根据不同小说的章节来设定，大点也没关系
    results = [None] * 1200  # 创建一个列表用于存储结果
    total_chapters = 1200

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_chapter, i): i for i in range(1, total_chapters + 1)}
        completed = 0

        for future in concurrent.futures.as_completed(futures):
            i = futures[future]  # 获取章节索引
            title, info = future.result()
            if title and info:
                results[i - 1] = (title, info)  # 按顺序存储结果
                completed += 1
                print(f"已完成: {completed}/{total_chapters}")

    for title, info in results:
        if title and info:
            print(title)
            save_to_file(title, info)

if __name__ == "__main__":
    main()


