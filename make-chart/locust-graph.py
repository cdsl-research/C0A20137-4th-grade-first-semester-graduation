import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# CSVファイルを読み込む
df = pd.read_csv('./output_stats_history.csv')

# 'Timestamp'列を日時型に変換（ここではUNIXタイムスタンプと仮定）
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

# 経過時間を計算
df['Elapsed Time'] = (df['Timestamp'] - df['Timestamp'].iloc[0]).dt.total_seconds()

# 'Elapsed Time'と'Requests/s'をプロット
plt.figure(figsize=(10, 6))  # 縦横比を10:6に設定

# グラフのタイトル、軸ラベル、横軸の表示間隔とラベル、そして縦軸のラベルのフォントサイズを個別に設定
plt.plot(df['Elapsed Time'], df['Requests/s'])

plt.xlabel('Elapsed Time (s)', fontsize=20)  # x軸ラベルのフォントサイズを20に設定
plt.ylabel('Requests/s', fontsize=20)  # y軸ラベルのフォントサイズを20に設定

plt.tick_params(axis='both', labelsize=15)  # x軸とy軸のティックラベルのフォントサイズを15に設定

plt.grid()

# 図のレイアウトを自動調整
plt.tight_layout()

# グラフを表示
plt.savefig('./loadtest.png')
