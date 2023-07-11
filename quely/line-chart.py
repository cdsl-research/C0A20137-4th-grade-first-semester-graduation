# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# # CSVファイルが格納されているディレクトリ
# dir_path = './csv/test'

# # ディレクトリ内のすべてのCSVファイルを見つける
# csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

# # 保存するグラフのディレクトリ
# save_dir = './graphs'
# os.makedirs(save_dir, exist_ok=True)

# # 各CSVファイルに対して
# for csv_file in csv_files:
#     # CSVファイルからデータを読み込む
#     df = pd.read_csv(os.path.join(dir_path, csv_file), header=0)
    
#     # 列名を設定
#     timestamp_column = df.columns[0]
#     value_column = df.columns[1]
    
#     # タイムスタンプをdatetime型に変換
#     df[timestamp_column] = pd.to_datetime(df[timestamp_column], format='%Y-%m-%d %H:%M:%S')

#     # 折れ線グラフを描く
#     plt.figure(figsize=(10,6))  # グラフのサイズを設定
#     plt.plot(df[timestamp_column], df[value_column], label='CPU Usage')

#     # グラフのタイトルと軸ラベルを設定
#     plt.title(csv_file[:-4])  # ファイル名から".csv"を取り除いてタイトルにする
#     plt.xlabel('Time')
#     plt.ylabel('CPU Usage')

#     # 凡例を表示
#     plt.legend()

#     # グラフを保存
#     plt.savefig(os.path.join(save_dir, csv_file[:-4] + '.png'))

#     # グラフをクリア
#     plt.clf()
# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# # CSVファイルが格納されているディレクトリ
# dir_path = './csv/Services'

# # ディレクトリ内のすべてのCSVファイルを見つける
# csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

# # 保存するグラフのディレクトリ
# save_dir = '/home/c0a20137/software/statics/images/line'
# os.makedirs(save_dir, exist_ok=True)

# # 各CSVファイルに対して
# for csv_file in csv_files:
#     # CSVファイルからデータを読み込む
#     df = pd.read_csv(os.path.join(dir_path, csv_file), header=0)
    
#     # 列名を設定
#     timestamp_column = df.columns[0]
#     value_column = df.columns[1]
    
#     # タイムスタンプをdatetime型に変換
#     df[timestamp_column] = pd.to_datetime(df[timestamp_column], format='%Y-%m-%d %H:%M:%S')

#     # 経過時間を計算
#     df['Elapsed Time'] = (df[timestamp_column] - df[timestamp_column].iloc[0]).dt.total_seconds()

#     # 折れ線グラフを描く
#     plt.figure(figsize=(10,6))  # グラフのサイズを設定
#     plt.plot(df['Elapsed Time'], df[value_column], label='CPU Usage')

#     # グラフのタイトルと軸ラベルを設定
#     plt.title(csv_file[:-4])  # ファイル名から".csv"を取り除いてタイトルにする
#     plt.xlabel('Elapsed Time (s)')
#     plt.ylabel('CPU Usage')

#     # 横軸の範囲を0から1000秒に制限
#     plt.xlim(0, 1000)

#     # 凡例を表示
#     plt.legend()

#     # グラフを保存
#     plt.savefig(os.path.join(save_dir, csv_file[:-4] + '.png'))

#     # グラフをクリア
#     plt.clf()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# データの読み込み
data = pd.read_csv('./csv/Services/catalogue-6479dbb5bd.csv')

# データの前処理
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['Elapsed'] = (data['Timestamp'] - data['Timestamp'].min()).dt.total_seconds()

# 横軸の範囲を設定
x_min = 0
x_max = 1000

# Podごとにグラフを作成
for pod in data['Pod'].unique():
    # Podごとのデータを抽出
    pod_data = data[data['Pod'] == pod]

    # グラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(pod_data['Elapsed'], pod_data['Value'])
    plt.title(f'Pod: {pod}')
    plt.xlabel('Elapsed Time (seconds)')
    plt.ylabel('Value')
    plt.xlim(x_min, x_max)
    plt.grid()

    # 横軸の目盛りを設定
    plt.xticks(np.arange(x_min, x_max+1, 100))

    # グラフを表示
    plt.savefig("./non.png")
