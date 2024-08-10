import cv2
import os
import json


dir = ('C:/Users/RD/WorkWork/Prog/Datasets/yolov5/validation/labels/')


for root, dirs, files in os.walk(dir):
    for file in files:
        if 'txt' in file:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                # print(content)
                data = json.loads(content)
                # print(data)
                class_name = data['class']
                height = data['rect']['Height']
                top_left_x = data['rect']['TopLeftX']
                top_left_y = data['rect']['TopLeftY']
                width = data['rect']['Width']
                # print(class_name,height,top_left_y)
                x_center = (top_left_x + width / 2) / 1536
                y_center = (top_left_y + height / 2) / 1536
                heightN = height / 1536
                widthN = width / 1536
                if class_name == 'sand':
                    temp_clas = 2

                if class_name == 'gravel':
                    temp_clas = 1

                if class_name == 'empty':
                    temp_clas = 0
                new_data = f"{temp_clas, x_center, y_center, widthN, heightN}"
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_data)



