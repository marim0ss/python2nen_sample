#coding: UTF-8
import requests
from bs4 import BeautifulSoup
import pprint

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url).text
soup = BeautifulSoup(html, "html.parser")

# すべてのaタグを検索してURLを表示する
links = soup.select("a")
pprint.pprint(links)

for link in links:
	print(link.get("href"))
	"""
	結果：
	https://www.ymori.com/books/python2nen/test1.html
	./test3.html

	※リンク２(./test3.html)は相対URL。絶対URLに変換すること
	"""

# ----------------------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):
	print(element.text)
	url = element.get("href")
	print(url)
"""
