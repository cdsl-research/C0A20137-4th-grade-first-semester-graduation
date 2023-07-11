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

# 1枚の図に複数のグラフを描画
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 12))  # 2行3列のサブプロットを作成

num_subplots = min(len(df['Pod']), 5)  # サブプロットの数を最大5個に制限する

for i, (pod, group) in enumerate(df.groupby('Pod')):
    if i >= num_subplots:
        break
    ax = axes[i // 3, i % 3]  # サブプロットの位置を取得
    ax.hist(group['Value'], bins=10, alpha=0.5)

    # グラフの設定
    ax.set_title(f'{pod}', fontsize=16)
    ax.set_xlabel('Cpu_usage', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)

    # ティックラベルのフォントサイズを設定
    ax.tick_params(axis='both', labelsize=12)

    # グリッドを有効にする
    ax.grid()

# 余白を調整
plt.tight_layout()

# 画像を保存
plt.savefig(f'{directory}/histogram.png')

plt.close()
