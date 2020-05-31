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

# ----------------------------------------------------------------
# 個別のデータをグラフで表示させる
# ----------------------------------------------------------------
# 国語（列）の棒グラフを作って表示する
# 国語列だけ表示するには
print(df[['国語']])

"""
df_kokugo = df[['国語']]
df_kokugo.plot.bar()            # 棒グラフを作る
plt.legend(loc="upper right")   # 凡例の位置を変える
plt.show()

# 国語と数学の棒グラフを作って表示する
df[['国語', '数学']].plot.bar()
plt.legend(loc="upper right")
plt.show()
"""
# C子(の行)の棒グラフを作って表示する
# C子(の行)だけ表示するには
print(df.loc[['C子']])

df.loc['C子'].plot.bar()
plt.legend(loc="upper right")
plt.show()


# C子の円グラフを作って表示する
df.loc['C子'].plot.pie(labeldistance=0.6)
plt.legend(loc="upper right")
plt.show()
