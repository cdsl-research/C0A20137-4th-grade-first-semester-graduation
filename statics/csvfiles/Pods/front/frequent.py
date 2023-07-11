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

# ヒストグラムを作成
plt.figure(figsize=(10, 6))
plt.hist(df['Value'], bins=10, alpha=0.5)

# グラフの設定
plt.title('Value Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# ティックラベルのフォントサイズを設定
plt.tick_params(axis='both', labelsize=15)

# グリッドを有効にする
plt.grid()

plt.savefig(f"{directory}/frequency.png")
