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
    # Check if file exists and delete it if it does
    filename = './十日终焉.txt'
    if os.path.exists(filename):
        os.remove(filename)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_chapter, i) for i in range(1, 713)]
        for future in concurrent.futures.as_completed(futures):
            title, info = future.result()
            if title and info:
                print(title)
                save_to_file(title, info)


if __name__ == "__main__":
    main()
