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

# ディレクトリが存在しない場合は作成する
if not os.path.exists(directory):
    os.makedirs(directory)

# 散布図を作成
plt.figure(figsize=(10, 6))  # 図のサイズを指定
plt.scatter(df['Timestamp'], df['Value'], s=10, alpha=0.5)

# グラフの設定
plt.xlabel('Timestamp', fontsize=14)
plt.ylabel('Value', fontsize=14)

# ティックラベルのフォントサイズを設定
plt.tick_params(axis='both', labelsize=12)

# グリッドを有効にする
plt.grid()

# 図のレイアウトを自動調整
plt.tight_layout()

# 画像を保存
save_path = os.path.join(directory, 'scatter.png')
plt.savefig(save_path)

plt.show()
