#coding: UTF-8
import requests
from pathlib import Path  # PC上にフォルダを作ったりアクセスしたりできる標準ライブラリ

# ----------------------------------------------------------------
# 保存用フォルダを作って保存する
"""
保存用フォルダを作る書式
	フォルダ = Path(フォルダ名)
	フォルダ.mkdir(exist_ok=True)

フォルダ内のファイルにアクセスするパスを作る
	フォルダ.joinpath(ファイル名)
"""
# ----------------------------------------------------------------

save_folder = Path("download")  # フォルダ作成
save_folder.mkdir(exist_ok=True)

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)


filename = image_url.split('/')[-1]       # URLから最後のファイル名を取り出して、
save_folder_path = save_folder.joinpath(filename)   # フォルダ名と連結

# 画像データをファイルに書き出す（画像データはバイナリファイル）
# →モードはwb   : w書き込み、bバイナリ
# ⭐️パスはフォルダに連結したパスを指定する
with open(save_folder_path, 'wb') as f:
	f.write(imgdata.content)     # バイナリファイルなので.textでなくcontent

"""
# 保存用フォルダを作る
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

# 画像データを、ファイルに書き出す
with open(out_path, mode="wb") as f:
	f.write(imgdata.content)
"""
