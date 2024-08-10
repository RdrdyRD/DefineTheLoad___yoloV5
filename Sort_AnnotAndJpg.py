import os
import shutil


dir = ('/home/rdrdyrd/WorkWork/Datasets/LoadType')
destination_directoryLabels = ('/home/rdrdyrd/WorkWork/Datasets/Dataset_Yolov5_DefineTheLoad/MainDataset/labels')
destination_directoryImages = ('/home/rdrdyrd/WorkWork/Datasets/Dataset_Yolov5_DefineTheLoad/MainDataset/images/')


# for root, dirs, files in os.walk(dir):
#     for file in files:
#         if not "txt" in file and not "jpg" in file:
#             os.rename(os.path.join(root, file), os.path.join(root, file)+'.jpg')
# counter = 0
# doppel_counter = 0
# new_uid = 0
# for root, dirs, files in os.walk(dir):
#     for file in files:
#         if 'txt' in file:
#
#             for roots1, dirs1, files1 in os.walk(dir):
#                 for file1 in files1:
#                     if 'jpg' in file1 and file[:-3] == file1[:-3]:
#                         uid = file1[:-3]
#                         if uid == new_uid:
#                             print(counter)
#                             print(uid)
#                             doppel_counter+=1
#                         new_file = shutil.copy(os.path.join(root, file), destination_directoryLabels + 'instance' + str(counter) +'.txt')
#                         # os.rename(new_file, 'instance' + str(counter) + '.txt')
#                         # print(new_file)
#                         new_file1 = shutil.copy(os.path.join(root, file1), destination_directoryImages + 'instance' + str(counter) +'.jpg')
#                         # os.rename(new_file1, 'instance' + str(counter) + '.jpg')
#                         # print(new_file1)
#                         counter+=1
#                         new_uid = file1[:-3]
# print(doppel_counter)
# print(counter)








for root, dirs, files in os.walk(destination_directoryLabels):

    for file in files:
        file_path = os.path.join(root, file)
        # Чтение содержимого файла
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()


        data = data.replace(',','')
        print(data)

        with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)

