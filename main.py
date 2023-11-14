from PIL import Image
from filters import DarkFilter, BrightFilter, InverseFilter
import os

def main():
    filter_names = [
        "Увеличить яркость",
        "Уменьшить яркость",
        "Инверсия"
    ]

    filters = [
        BrightFilter(),
        DarkFilter(),
        InverseFilter()
    ]

    print("Добро пожаловать")

    is_finished = False
    while not is_finished:
        path = input("Введите путь к файлу >>> ")

        while not os.path.exists(path):
            path = input("Файл не найден. Попробуйте еще раз >>> ")

        img = Image.open(path).convert('L')

        print("Какой фильтр хотите применить >>> ?")

        for i in range(len(filter_names)):
            print(f'{i} - {filter_names[i]}')

        choice = input("Выберите фильтр (введите номер): >>> ")

        while not choice.isdigit() or int(choice) >= len(filters):
            choice = input("Некорректный ввод. Попробуйте еще раз >>> ")

        filt = filters[int(choice)]
        img = filt.apply_to_image(img)

        img.show()
        answer = input("Еще раз? (да/нет): ")

        while answer != 'да' and answer != 'нет':
            answer = input("Некорректный ввод. Попробуйте еще раз >>> ")

        is_finished = answer == 'нет'

if name == "main":
    main()