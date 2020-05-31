#coding: UTF-8
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# ----------------------------------------------------------------
# CSVファイルを読み込む
# ----------------------------------------------------------------
filename = 'test.csv'
df = pd.read_csv(filename)

print('------------CSVファイル: {} を読み込み------------'.format(filename))
print(df)

# ----------------------------------------------------------------
# グラフを作って表示する
# ----------------------------------------------------------------
# print('グラフを作成・表示します')
# df.plot()            # 折れ線グラフを作る
# plt.show()           # グラフを表示する


# 読み込み時、index_col=0で名前の列をインデックスにする
df = pd.read_csv(filename, index_col=0)
print('------------０列目（名前の列）をインデックスに変更------------')
print(df)

df.plot.bar()            # 棒グラフを作る
plt.legend(loc="upper right")   # 凡例の位置を変える
plt.show()

"""
# 棒グラフ（水平）を作って表示する
df.plot.barh()
plt.legend(loc="lower left")
plt.show()

# 積み上げ棒グラフを作って表示する
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()

# 箱ひげグラフを作って表示する
df.plot.box()
plt.show()

# 面グラフを作って表示する
df.plot.area()
plt.legend(loc="lower right")
plt.show()

1行データであれば、
DataFrame(1行データ).plot.pie(labeldistance=中心からの距離)
で円グラフも作成できる
"""
