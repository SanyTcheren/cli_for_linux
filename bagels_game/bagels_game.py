"""Бейглз, дедуктивная логическая игра."""
import argparse
from random import randint
from colorama import init, Fore
init()


def bagels_greating(length):
    """
    Приветствие для игры Бейглз и объяснение её правил.

    Зависит от colorama
    """
    end = ''
    if 1 < length < 5:
        end = '-х'
    elif 5 <= length < 100:
        end = '-и'
    elif length == 1:
        end = '-о'
    print(Fore.GREEN +
          '''
          Бейглз, дедуктивная логическая игра.
          От Sany Tcheren tcherenkovskiy@gmail.com''')
    print(Fore.CYAN +
          f'''
    Я загадал {length}{end} значное число, попробуйте угадать его.
    Предлогайте варианты, а я буду Вам подсказывать.
    Если я говорю:    Это значит:
        Пико          В Вашем числе есть правильная цифра на неправильном месте
        Ферми         В Вашем числе есть правильная цифра на правильном месте
        Бейглз        В Вашем числе нет правильных цифр
          ''' + Fore.RESET)


def offer_game():
    """
    Предложение сыграть в игру.

    Печатает предложение сыграть и возвращает результат ответа (True/False).
    Зависет от colorama.
    """
    answer = 'н'
    offer = Fore.GREEN + "Сыграем в Бейглз?(д/н): " + Fore.RESET
    while True:
        answer = input(offer).lower()
        if answer not in ['д', 'н']:
            print(Fore.RED + 'Введите на клавиатуре "д" или "н"' + Fore.RESET)
        else:
            break
    return answer == "д"


def get_number(length):
    """Получение строки с цифрами."""
    number = []
    while True:
        number_str = input(Fore.GREEN + 'Ваше число: ')
        if len(number_str) != length:
            print(Fore.RED + f'чило должно быть из {length} цифр!!!')
            continue
        try:
            for i in range(length):
                number.append(int(number_str[i]))
            return number
        except ValueError:
            print(Fore.RED + 'В числе должны быть только цифры от 0 до 9!!!')
            continue


def check_win(number, target):
    """Проверка на полное совпадение."""
    for i, value in enumerate(number):
        if value != target[i]:
            return False
    return True


def check_number(number, target):
    """Анализ цифр и возврат подсказки."""
    result = []
    for i, value in enumerate(number):
        if value == target[i]:
            result.append('Ферми')
        elif value in target:
            result.append('Пико')
    if len(result) == 0:
        result.append('Бейглз')
    result.sort()
    return ' '.join(result)


def main(length, counter):
    """Главная функция игры Бейглз."""
    bagels_greating(length)
    while offer_game():
        target_str = str(randint(10**(length-1), 10**length-1))
        target = [int(x) for x in target_str]
        print(Fore.CYAN + f'У вас {counter} попыток, начинаем')
        for i in range(1, counter+2):
            if i == counter+1:
                print(Fore.BLUE +
                      'Попытки закончились, Вы проиграли.',
                      f'Моё число: {target_str}')
                break
            print(Fore.CYAN + f'Попытка №{i}')
            number = get_number(length)
            if check_win(number, target):
                print(Fore.BLUE + "Мои поздравления, Вы угадали!!!")
                break
            print(Fore.GREEN + check_number(number, target))
    print(Fore.CYAN + "Спасибо за игру." + Fore.RESET)


def create_parser():
    """Создаем парсер аргументов."""
    parser = argparse.ArgumentParser(
        prog='bagels_game',
        description='Логическая мини-игра "Бейглз"',
        epilog='@2022 Sany Tcheren thcerenkovskiy@gmail.com')
    parser.add_argument('-l', '--length', default=3, type=int,
                        help='количество цифр в загаданном слове')
    parser.add_argument('-c', '--counter', default=10, type=int,
                        help='колличество попыток')
    return parser


if __name__ == '__main__':
    my_parser = create_parser()
    my_namespace = my_parser.parse_args()
    main(my_namespace.length, my_namespace.counter)
