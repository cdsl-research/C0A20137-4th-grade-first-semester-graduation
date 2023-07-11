#メトリクス一覧を取得してCSVファイルへ出力
import requests
from datetime import datetime, timedelta
import json
import pandas as pd

# PrometheusのURL
url = "http://192.168.100.104:9090"

# データを取得する期間を指定（過去1時間とします）
end_time = datetime.now()
start_time = end_time - timedelta(hours=1)

# UNIXタイムスタンプに変換
end_time_unix = end_time.timestamp()
start_time_unix = start_time.timestamp()

# APIエンドポイントを作成。ここでは、特定のnamespaceのすべてのメトリクスを選択します。
api_endpoint = f"{url}/api/v1/series?match[]={{namespace=\"sock-shop\"}}&start={start_time_unix}&end={end_time_unix}"

# APIリクエストを送信
response = requests.get(api_endpoint)

# レスポンスをJSON形式で保存
data = response.json()

# データをpandas DataFrameに変換
df = pd.json_normalize(data['data'])

# 必要なカラムだけを選択して新たなDataFrameを作成
df_filtered = df[['pod', '__name__']]

# NaNを含む行を削除
df_filtered = df_filtered.dropna()

# CSVファイルに出力
df_filtered.to_csv('./metrics.csv', index=False)

# '__name__'列のユニークな値を取得
unique_metrics = df['__name__'].unique()

# データフレームに変換
unique_metrics_df = pd.DataFrame(unique_metrics, columns=['__name__'])

# CSVファイルに出力
unique_metrics_df.to_csv('~/software/statics/images/kind-metrics/2unique_metrics.csv', index=False)
