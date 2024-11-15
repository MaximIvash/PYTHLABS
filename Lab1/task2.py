import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default='.')
parser.add_argument('--files', nargs='*', default='')

parserArgs = parser.parse_args()
sourcePath = parserArgs.dirpath
files = parserArgs.files

existFiles = []
notExistFiles = []
dirFiles = os.listdir(sourcePath)

if(len(files) != 0):
    for file in files:
        check = 0
        for exist in dirFiles:
            if (file == exist):
                check = 1
                break
        if (check):
            existFiles.append(file)
        else:
            notExistFiles.append(file)

    with open('exist.txt', 'w') as exist, open('notExist.txt', 'w') as notExist:
        print("exist files:")
        for i in existFiles:
            print(f'{i}')
            exist.write(f'{i}\n')

        print("not exist files:")
        for i in notExistFiles:
            print(f'{i}')
            notExist.write(f'{i}\n')

else:
    numOfSourcesFiles = len(dirFiles)
    sum = 0
    for i in dirFiles:
        sum += os.path.getsize(f'{sourcePath}/{i}')
    print(f'Эта директория содержит {numOfSourcesFiles} файла и имеет общий размер: {sum} байт')