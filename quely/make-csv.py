import csv

def create_csv_files(input_file):
    # 名前ごとのデータを格納する辞書
    data_dict = {}

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップする

        for row in reader:
            # 行から値を取得
            timestamp = row[0]
            value = row[1]
            name = row[2]

            # 名前ごとにデータを追加する
            if name not in data_dict:
                data_dict[name] = []

            # 同じ時刻のデータが既にある場合はスキップする
            if any(row[0] == timestamp for row in data_dict[name]):
                continue

            data_dict[name].append((timestamp, value))

    # 名前ごとのデータを時刻でソートする
    for name, data in data_dict.items():
        data_dict[name] = sorted(data, key=lambda x: x[0])

    # 名前ごとに新しいCSVファイルを作成する
    for name, data in data_dict.items():
        output_file = f"./csv/test/{name}.csv"
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Value'])

            for row in data:
                writer.writerow(row)

        print(f"Created {output_file}")

# 入力ファイル名を指定して関数を呼び出す
input_file = 'container_cpu_usage_seconds_total.csv'
create_csv_files(input_file)
