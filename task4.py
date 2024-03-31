import os

file_paths = ['1.txt', '2.txt', '3.txt'] #Пути в файлам

file_contents = {}

#Читаем содержимое каждого файла
for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents[file_path] = lines


#Записываем результат в новый файл
with open('5.txt', 'w', encoding='utf-8') as file5:
    #Проходим по каждому файлу и его содержимому
    for file_path, lines in file_contents.items():
        # Записываем имя файла
        file5.write(file_path + '\n')
        #Записываем количество строк
        num_lines = len(lines)
        file5.write(str(num_lines) + '\n')
        # Записываем содержимое файла
        file5.writelines(lines)
        file5.write('\n\n')

