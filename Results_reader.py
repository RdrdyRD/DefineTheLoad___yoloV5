import pandas as pd

# Загрузка данных из файла result.csv
file_path = '/home/rdrdyrd/WorkWork/Projects/DefineTheLoad___yoloV5/yolov5/runs/train/exp/results.csv'  # Укажите путь к вашему файлу
df = pd.read_csv(file_path)

# Вывод первых 5 строк данных
print(df.head())