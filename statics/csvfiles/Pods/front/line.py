import os
import pandas as pd
import matplotlib.pyplot as plt

# ディレクトリパスとファイル名を指定
directory = '/home/c0a20137/software/quely/csv/Services'  # ディレクトリのパスを指定
filename = 'front-end-7f5c844b4c.csv'  # ファイル名を指定

# CSVファイルのパスを作成
file_path = os.path.join(directory, filename)

# CSVファイルを読み込む
df = pd.read_csv(file_path)

# Timestamp列を日時型に変換
df['Timestamp'] = pd.to_datetime(df['Timestamp'])


# 最初のタイムスタンプを基準として経過時間を計算
df['TimeElapsed'] = (df['Timestamp'] - df['Timestamp'].min()).dt.total_seconds()

# Podごとにグループ化して折れ線グラフを作成
plt.figure(figsize=(10, 6))
for pod, group in df.groupby('Pod'):
    plt.plot(group['TimeElapsed'], group['Value'], label=pod)

# グラフの設定
plt.xlabel('Elapsed Time (s)', fontsize=20)
plt.ylabel('Cpu_usage', fontsize=20)
plt.legend()

# ティックラベルのフォントサイズを設定
plt.tick_params(axis='both', labelsize=15)

# グリッドを有効にする
plt.grid()

# 図のレイアウトを自動調整
plt.tight_layout()

plt.savefig(f"{directory}/front.png")
