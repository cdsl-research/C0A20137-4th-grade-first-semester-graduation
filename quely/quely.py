#CPU使用率を取得する
from prometheus_api_client import PrometheusConnect
from datetime import datetime
import pytz
import pandas as pd
import os

# Prometheusとの接続を確立
prom = PrometheusConnect(url="http://192.168.100.104:9090", disable_ssl=True)

# メトリクス名とnamespaceを指定
metric_name_usage = 'container_cpu_usage_seconds_total'
metric_name_limit = 'kube_pod_container_resource_limits_cpu_cores'
namespace = 'sock-shop'

# PromQLクエリを作成
query_usage = f'{metric_name_usage}{{namespace="{namespace}"}}'
query_limit = f'{metric_name_limit}{{namespace="{namespace}"}}'

# データを取得する期間を指定（タイムスタンプで指定）
start_time = datetime.fromtimestamp(1689055602, tz=pytz.UTC)
end_time = datetime.fromtimestamp(1689056204, tz=pytz.UTC)

# 時系列データを取得
usage_data = prom.custom_query_range(query=query_usage, start_time=start_time, end_time=end_time, step='1m')
limit_data = prom.custom_query_range(query=query_limit, start_time=start_time, end_time=end_time, step='1m')

# CPU使用量のメトリクスデータのDataFrameリストを作成
usage_df_list = []
for metric_item in usage_data:
    temp_df = pd.DataFrame(metric_item['values'], columns=['timestamp', 'value'])
    temp_df['timestamp'] = pd.to_datetime(temp_df['timestamp'], unit='s')
    temp_df['value'] = temp_df['value'].astype(float)

    # metricから必要なデータを追加
    temp_df['pod'] = metric_item['metric']['pod']
    temp_df['namespace'] = metric_item['metric']['namespace']
    
    usage_df_list.append(temp_df)

# 同様にCPU制限量のメトリクスデータのDataFrameリストを作成
limit_df_list = []
for metric_item in limit_data:
    temp_df = pd.DataFrame(metric_item['values'], columns=['timestamp', 'limit'])
    temp_df['timestamp'] = pd.to_datetime(temp_df['timestamp'], unit='s')
    temp_df['limit'] = temp_df['limit'].astype(float)

    # metricから必要なデータを追加
    temp_df['pod'] = metric_item['metric']['pod']
    temp_df['namespace'] = metric_item['metric']['namespace']
    
    limit_df_list.append(temp_df)

# 同一のpodについてCPU使用量と制限量をマージし、使用率を計算
for usage_df, limit_df in zip(usage_df_list, limit_df_list):
    # マージ（結合）
    merged_df = pd.merge(usage_df, limit_df, on=['timestamp', 'pod', 'namespace'])

    # CPU使用率を計算
    merged_df['usage_rate'] = merged_df['value'] / merged_df['limit'] * 100

    # PodごとにCSVファイルに書き込む
    merged_df[['timestamp', 'usage_rate', 'pod', 'namespace']].to_csv(f'./pod-cpu-usage/{merged_df["pod"].unique()[0]}_usage_rate.csv', index=False)

