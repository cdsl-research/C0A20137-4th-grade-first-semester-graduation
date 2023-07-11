import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルを読み込む
data_frame = pd.read_csv('./container_cpu_usage_seconds_total.csv', parse_dates=['timestamp'])
df = pd.read_csv('./output_stats_history.csv')

# 'Timestamp'列を日時型に変換（ここではUNIXタイムスタンプと仮定）
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

# 新しいfigureを作成
fig, ax1 = plt.subplots(figsize=(10, 6))

# ax1に対して、同時刻で存在しているpod名の個数を描画
pod_counts = data_frame.groupby('timestamp')['pod'].nunique()
ax1.bar(pod_counts.index, pod_counts, label='Number of Pods', alpha=0.6)
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Number of Pods')

# ax2はax1と同じx軸を共有し、y軸は異なる
ax2 = ax1.twinx()
ax2.plot(df['Timestamp'], df['Requests/s'], color='orange', label='Requests/s')
ax2.set_ylabel('Requests/s')

# 各プロットのラベルからレジェンドを作成
fig.legend(loc='upper left', bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# グラフのタイトルを設定
plt.title('Number of Pods and Requests per Second over Time')

plt.grid()
plt.savefig('./combined_graph.png')
