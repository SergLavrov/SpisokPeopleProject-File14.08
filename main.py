
# Список людей на проекте.
# Действия: Запись в файл(при выходе), чтение из файла(при запуске программы),
# Добавление человека на проект, удаление человека с проекта, получение списка людей на проекте,
# есть ли человек на проекте.
# В список людей должен храниться в алфавитном порядке.

import os
from functions import *

os.system('cls')

users = read_user_from_file()
print(sorted(users))

os.system('pause')
os.system('cls')

while True:
    choice = input_choice()

    if choice == '0':
        write_user_to_file(users)
        break

    elif choice == '1':
        add_user(users)

    elif choice == '2':
        remove_user(users)

    elif choice == '3':
        list_users(users)

    else:
        print('Invalid choice')

    os.system('pause')
    os.system('cls')

print('Goodbye')
