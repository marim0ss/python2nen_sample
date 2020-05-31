#coding: UTF-8
import requests
from bs4 import BeautifulSoup
import urllib.parse
import pprint
import csv

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url).text
soup = BeautifulSoup(html, "html.parser")

# すべてのaタグを検索してURLを表示する
links = soup.select("a")
# pprint.pprint(links)

# ----------------------------------------------------------------
# csvモジュールを使って、行として書き込む
# https://tonari-it.com/python-csv-writer-writerow/
# ----------------------------------------------------------------

filename = "link.txt"
with open(filename, 'w', encoding='utf-8') as f:
	writer = csv.writer(f)
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
		# セットにしてリンク名とurlをセットにして1行ずつ書き込む
		writer.writerow([link_name, join_url])

"""
import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# ファイルを書き込みモードで開く
filename = "linklist.txt"
with open(filename, "w") as f:
	# すべてのaタグを検索し、リンクを絶対URLで書き出す
	for element in soup.find_all("a"):
		url = element.get("href")
		link_url = urllib.parse.urljoin(load_url, url)
		f.write(element.text+"\n")
		f.write(link_url+"\n")
		f.write("\n")
"""
