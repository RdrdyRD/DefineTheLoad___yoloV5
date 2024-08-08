import os
import shutil


dir = ('C:/Users/RD/WorkWork/Prog/Datasets/8.3.2024new/d/d/Datase/sorted')
destination_directory = ('C:/Users/RD/WorkWork/Prog/Datasets/yolov5/validation/labels')
#
# for root, dirs, files in os.walk(dir):
#     for file in files:
#         if "txt" in file:
#             shutil.move(os.path.join(root, file), destination_directory)

# for root1, dirs1, files1 in os.walk(destination_directory):
#     for file1 in files1:
#         for root, dirs, files in os.walk(dir):
#             for file in files:
#                 if str(file1[1:13]) in file:
#                     shutil.move(os.path.join(root, file), destination_directory)
# забыл добавить jpg

# for root, dirs, files in os.walk(destination_directory):
#     for file in files:
#         os.rename(os.path.join(root, file), os.path.join(root,file)+'.jpg')


for root, dirs, files in os.walk(destination_directory):

    for file in files:
        file_path = os.path.join(root, file)
        # Чтение содержимого файла
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()


        data = data.replace(',','')
        print(data)

        with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)


