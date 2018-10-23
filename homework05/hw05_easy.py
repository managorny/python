# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#Создание
import os

def actionWithDirectory(actionFail, actionSuccess, actionFunction):
    dirs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cwd = os.getcwd()
    for value in dirs:
        a = value
        myDir = "dir_"
        path = "%s/%s%s" % (cwd, myDir, a)
        try:
            actionFunction(path)
        except OSError: 
            print("%s директорию %s%s не удалось" % (actionFail, myDir, a))
        else:
            print("%s Директория %s%s создана" % (actionSuccess, myDir, a))

actionWithDirectory("Создать", "создана", os.mkdir)

#Удаление
actionWithDirectory("Удалить", "удалена", os.removedirs)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def showDir():
    cwd = os.getcwd()
    path = "%s" % cwd
    print(os.listdir(path))

showDir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import sys
import shutil

def copyFile():
    path = sys.argv[0]
    copy = "%s - copy.py" % path
    shutil.copyfile(path, copy)
    print("Копия создана по адресу:", copy)

copyFile()
