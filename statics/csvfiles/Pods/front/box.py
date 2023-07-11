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

# Podごとにデータをフィルタリングして箱ひげ図を作成
plt.figure(figsize=(10, 6))
df.boxplot(column='Value', by='Pod')

# グラフの設定
plt.xlabel('Pod name', fontsize=20)
plt.ylabel('Cpu_usage', fontsize=20)

# ティックラベルのフォントサイズを設定
plt.tick_params(axis='both', labelsize=15)

# グリッドを有効にする
plt.grid()

# 図のレイアウトを自動調整
plt.tight_layout()

plt.savefig(f"{directory}/box.png")
