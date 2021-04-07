#Валидатор паролей:
# пароле должно быть не менее 8 символов
#В пароле должны быть числа
#В пароле необходима минимум одна заглавная буква

import re

def validate():
    while True:
        password = input("Введиде пароль: ")
        if len(password) < 8:
            print("В пароле должно быть не менее 8 символов")
        elif re.search('[0-9]',password) is None:
            print("В пароле должны быть числа")
        elif re.search('[A-Z]',password) is None:
            print("В пароле необходима минимум одна заглавная буква")
        else:
            print("Отличный пароль")
            break

validate()