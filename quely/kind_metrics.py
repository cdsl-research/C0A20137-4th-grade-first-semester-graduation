import pandas as pd
from prometheus_api_client import PrometheusConnect
from datetime import datetime, timedelta

# Prometheusとの接続を確立
prom = PrometheusConnect(url="http://192.168.100.104:9090", disable_ssl=True)

# メトリクス名とnamespaceを指定
metrics = ['container_cpu_usage_seconds_total', 'metric_2', 'metric_3']  # 関心のあるすべてのメトリクス名をリストに追加します
namespace = 'sock-shop'

for metric_name in metrics:
    # PromQLクエリを作成
    query = f'{metric_name}{{namespace="{namespace}"}}'

    # データを取得する期間を指定（過去1時間とします）
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)

    # 時系列データを取得
    metric_data = prom.custom_query_range(
        query=query, 
        start_time=start_time, 
        end_time=end_time,
        step='1m'  # 1分ごとのデータを取得
    )

    # データが存在する場合だけDataFrameに変換
    if metric_data:
        # データをpandas DataFrameに変換
        data_frame = pd.json_normalize(metric_data, 'values', ['metric'])
        data_frame.columns = ['timestamp', 'value', 'metric_info']
        data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'], unit='s')
        data_frame['value'] = data_frame['value'].astype(float)

        # Extract pod from metric_info
        data_frame['pod'] = data_frame['metric_info'].apply(lambda x: x.get('pod'))
        filtered_data_frame = data_frame[data_frame['pod'].str.contains('front')]

        # CSVファイルに書き込む
        filtered_data_frame[['timestamp', 'value', 'pod']].to_csv(f'~/csvfiles/{metric_name}.csv', index=False)
    else:
        print(f"No data for metric {metric_name}")
