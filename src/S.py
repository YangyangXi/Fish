import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
for i in range(1, 713):
    url = f'https://www.zsdade.com/books/138095/{i}.html'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    e = etree.HTML(response.text)
    title = e.xpath('//h1/text()')[0]
    info = e.xpath('//div[@id="chaptercontent"]/text()')
    info.pop(-2)
    info = '\n'.join(info)
    print(title)

    with open('./我本无意成仙.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')