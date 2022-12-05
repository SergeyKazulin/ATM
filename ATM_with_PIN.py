import random
import datetime
import pwinput


def main():
    print('Добро пожаловать в банковскую систему. ATM.')
    name_list, card_list, pin_list, balance_list = read_file()
    option = 0
    while option != 5:
        #print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print('\nВЫБЕРИТЕ НЕОБХОДИМУЮ ВАМ ОПЕРАЦИЮ.')
        print()
        # вывод на дисплей меню
        atm_menu = ['1. Остаток На Счете.', '2. Снять Деньги.', '3. Положить Деньги.', '4. Сменить PIN код.', '5. Выход']
        #print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

        for option in atm_menu:
            print(option)
        user_input = False

       # validation - проверка пользовательского ввода
        while not user_input:
            try:
                option = int(input('Пожалуйста выберите необходимую операцию, от 1 до 5: '))
                if 0 < option < 6:
                    user_input = True
                else:
                    print('Пожалуйста выберите номер операции болбше 0, но меньше 6: ')
                    for option in atm_menu:
                        print(option)
            except:
                print('\nERROR!!! Пожалуйств введите номер операции от 1 до 5: ')
                for option in atm_menu:
                    print(option)
                    
        match option:
            case 1:
                name_list, card_list, pin_list, balance_list = balance_account(name_list, card_list, pin_list, balance_list)
            case 2:
                name_list, card_list, pin_list, balance_list = credit(name_list, card_list, pin_list, balance_list)
            case 3:
                name_list, card_list, pin_list, balance_list = deposit(name_list, card_list, pin_list, balance_list)
            case 4:
                name_list, card_list, pin_list, balance_list = change_pin(name_list, card_list, pin_list, balance_list)
            case 5:
                exit(name_list, card_list, pin_list, balance_list)

# Функции для считывания из файла
def read_file():
    name_list = []
    card_list = []
    pin_list = []
    balance_list = []

# считываем техтовый файл
    file = open('atm_card_pin.txt', 'r')
    lines = file.readlines()
    for line in lines:
        information = line.split()
        card_list.append(information[0])
        pin_list.append(information[1])
        balance_list.append(float(information[2]))
        name_list.append(information[3] + ' ' + information[4])
        
        #print(f'Все счета: {line}')
    return name_list, card_list, pin_list, balance_list

