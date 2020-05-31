#coding: UTF-8
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

filename = 'test.csv'
print('------------CSVファイル: {} を読み込み------------'.format(filename))
# df = pd.read_csv(filename)
# print(df)

print('------------０列目（名前の列）をインデックスに変更------------')
df = pd.read_csv(filename, index_col=0)
print(df)

# df.plot.bar()            # 棒グラフを作る
# plt.legend(loc="upper right")   # 凡例の位置を変える
# plt.show()

# ----------------------------------------------------------------
# 生徒ごと→科目ごとのグラフに変更する
#    -> 行と列を入れ替えれば良い
# ----------------------------------------------------------------
print('------------生徒ごと→科目ごとのグラフに変更する------------')

print('行列入れ替えdf： ')
print(df.T)
df_trans = df.T
df_trans.plot.bar()            # 棒グラフを作る
plt.legend(loc="upper right")
# plt.show()


print('------------グラフの色を変更------------')
# カラーリストを作っておいて、色を変更できる
colorlist = ["skyblue","steelblue","tomato","cadetblue","orange","sienna"]
df_trans.plot.bar(color = colorlist)
plt.legend(loc="lower right")
# plt.show()

print('------------グラフを画像ファイル出力------------')
# plt.savefig(ファイル名)   : plt.show()の代わりに使う。showと併用は不可？
plt.savefig('bargraph.png')
