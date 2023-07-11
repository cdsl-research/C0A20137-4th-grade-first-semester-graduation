import pandas as pd
from prometheus_api_client import PrometheusConnect
from datetime import datetime, timedelta
import pytz

# Prometheusとの接続を確立
prom = PrometheusConnect(url="http://192.168.100.104:9090", disable_ssl=True)

# メトリクス名とnamespaceを指定
metric_name = 'container_cpu_usage_seconds_total'
namespace = 'sock-shop'

# PromQLクエリを作成
query = f'{metric_name}{{namespace="{namespace}"}}'


# データを取得する期間を指定（過去1時間とします）
# end_time = datetime.now() - timedelta(minutes=9)
# start_time = end_time - timedelta(hours=0.4)
start_time = datetime.fromtimestamp(1689080454, tz=pytz.UTC)
end_time = datetime.fromtimestamp(1689081456, tz=pytz.UTC)

# 時系列データを取得
metric_data = prom.custom_query_range(
    query=query, 
    start_time=start_time, 
    end_time=end_time,
    step='1m'  # 1分ごとのデータを取得
)

# データをpandas DataFrameに変換
data_frame = pd.json_normalize(metric_data, 'values', ['metric'])
data_frame.columns = ['timestamp', 'value', 'metric_info']
data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'], unit='s')
data_frame['value'] = data_frame['value'].astype(float)

# Extract pod from metric_info
data_frame['pod'] = data_frame['metric_info'].apply(lambda x: x.get('pod'))

# 'timestamp'と'pod'の列の値が重複している行を削除
data_frame = data_frame.drop_duplicates(subset=['timestamp', 'pod'])


# CSVファイルに書き込む
data_frame[['timestamp', 'value', 'pod']].to_csv('./container_cpu_usage_seconds_total.csv', index=False)
