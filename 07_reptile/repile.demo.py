# 1. 爬虫的基本工作流程
# 发送请求 (Request)：向服务器申请访问网页。
# 获取响应 (Response)：服务器返回网页的 HTML 源代码。
# 解析数据 (Parsing)：从乱七八糟的代码里提取出你想要的信息（如标题、价格）。
# 保存数据 (Storage)：存入文件或数据库。

## Books to Scrape (最适合练习提取列表数据) 完整地址： http://books.toscrape.com/ 这是最经典的模拟电商网站，适合练习如何抓取书籍的标题、价格、评分、库存状态以及处理多页翻页。
## Quotes to Scrape (最适合练习多重解析)  完整地址： http://quotes.toscrape.com/ 这是一个名言警句网站，适合练习如何通过 Tags（标签） 过滤内容，或者学习如何模拟用户登录。
## Scrape This Site (最适合进阶挑战)  完整地址： https://www.scrapethissite.com/pages/ 这个网站提供了不同的“关卡”，比如爬取全世界的国家数据（静态表格）、奥斯卡获奖电影信息（Ajax 动态加载）等。

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

BASE_URL = "http://books.toscrape.com/"

def scrape_page(url):
    """
    爬取指定页面的书籍信息
    返回一个列表，每个元素是字典：{书名, 价格, 评分, 库存}
    """
    books_data = []
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all("article", class_="product_pod")
            for book in books:
                # 书名
                title = book.h3.a["title"]
                # 价格
                price = book.find("p", class_="price_color").text
                # 评分（存储在 class 属性里，如 "star-rating Three"）
                rating_class = book.find("p", class_="star-rating")["class"]
                rating = rating_class[1]  # 第二个元素是具体评分
                # 库存状态（在 product_price 区块里）
                stock = book.find("p", class_="instock availability").get_text(strip=True)

                books_data.append({
                    "书名": title,
                    "价格": price,
                    "评分": rating,
                    "库存": stock
                })
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
    return books_data

def get_next_page(soup, current_url):
    """
    查找下一页链接并返回完整 URL
    """
    next_page = soup.find("li", class_="next")
    if next_page:
        return urljoin(current_url, next_page.a["href"])
    return None

def scrape_all_books():
    url = BASE_URL
    all_books = []

    while url:
        print(f"正在爬取: {url}")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # 当前页面书籍信息
            books = scrape_page(url)
            all_books.extend(books)
            # 下一页
            url = get_next_page(soup, url)
            time.sleep(1)  # 延迟避免过快请求
        else:
            print(f"请求失败，状态码: {response.status_code}")
            break

    # 保存到 CSV，编码 utf-8-sig，避免 Excel 打开乱码
    print(all_books)
    df = pd.DataFrame(all_books)
    df.to_csv("books.csv", index=False, encoding="utf-8-sig")

    print(f"爬取完成，共获取 {len(all_books)} 本书，已保存到 books.csv")

if __name__ == "__main__":
    scrape_all_books()
