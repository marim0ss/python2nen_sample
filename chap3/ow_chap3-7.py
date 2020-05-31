#coding: UTF-8
import pandas as pd

# ----------------------------------------------------------------
# CSVファイルを読み込む
# ----------------------------------------------------------------
filename = 'test.csv'
df = pd.read_csv(filename)

print('------------CSVファイル: {} を読み込み------------'.format(filename))
print(df)
# print('データの件数    ＝', len(df))
# print('項目名(ヘッダー)＝', df.columns.values)
# print('インデックス(左列の番号)＝', df.index.values)

# ----------------------------------------------------------------
# 条件に合うデータを抽出する
# df = [df['列'] を使った条件 ]
#    国語の列が90点以上の行を抽出する
#    df = [df['国語'] >= 90 ]
# ----------------------------------------------------------------
print('------------数学の列が90点以上の行を抽出------------')
df_math = df[df['数学'] >= 90]
print(df_math)

# ----------------------------------------------------------------
# 集計（最大値、最小値、平均値、中央値、合計など）をして表示
# ----------------------------------------------------------------
print('国語の最高点は：', df['国語'].max())
print('国語の最低点は：', df['国語'].min())

print('数学の平均値は：', df['数学'].mean())
print('数学の中央値は：', df['数学'].median())

print('英語の合計は：', df['英語'].sum())