import os
from shutil import copy
from sys import argv

SourcePath = '.'
if(len(argv) > 1):
    SourcePath = argv[1]


files = os.listdir(SourcePath)
listOfFiles = []

for i in files:
    fileSize = os.path.getsize(f'{SourcePath}/{i}')
    if fileSize <= 2048:
        listOfFiles.append(i)

if len(listOfFiles) != 0:
    try:
        os.mkdir("small")
    except FileExistsError:
        print("Директория уже существует")

    for i in listOfFiles:
        fileSourcePath = f'{SourcePath}/{i}'
        fileDestinationPath = "small/" + str(i)
        copy(fileSourcePath, fileDestinationPath)
else:
    print("Таких файлов нет")