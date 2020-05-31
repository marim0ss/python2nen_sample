#coding: UTF-8
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib.parse
import pprint

# 保存フォルダ作成
save_folder = Path("download")
save_folder.mkdir(exist_ok=True)

# 画像ファイルを取得する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url).text
soup = BeautifulSoup(html, "html.parser")

#imgタグだけ取り出し
img_tags = soup.select("img")
# pprint.pprint(img_tags)

for tag in img_tags:
	img_url = tag.get("src")  # 画像URL取得できる
	# print(img_url)
	join_url = urllib.parse.urljoin(load_url, img_url)  # 画像URLを絶対URLに変換
	print(join_url)

	filename = join_url.split('/')[-1]
	# -----------------------------------------------------
	# save_folder_path = save_folder.joinpath(filename)
	# pprint.pprint(save_folder_path)

"""
import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
	src = element.get("src")

	# 絶対URLと、ファイルを表示する
	image_url = urllib.parse.urljoin(load_url, src)
	filename = image_url.split("/")[-1]
	print(image_url, ">>", filename)
"""
