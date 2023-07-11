# import os
# import csv

# # CSVファイルが格納されているディレクトリ
# dir_path = './csv/Pods'

# # ディレクトリ内のすべてのCSVファイルを見つける
# csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

# # サービスごとのデータを格納する辞書
# data_dict = {}

# # 各CSVファイルに対して
# for csv_file in csv_files:
#     # ファイル名からサービス名とレプリカの識別名を抽出する
#     service_name, replica_name = csv_file[:-4].rsplit('-', 1)

#     # CSVファイルからデータを読み込む
#     with open(os.path.join(dir_path, csv_file), 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # ヘッダー行をスキップする

#         for row in reader:
#             # 行から値を取得
#             timestamp = row[0]
#             value = row[1]

#             # サービスごとにデータを追加する
#             name = service_name
#             if name not in data_dict:
#                 data_dict[name] = []
#             data_dict[name].append((timestamp, value, replica_name))

# # サービスごとに新しいCSVファイルを作成する
# for name, data in data_dict.items():
#     output_file = f"./csv/Services/{name}.csv"
#     with open(output_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Timestamp', 'Value', 'Pod'])

#         for row in data:
#             writer.writerow(row)

#     print(f"Created {output_file}")
import os
import csv

# CSVファイルが格納されているディレクトリ
dir_path = './csv/test'

# サービスごとのデータを格納する辞書
data_dict = {}

# ディレクトリ内のすべてのCSVファイルを見つける
csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

# 各CSVファイルに対して
for csv_file in csv_files:
    # ファイル名からサービス名とPod名を抽出する
    service_name = csv_file.rsplit('-', 1)[0]
    pod_name = csv_file.rsplit('-', 1)[-1][:-4]  # .csv拡張子を除く

    # CSVファイルからデータを読み込む
    with open(os.path.join(dir_path, csv_file), 'r') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップする

        for row in reader:
            # 行から値を取得
            timestamp = row[0]
            value = row[1]

            # サービスごとにデータを追加する
            if service_name not in data_dict:
                data_dict[service_name] = []
            data_dict[service_name].append((timestamp, value, pod_name))

# サービスごとに新しいCSVファイルを作成する
for service_name, data in data_dict.items():
    output_file = f"./csv/Services/{service_name}.csv"
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Value', 'Pod'])

        for row in data:
            writer.writerow(row)

    print(f"Created {output_file}")
