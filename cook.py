import os
import time
from pprint import pprint
import json
from glob import glob

# cook_data={
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

file_path = "recipes.txt"


def make_cook_book(file_path):
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as src_file:
        last_key = ''
        for line in src_file:
            line = line.strip()
            if line.isdigit():
                continue
            elif line and '|' not in line:
                cook_book[line] = []
                last_key = line
            elif line and '|' in line:
                name, qt, msure = line.split(" | ")
                cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))

    print(cook_book)


def r_bk(file_path):
    c_b = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            count = int(f.readline().strip())

            ingredients = []

            for _ in range(count):
                ingredient_info = f.readline().strip().split('|')
                ingredient = {
                    'ingredient_name': ingredient_info[0].strip(),
                    'quantity': int(ingredient_info[1].strip()),
                    'measure': ingredient_info[2].strip()
                }
                ingredients.append(ingredient)

            c_b[dish_name] = ingredients

            f.readline()

    return c_b


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:
        if dish_name in c_b:
            for ings in c_b[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


def rewrite_file():
    outout_file = "rewrite_file.txt"
    comparsion_list = {}

    with open (outout_file, 'w'):
        pass
    for files_read in glob('dir3dz/*.txt'):
        name_read = files_read.split('\\')[1]
        file_path = os.path.join(os.getcwd(), files_read)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_read = f.readlines()
        comparsion_list[name_read] = len(file_read)

    comparsion_list = sorted(comparsion_list.items(), key=lambda item: item[1])

    for item in comparsion_list:
        name = 'dir3dz/' + item[0]
        file_path = os.path.join(os.getcwd(), name)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_write = f.readlines()
        with open(outout_file, 'a', encoding='utf-8') as f_total:
            f_total.write(item[0] + '\n')
            f_total.write(str(len(file_write)) + '\n')
            f_total.writelines(file_write)
            f_total.write('\n')
    return

if __name__ == '__main__':
    filename = "book_cook.txt"
    c_b = r_bk(file_path)
    print('Задание 1------------------------------------------------------------')
    time.sleep(1)
    print(c_b)
    print('Задание 2------------------------------------------------------------')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))
    time.sleep(2)
    print('Задание 3------------------------------------------------------------')
    rewrite_file()