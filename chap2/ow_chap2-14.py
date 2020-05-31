#coding: UTF-8
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib.parse
import time
import pprint

# 保存フォルダ作成
save_folder = Path("download2")
save_folder.mkdir(exist_ok=True)

# ページにアクセス
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url).text
soup = BeautifulSoup(html, "html.parser")

#imgタグだけ取り出し
img_tags = soup.select("img")
# pprint.pprint(img_tags)

for tag in img_tags:
	img_url = tag.get("src")  # その中から画像URLを抽出する
	# print(img_url)
	join_url = urllib.parse.urljoin(load_url, img_url)  # 画像URLを絶対URLに変換
	print(join_url)

	filename = join_url.split('/')[-1]
	imgdata = requests.get(join_url).content  # imgのURLにアクセス

	save_folder_path = save_folder.joinpath(filename)
	with open(save_folder_path, 'wb') as f:
		f.write(imgdata)
	print("------------画像：{} を保存します------------".format(filename))
	time.sleep(1)
print("------------このページの全ての画像を保存しました------------")

"""
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 保存用フォルダを作る
out_folder = Path("download2")
out_folder.mkdir(exist_ok=True)

# すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
	src = element.get("src")

	# 絶対URLを作って、画像データを取得する
	image_url = urllib.parse.urljoin(load_url, src)
	imgdata = requests.get(image_url)

	# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
	filename = image_url.split("/")[-1]
	out_path = out_folder.joinpath(filename)

	# 画像データを、ファイルに書き出す
	with open(out_path, mode="wb") as f:
		f.write(imgdata.content)

	# 1回アクセスしたので1秒待つ
	time.sleep(1)
"""
