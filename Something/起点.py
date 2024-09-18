import asyncio
import aiohttp
import os
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

async def fetch_chapter(session, url):
    try:
        async with session.get(url, headers=headers) as response:
            response_text = await response.text()
            e = etree.HTML(response_text)
            title = e.xpath('//h1/text()')[0]
            info = e.xpath('//article[@id="article"]/p/text()')
            if len(info) > 1:
                info.pop(-2)
            info = '\n'.join(info)
            return title, info
    except Exception as e:
        print(f"Error fetching chapter from {url}: {e}")
        return None

async def extract_links(session, chapter_page_url):
    try:
        async with session.get(chapter_page_url, headers=headers) as response:
            response_text = await response.text()
            e = etree.HTML(response_text)
            links = e.xpath('//div[@class="info-chapters flex flex-wrap"]//a/@href')
            return links
    except Exception as e:
        print(f"Error extracting links: {e}")
        return []

async def main():
    filename = './校花.txt'
    if os.path.exists(filename):
        os.remove(filename)

    chapter_page_url = 'https://www.7biqi.com/341_341285'  # 替换为实际章节页面的URL
    async with aiohttp.ClientSession() as session:
        links = await extract_links(session, chapter_page_url)

        tasks = [fetch_chapter(session, link) for link in links]
        results = await asyncio.gather(*tasks)

        with open(filename, 'a', encoding='utf-8') as f:
            for result in results:
                if result:
                    title, info = result
                    f.write(title + '\n\n' + info + '\n\n')
                    print(f"已完成: {title}")

if __name__ == "__main__":
    # 适配不同的运行环境
    try:
        asyncio.run(main())
    except RuntimeError as e:
        print(f"Error: {e}")
