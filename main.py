## main стартовый модуль проекта
from functions import funk1, funk2
import os

root_dir = f"{os.getcwd()}/data/"

image_paths = funk1(root_dir)
funk2(root_dir, image_paths)
