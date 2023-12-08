from objects.PlayerManager import PlayerManager

import os


game = True
while game:
    os.system('cls')
    manager = PlayerManager()
    game = manager.play()

    while game:
        is_continue = input('Не хочешь ещё разок? Введи да или нет: ').lower()

        if is_continue in ('нет', 'exit', 'quit'):
            game = False
        elif is_continue == 'да':
            break
        else:
            print('Ты ввёл неправильные данные!')