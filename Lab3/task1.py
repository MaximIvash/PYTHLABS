from sys import argv
from pathlib import Path
import numpy as np
from skimage import transform, io, color, filters


def menu():
    while True:
        print("пожалуйста, выберите преобразование для ваших jpg-файлов:\n"
              "1 - поверните изображение на 45 градусов\n"
              "2 - искажение\n"
              "3 - измените размер до 100х100\n"
              "4 - создайте гауссовский фильтр\n"
              "5 - сделать изображение серым\n"
              "6 - сложная трансформация\n")
        ans = int(input())
        if ans >= 1 & ans <= 6:
            return ans
        else:
            print("Неправильный номер! Пробуйте снова")
            ans = int(input())

def transformations(image, caseMode):
    if caseMode == 1:
        rotated = transform.rotate(image, angle = 45)
        return rotated

    elif caseMode == 2:
        tform = transform.SimilarityTransform(translation=(0, -100))
        warped = transform.warp(image, tform)
        return warped

    elif caseMode == 3:
        resized = transform.resize(image,(100,100))
        return resized

    elif caseMode == 4:
        gauss = filters.gaussian(image)
        return gauss

    elif caseMode == 5:
        colored = color.rgb2gray(image)
        return colored

    elif caseMode == 6:
        complex = transform.rotate(image, angle = 90)
        tform = transform.SimilarityTransform(translation=(50, -50))
        complex1 = transform.warp(complex, tform)
        complex2 = color.rgb2gray(complex1)
        return complex2



def main():
    if len(argv) == 2:
        path = Path(argv[1])
    else:
        print("Вы должны ввести путь к вашей директории!")
    mode = menu()

    for dir in path.iterdir():
        pictures = io.imread_collection(f"{dir}/*.jpg")
        num = len(pictures)
        if(len(pictures) != 0):
            for img in pictures:
                transformed = transformations(img,mode)
                io.imsave(f'{dir}/{num}.jpg', (transformed * 255).astype(np.uint8))
                num+=1

    print("Успешно")

main()