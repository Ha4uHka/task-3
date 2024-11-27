## functions - модуль для импорта функций для работы

# TODO import <зависимость из задания>
# TODO переименовать функции
import os

import shutil

def funk1(root_dir):
    image_paths = []
    for dir_name in os.listdir(root_dir):
        dir_path = os.path.join(root_dir, dir_name)
        if os.path.isdir(dir_path):
            for image_name in os.listdir(dir_path):
                image_path = os.path.join(dir_path, image_name)
                if os.path.isfile(image_path):
                    image_paths.append((image_name, image_path))
    return image_paths


def funk2(root_dir, image_paths):
    image_paths.sort(key=lambda x: x[0])
    for i, (image_name, image_path) in enumerate(image_paths):
        new_dir_name = str(i // 3 + 1)  # Номер новой папки
        new_dir_path = os.path.join(root_dir, new_dir_name)
        os.makedirs(new_dir_path, exist_ok=True)  # Создаем новую папку, если она не существует

        new_image_name = f'{i % 3 + 1}.jpg'  # Новое имя картинки
        new_image_path = os.path.join(new_dir_path, new_image_name)
        os.rename(image_path, new_image_path)  # Перемещаем картинку в новую папку