import pandas as pd
import matplotlib.pyplot as plt
import os

# CSVデータの読み込み
data_frame = pd.read_csv('./container_cpu_usage_seconds_total.csv')

# 'timestamp'列をdatetimeオブジェクトに変換
data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'])

# ポッド名ごとにデータフレームを分割
grouped = data_frame.groupby('pod')

# 出力ディレクトリの指定
output_dir = '/home/c0a20137/images/'

# 各ポッドごとにグラフを作成
for pod_name, group_df in grouped:
    # グラフをプロットする前に時刻でソート
    group_df = group_df.sort_values('timestamp')

    plt.figure(figsize=(10, 6))
    plt.plot(group_df['timestamp'], group_df['value'])
    plt.title(f'CPU Usage for {pod_name}')
    plt.xlabel('Timestamp')
    plt.ylabel('CPU Usage')
    plt.grid(True)
    filename = f"{pod_name.replace('/', '_')}_cpu_usage.png"  # '/'はファイル名に使用できないため'_'に置き換え
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()