# функция просмотра баланса
def balance_account(name_list, card_list, pin_list, balance_list):
    card_number = input('\nВведите номер вашего счета (16 цифр): ')
    #print(f'Card Number: {card_number[:4]}-{card_number[4:8]}-{card_number[8:12]}-{card_number[12:]}\n')
    index = 0
    found = False
    for i in card_list:
        if i == card_number:
            found = True
            break
        index = index + 1
    if found:
        print()
        #print('\n', datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), '\n')
        #print(f'{name_list[index]}. Баланс вашего счета= {balance_list[index]} р.')
        #print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    else:
        print('\nИзвините. Такой номер карты не существует.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, card_list, pin_list, balance_list
    
    pin_number = pwinput.pwinput('\nВведите PIN код вашей карты (4 цифры): ', mask='*')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    #print(f'PIN code of the card: {pin_number]}\n')
    index = 0
    found = False
    for i in pin_list:
        if i == pin_number:
            found = True
            break
        index = index + 1
    if found:
        print('\n', datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), '\n')
        print(f'{name_list[index]}. Баланс вашего счета= {balance_list[index]} р.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    else:
        print('Извините. Неверный PIN код.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    return name_list, card_list, pin_list, balance_list


# функция снятия денег со счета
def credit(name_list, card_list, pin_list, balance_list):
    card_number = input('\nВведите номер вашего счета: ')
    index = 0
    found = False
    for i in card_list:
        if i == card_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
    else:
        print('Извините. Такой номер карты не существует.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, name_list, card_list, balance_list
        
    pin_number = pwinput.pwinput('\nВведите PIN код вашей карты (4 цифры): ', mask='*')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    #print(f'PIN code of the card: {pin_number}\n')
    index = 0
    found = False
    for i in pin_list:
        if i == pin_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                withdraw_amount = float(input('Введите сумму, которую желаете снять со счета: '))
                # сумма снятая клиентом
                if withdraw_amount < 0:
                    print('ERROR!!! Ввод должен быть положительным целым числом. Повторите ввод.\n')
                    break
                amount = balance_list[index] - withdraw_amount
                # если сумма больше или = 0, вычитаем сумму из баланса
                if amount > 0:
                    balance_list[index] = balance_list[index] - withdraw_amount
                    print('\n', datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
                    print(f'Вы сняли: {withdraw_amount} р. с вашего счета. \nВаш баланс= {balance_list[index]} р.')
                    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
                    problem = False
                else:
                    print(f'{name_list[index]}, к сожалению, у вас недостаточно средств.\n')
                    print(f'Ваш баланс= {balance_list[index]} р.\n')
                    break
            finally:
                return name_list, card_list, pin_list, balance_list
    else:
        print('Извините. Неверный PIN код.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, name_list, card_list, balance_list

# функция пополнения счета
def deposit(name_list, card_list, pin_list, balance_list):
    card_number = input('\nВведите номер вашего счета: ')
    index = 0
    found = False
    for i in card_list:
        if i == card_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
    else:
        print('Извините. Такой номер карты не существует.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, name_list, card_list, balance_list
        
    pin_number = pwinput.pwinput('\nВведите PIN код вашей карты (4 цифры): ', mask='*')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    #print(f'PIN code of the card: {pin_number}\n')
    index = 0
    found = False
    for i in pin_list:
        if i == pin_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                deposit_amount = float(input('Введите сумму, на которую желаете пополнить счет: '))
                # сумма пополнения счета
                if deposit_amount < 0:
                    print('ERROR!!! Ввод должен быть положительным целым числом. Повторите ввод.\n')
                    break
                amount = balance_list[index] + deposit_amount
                if amount > 0:
                    balance_list[index] = balance_list[index] + deposit_amount
                    print('\n', datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
                    print(f'Вы внеесли: {deposit_amount} р. на ваш счет. \nВаш баланс= {balance_list[index]} р.')
                    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
                    problem = False
                #else:
                #    print(f'{name_list[index]}, к сожалению, у вас недостаточно средств.\n')
                #    print(f'Ваш баланс= {balance_list[index]} р.\n')
                #    break
            finally:
                return name_list, card_list, pin_list, balance_list
    else:
        print('Извините. Неверный PIN код.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, name_list, card_list, balance_list
    
def change_pin(name_list, card_list, pin_list, balance_list):
    card_number = input('\nВведите номер вашего счета: ')
    index = 0
    found = False
    for i in card_list:
        if i == card_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
    else:
        print('Извините. Такой номер карты не существует.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, name_list, card_list, balance_list
        
    pin_number = pwinput.pwinput('\nВведите PIN код вашей карты (4 цифры): ', mask='*')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    #print(f'PIN code of the card: {pin_number}\n')
    index = 0
    found = False
    for i in pin_list:
        if i == pin_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                new_pin = input('Введите новый PIN коде (длиной 4 цифры): ')
                if new_pin == None:
                    print('ERROR!!! PIN должен состоять из 4 цифр.\n')
                    break
                if new_pin != None:
                    pin_list[index] = new_pin
                    print('\n', datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
                    print(f'Ваш PIN успешно изменен на: {pin_list[index]}')
                    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
                    problem = False
            finally:
                return name_list, card_list, pin_list, balance_list
    else:
        print('Извините. Неверный PIN код.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        return name_list, name_list, card_list, balance_list

def exit(name_list, card_list, pin_list, balance_list):
    print('Спасибо, что посетили наш банк.')
    quit_file = open('atm_card_pin.txt', 'w')

    for index in range(len(card_list)):
        balance_list[index] = f'{balance_list[index]:.2f}'
        save = f'{card_list[index]} {pin_list[index]} {str(balance_list[index])} {name_list[index]} \n'
        quit_file.write(save)
    
    quit_file.close()

main()