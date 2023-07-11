import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み（ヘッダー行をスキップする）
data = pd.read_csv('/home/c0a20137/csvfiles/container_cpu_usage_seconds_total.csv', skiprows=1, header=None, names=['timestamp', 'value', 'identifier'])

# timestamp列を日時型に変換（フォーマットを指定）
data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')

# identifilterごとにグラフを作成し保存
identifilters = data['identifier'].unique()
for identifilter in identifilters:
    filtered_data = data[data['identifier'] == identifilter]
    
    # グラフ描画
    plt.plot(filtered_data['timestamp'], filtered_data['value'])
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Time Series Graph - ' + identifilter)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # グラフをファイルに保存
    filename = identifilter.replace('/', '-') + '.png'  # ファイル名に含まれるスラッシュをハイフンに変換
    plt.savefig(f"/home/c0a20137/images/{filename}")
    plt.clf()  # プロットをクリア
