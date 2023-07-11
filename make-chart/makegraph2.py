import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
data = pd.read_csv('/home/c0a20137/csvfiles/container_cpu_usage_seconds_total.csv')

# ポッドごとにグラフを作成
pod_list = data['pod'].unique()
for pod in pod_list:
    filtered_data = data[data['pod'] == pod]
    
    # グラフの作成
    plt.plot(filtered_data['timestamp'], filtered_data['value'])
    plt.xlabel('timestamp')
    plt.ylabel('value')
    plt.title(f'Time Series Graph - {pod}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # グラフの保存
    filename = f'{pod}.png'
    plt.savefig(f"/home/c0a20137/images/{filename}")
    plt.clf()  # グラフをクリア
    
    print(f'グラフをファイル "{filename}" に保存しました。')
