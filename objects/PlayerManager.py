from objects.AlchemyStance import AlchemyStance
from objects.potions import POTIONS, water_bubble, spoiled_potion
from objects.ingredients import *

from models.models import Potion

from random import choice, randint
from copy import deepcopy
from time import sleep
from typing import Optional
import os


class PlayerManager:
    def __init__(self):
        # алхимическая стойка
        self.al_st = AlchemyStance()

        # задача игроку
        self.alchemy_task: Potion | None = None

        # нужно ли поднимать лвл зелью
        self.lvl_up_task = False

        # нужно ли поднимать время действия зелья
        self.duration_up_task = False

        # нужно ли делать зелье взрывным
        self.explosive_task = False

        # для удобства буду вести тут список ингредиентов
        self.user_ingrs = []

    def __str__(self):
        """Выводит общую информацию на экран"""
        info = '=============================================================\n' \
               '\tПравила этого клуба описаны в файле README.txt\n' \
               '\tДля выхода введи: exit\n' \
               '=============================================================\n\n'
        return info

    def __generate_alchemy_task(self) -> None:
        """
        Дёргает случайное зелье из списка POTIONS файла potions.py
        Немного преобразует его и отправляет рецепт как задачу игроку.
        """
        # чтобы не было проблем с изменением атрибутов
        # полностью копируем его при помощи deepcopy модуля copy
        alchemy_task = deepcopy(choice(POTIONS[3:]))
        self.al_st.set_bubble(alchemy_task)

        # если зелью можно поднять лвл
        if alchemy_task.is_lvl_up:
            self.lvl_up_task = bool(randint(0, 1))
            if self.lvl_up_task:
                self.al_st.brewing_potion(glowstone)
        # если зелью можно поднять время
        if alchemy_task.is_duration_up and not alchemy_task.is_lvl_up:
            self.duration_up_task = bool(randint(0, 1))
            if self.duration_up_task:
                self.al_st.brewing_potion(redstone)
        # взрывное не взрывное
        self.explosive_task = bool(randint(0, 1))
        if self.explosive_task:
            self.al_st.brewing_potion(powder)
        # регаем задачу
        self.alchemy_task = self.al_st.take_bubble()

    def __check_potion(self, potion: Potion) -> bool:
        """
        Проверяет, удовлетворяет ли сваренное игроком зелье
        тому, которое было поставлено ему в задаче.
        Возвращает True, если это так, False в противном случае.
        """
        check = (
            potion == self.alchemy_task,
            potion.duration == self.alchemy_task.duration,
            potion.effects == self.alchemy_task.effects,
            potion.is_explosive == self.alchemy_task.is_explosive,
            potion.is_lvl_up == self.alchemy_task.is_lvl_up,
            potion.is_duration_up == self.alchemy_task.is_duration_up,
        )
        return all(check)

    def __check_shit(self, ingr: Ingredient = None) -> bool:
        """
        Проверяет не испорчено ли зелье.
        Возвращает bool: True, если испорчено,
        False в противном случае.
        """
        check = (
            self.al_st.bubble is spoiled_potion,
            ingr in self.user_ingrs,
            ingr and self.lvl_up_task and ingr is redstone,
            ingr is powder and not self.explosive_task,
            ingr and self.duration_up_task and ingr is glowstone,
            ingr and not self.lvl_up_task and ingr is glowstone,
            ingr and not self.duration_up_task and ingr is redstone,
        )
        return any(check)

    @staticmethod
    def __get_ingr_by_title(title: str) -> Optional[Ingredient]:
        """
        Позволяет дёрнуть ингредиент по его названию
        Возвращает либо объект Ingredient, либо None.
        """
        for key, ingr in INGREDIENTS.items():
            if ingr.title.lower() == title.lower():
                return ingr

    def play(self) -> bool:
        """
        Игровой цикл
        Возвращает False, если игра закончилась.
        True, если можно повторить партию.
        """
        print(self)
        self.__generate_alchemy_task()
        self.al_st.set_bubble(water_bubble)

        key = None
        while True:
            e = 'Взрывное' if self.explosive_task else ''
            t = 'с увеличенным временем действия' if self.duration_up_task else ''
            info = f'Твоя задача сварить: {e} {self.alchemy_task} {self.alchemy_task.lvl} {t}'
            print(info)

            key = input('\tВведи индекс игредиента или его название: ')
            is_digit = key.isdigit()
            ingr = None

            if key == 'exit':
                return False

            if is_digit:
                index = int(key)
                if index > 0:
                    ingr = INGREDIENTS.get(index, None)
            else:
                ingr = self.__get_ingr_by_title(title=key)

            if not ingr:
                print('\t\tТакого ингредиента не существует.\n')
            else:
                print('\t\tЗелье варится...\r')
                sleep(2)
                self.al_st.brewing_potion(ingr)
                os.system('cls')
                print(self)

                if self.__check_shit(ingr):
                    print('Твоё текущее зелье: \n')
                    print(self.al_st)
                    print(f'Поздравляю, ты сварил говно! GAME OVER.')
                    return True

                # важно чтобы это добавление было после проверки на говно
                # и добавление в основной список al_st
                # этот список используется в методе __check_shit
                self.user_ingrs.append(ingr)
                print(f'\t\tУспешно добавлен {ingr} в зелье\n\n')
                print(self.al_st)

                potion = self.al_st.take_bubble()
                if self.__check_potion(potion):
                    print('Поздравляю, ты сварил нужное зелье!')
                    return True
                else:
                    self.al_st.set_bubble(potion)
                    print('\t\tЗелье ещё не готово.\n')
