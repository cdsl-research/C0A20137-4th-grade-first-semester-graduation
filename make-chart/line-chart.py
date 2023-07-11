import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('container_cpu_usage_seconds_total.csv', header=None, names=['Timestamp', 'Value', 'Label'], skiprows=1)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%d %H:%M:%S')

unique_labels = data['Label'].unique()  # 一意のLabelを取得

for label in unique_labels:
    filtered_data = data[data['Label'] == label]  # Labelに基づいてデータをフィルタリング
    filtered_data = filtered_data.sort_values('Timestamp')  # タイムスタンプでソート
    timestamps = filtered_data['Timestamp']
    values = filtered_data['Value']

    plt.figure(figsize=(10, 6))  # グラフのサイズを指定
    plt.plot(timestamps, values)  # プロット

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'Line Graph - {label}')
    plt.xticks(rotation=45)
    
    plt.savefig(f'../statics/images/by-pod-cpu/{label}_line_graph.png')  # グラフ画像を保存
    plt.close()  # メモリ解放のためにグラフを閉じる
