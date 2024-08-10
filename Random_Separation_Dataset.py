import os
import shutil
from sklearn.model_selection import train_test_split


dataset_dir = '/home/rdrdyrd/WorkWork/Datasets/Dataset_Yolov5_DefineTheLoad/MainDataset'
images_dir = os.path.join(dataset_dir, 'images')
labels_dir = os.path.join(dataset_dir, 'labels')
output_dirs = {
    'train': os.path.join(dataset_dir, 'train'),
    'val': os.path.join(dataset_dir, 'val'),
    'test': os.path.join(dataset_dir, 'test')
}
split_ratios = [0.8, 0.1, 0.1]
random_seed = 42


for key, output_dir in output_dirs.items():
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)


image_files = sorted([f for f in os.listdir(images_dir) if f.endswith('.jpg')])
label_files = sorted([f for f in os.listdir(labels_dir) if f.endswith('.txt')])


assert len(image_files) == len(label_files), "Количество изображений и меток должно совпадать"

# Разделяем на train и временный (val + test)
train_images, temp_images, train_labels, temp_labels = train_test_split(
    image_files, label_files, test_size=(split_ratios[1] + split_ratios[2]), random_state=random_seed)

# Разделяем временный на val и test
val_images, test_images, val_labels, test_labels = train_test_split(
    temp_images, temp_labels, test_size=split_ratios[2] / (split_ratios[1] + split_ratios[2]), random_state=random_seed)

# Функция для копирования файлов
def copy_files(file_list, src_dir, dst_dir):
    for file_name in file_list:
        shutil.copy(os.path.join(src_dir, file_name), os.path.join(dst_dir, file_name))

# Копируем файлы
copy_files(train_images, images_dir, os.path.join(output_dirs['train'], 'images'))
copy_files(train_labels, labels_dir, os.path.join(output_dirs['train'], 'labels'))

copy_files(val_images, images_dir, os.path.join(output_dirs['val'], 'images'))
copy_files(val_labels, labels_dir, os.path.join(output_dirs['val'], 'labels'))

copy_files(test_images, images_dir, os.path.join(output_dirs['test'], 'images'))
copy_files(test_labels, labels_dir, os.path.join(output_dirs['test'], 'labels'))

print("Датасет успешно разбит на train, val и test с использованием seed!")