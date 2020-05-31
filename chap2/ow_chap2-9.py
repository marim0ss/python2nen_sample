#coding: UTF-8
import requests
from bs4 import BeautifulSoup
import urllib.parse
import pprint

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url).text
soup = BeautifulSoup(html, "html.parser")

# すべてのaタグを検索してURLを表示する
links = soup.select("a")
pprint.pprint(links)

filename = "link.txt"
with open(filename, 'w', encoding='utf-8') as f:
	for link in links:
		link_name = link.text
		url = link.get("href")
		"""
		結果：
		https://www.ymori.com/books/python2nen/test1.html
		./test3.html

		※リンク２(./test3.html)は相対URL。絶対URLに変換すること

		urllib.parse.urljoinメソッドを使う
		urllib.parse.urljoin(ベースURL, 調べるor結合するURL)
		"""
		join_url = urllib.parse.urljoin(load_url, url)
		f.write(link_name + "\n")  # writeメソッド:文字列の書き込み、
		f.write(join_url + "\n")  # つながってしまうので改行いれる

# ----------------------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索し、リンクを絶対URLで表示する
for element in soup.find_all("a"):
	print(element.text)
	url = element.get("href")
	link_url = urllib.parse.urljoin(load_url, url)
	print(link_url)
"""
