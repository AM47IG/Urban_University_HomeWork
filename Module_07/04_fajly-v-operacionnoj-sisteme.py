import os
import time

directory = 'C:/Users/AM47IG/Downloads/Telegram Desktop'
directory = os.path.normpath(directory)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, \nПуть: {filepath}, \nРазмер: {filesize} байт, \nВремя изменения: {formatted_time}, \nРодительская директория: {parent_dir}')
        print('*' * 20)