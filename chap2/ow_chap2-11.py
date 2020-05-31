#coding: UTF-8
import requests
import pprint

# ----------------------------------------------------------------
# 画像ファイルを取得->保存する
# ----------------------------------------------------------------
image_url = "https://www.ymori.com/books/python2nen/sample1.png"

# 画像なので.textはつけない
imgdata = requests.get(image_url)

# ----------------------------------------------------------------
#ファイル名はURLの最後の名前にする
# ----------------------------------------------------------------
"""
filename = image_url.split('/')  # split:文字列の分割メソッド。
print(filename) # ['https:', '', 'www.ymori.com', 'books', 'python2nen', 'sample1.png']
print(image_url.split('/')[-1])  # sample1.png  [-1]後ろから１番目の要素を特定できる
"""
filename = image_url.split('/')[-1]


# 画像データをファイルに書き出す（画像データはバイナリファイル）
# →モードはwb   : w書き込み、bバイナリ
with open(filename, 'wb') as f:
	f.write(imgdata.content)     # バイナリファイルなので.textでなくcontent



"""
import requests

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出す
filename = image_url.split("/")[-1]

# 画像データを、ファイルに書き出す
with open(filename, mode="wb") as f:
	f.write(imgdata.content)
"""
