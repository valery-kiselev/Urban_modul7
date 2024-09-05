import os
from time import strftime, localtime

directory = '.'
for i in os.walk('.'):
    files = [f for f in os.listdir() if os.path.isfile(f)]
    dir = [d for d in os.listdir() if os.path.isdir(d)]
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



