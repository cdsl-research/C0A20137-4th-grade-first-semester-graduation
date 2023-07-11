# from datetime import datetime
# import pytz

# # Prometheusとの接続を確立
# prom = PrometheusConnect(url="http://192.168.100.104:9090", disable_ssl=True)

# # メトリクス名とnamespaceを指定
# metric_name = 'container_cpu_usage_seconds_total'
# namespace = 'sock-shop'

# # PromQLクエリを作成
# query = f'rate({metric_name}{{namespace="{namespace}"}}[1m]) * 100'

# # データを取得する期間を指定（タイムスタンプで指定）
# start_time = datetime.fromtimestamp(1688354053, tz=pytz.UTC)
# end_time = datetime.fromtimestamp(1688355156, tz=pytz.UTC)

# # 時系列データを取得
# metric_data = prom.custom_query_range(
#     query=query, 
#     start_time=start_time, 
#     end_time=end_time,
#     step='1m'  # 1分ごとのデータを取得
# )

# # 各メトリクスデータのDataFrameリストを作成
# df_list = []
# for metric_item in metric_data:
#     temp_df = pd.DataFrame(metric_item['values'], columns=['timestamp', 'value'])
#     temp_df['timestamp'] = pd.to_datetime(temp_df['timestamp'], unit='s')
#     temp_df['value'] = temp_df['value'].astype(float)
    
#     # metricから必要なデータを追加
#     temp_df['pod'] = metric_item['metric']['pod']
#     temp_df['namespace'] = metric_item['metric']['namespace']
    
#     df_list.append(temp_df)

# # すべてのデータフレームを結合
# data_frame = pd.concat(df_list)

# # CSVファイルに書き込む
# data_frame[['timestamp', 'value', 'pod', 'namespace']].to_csv('./container_cpu_usage_rate.csv', index=False)
