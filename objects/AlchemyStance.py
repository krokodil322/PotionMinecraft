from objects.potions import *

from copy import deepcopy
from random import choice


class AlchemyStance:
    """
    Алхимической стойка
    """

    def __init__(self, is_minecraft: bool=False):
        # список добавленных ингредиентов
        self.curr_ingrs = []

        # текущее зелье
        self.bubble = None

        # зельки варятся исключительно по правилам майна
        # пока не используется
        self.__is_minecraft = is_minecraft

    def __len__(self) -> int:
        """
        Размер объекта вычисляется
        по размеру списка с ингредиентами
        """
        return len(self.curr_ingrs)

    def __str__(self):
        """Служебный вывод инфы о текущей зельке"""
        # try:
        ingrs = [str(ingr) for ingr in self.curr_ingrs]
        effects = [str(eff) for eff in self.bubble.effects]

        duration = self.bubble.duration
        if self.bubble.duration != 'instant':
            duration = duration.strftime("%M:%S")

        info = f'\nВарочная стойка\n' \
               f'Текущее зелье: {self.bubble}\n' \
               f'Добавленные ингредиенты: {ingrs}\n' \
               f'Эффекты: {effects}\n' \
               f'Время действия: {duration}\n' \
               f'Уровень зелья: {self.bubble.lvl}\n' \
               f'Взрывное ли: {self.bubble.is_explosive}\n' \
               f'Можно ли увелить время действия: {self.bubble.is_duration_up}\n' \
               f'Можно ли увеличить уровень: {self.bubble.is_lvl_up}\n'
        return info
        # если в стойке potion=None, то будут проблемы с выводом
        # except AttributeError:
        #     return 'Стойка пока пуста.'

    def set_bubble(self, bubble: Potion) -> None:
        """
        Добавляет склянку с жидкостью на алхимическую стойку
        Если объект не типа Potion, либо в ячейке зелья уже что-то есть,
        то его нельзя положить в данную ячейку
        """
        if isinstance(bubble, Potion) and not self.bubble:
            self.bubble = bubble
            if bubble.lvl == 0:
                self.bubble.lvl = 1

            # только у water_bubble и spoiled_potion нету паттерна
            # по ингредиентам => если не они, то копируем ингредиенты в curr_ingrs
            # это нужно когда мы варим начиная не с water_bubble, а с какого-нибудь зелья
            if self.bubble not in (water_bubble, spoiled_potion):
                if not self.bubble.ingredients:
                    self.curr_ingrs = choice(self.bubble.ingredients_patterns)
                else:
                    self.curr_ingrs = self.bubble.ingredients
                # в таком случае ещё устанавливаем эффекты
                self.__set_effects_potion()

    def take_bubble(self) -> Potion:
        """
        Возвращает сваренное зелье, очищает
        классовые атрибуты от уже ненужного хлама:
        Очищает список ингредиентов curr_ingrs
        Ставит значение None для potion
        """
        # устанавливаем текущие ингредиенты в данные зелья
        self.bubble.ingredients = self.curr_ingrs
        # сбрасываем текущий список
        self.curr_ingrs = []
        # перекидываем объект зелья на другую ссылку
        potion = self.bubble
        # очищаем старую ссылку
        self.bubble = None
        return potion

    def brewing_potion(self, ingr: Ingredient) -> None:
        """
        Главный метод этой сущности. Меняет сами зелья, либо
        их св-ва в зависимости от принятого параметра ingr.
        """
        if ingr.transform and ingr not in self.curr_ingrs:
            # эта ветка срабатывает когда ингредиент
            # полностью меняет тип зелья
            self.curr_ingrs.append(ingr)

            # сверяем текущие ингредиенты
            # с ингредиентами зелий из файла potions.py
            new_potion = None
            search = False
            for potion in POTIONS:
                for ingrs in potion.ingredients_patterns:
                    if self.curr_ingrs == ingrs:
                        new_potion = deepcopy(potion)
                        search = True
                        break
                if search:
                    break


            # эта часть отвечает за новоприбывшие зелья
            # она подгоняет их шаблонные характеристики
            # к характеристикам текущего зелья в bubble
            if not new_potion:
                self.bubble = spoiled_potion
            else:
                new_potion.lvl = self.bubble.lvl
                new_potion.is_explosive = self.bubble.is_explosive

                # если у зелья is_duration_up=False и duration != 'instant'
                # это означает, что зелье прокачено редстоуном и нужно
                # поставить новому зелью тайминги как у прокаченного зелья
                if not self.bubble.is_duration_up \
                   and self.bubble.duration == self.bubble.durations_patterns.extended:
                    new_potion.duration = new_potion.durations_patterns.extended
                    new_potion.is_duration_up = False
                    new_potion.is_lvl_up = False

                # если у зелья is_lvl_up=False и в паттернах таймингов
                # присутствует время для прокачки, то это значит, что
                # этому зелью нужно прокачать показатели лвла, эффектов
                if (self.bubble not in (water_bubble, awkward_potion, spoiled_potion) and
                    not self.bubble.is_lvl_up and
                   (self.bubble.duration == self.bubble.durations_patterns.lvl_up
                    or self.bubble.duration == 'instant')):

                    if new_potion.duration != 'instant':
                        new_potion.duration = new_potion.durations_patterns.lvl_up
                    new_potion.is_duration_up = False
                    new_potion.is_lvl_up = False

                self.bubble = new_potion
                del new_potion

            self.__set_effects_potion()

        elif ingr.lvl_up and self.bubble.is_lvl_up:
            # эта ветка срабатывает, когда ингредиент
            # может поднять уровень зелья
            self.bubble.is_duration_up = False
            self.bubble.is_lvl_up = False

            # поднимаем уровень
            self.bubble.lvl += 1

            # устанавливаем эффекты соответственно уровню
            self.__set_effects_potion()

            # устанавливаем время прокаченное светопылью зелья
            if self.bubble.duration != 'instant':
                self.bubble.duration = self.bubble.durations_patterns.lvl_up

        elif ingr.time_up and self.bubble.is_duration_up:
            # эта ветка срабатывает, когда ингредиент
            # может увеличить продолжительность действия зелья
            self.bubble.is_duration_up = False
            self.bubble.is_lvl_up = False

            # устанавливаем время прокаченного редстоуном зелья
            self.bubble.duration = self.bubble.durations_patterns.extended

        elif ingr.explosion and not self.bubble.is_explosive:
            # эта ветка срабатывает, когда попадает порох
            self.bubble.is_explosive = True

    def __set_effects_potion(self) -> None:
        """Устанавливает эффекты зелью"""
        if self.bubble and self.bubble.possible_effects:
            # сбрасываем старые эффекты
            self.bubble.effects = []
            # идём по ожидаемым эффектам зелья
            for group_effects in self.bubble.possible_effects:
                # дёргаем конкретный эффект по уровню
                # если зелье имеет постоянный эффект на всех лвлах(черепашье зелье),
                # то проверяем передаваемый эффект на итерируемость
                # если он итерируемый, то значит смещаем значение
                # эффекта вместе с лвлом, а, если нет, то
                # он просто переходит без имзенений
                if hasattr(group_effects, '__iter__'):
                    effect = group_effects[self.bubble.lvl - 1]
                else:
                    effect = group_effects
                self.bubble.effects.append(effect)


if __name__ == '__main__':
    def show_data_potion(potion: Potion) -> None:
        if not isinstance(potion, Potion):
            raise TypeError(f'potion must be Potion but get type: {type(potion)}')

        for key, value in potion.__dict__.items():
            print(key, value, sep=': ')

    al_st = AlchemyStance()
    al_st.set_bubble(water_bubble)
    al_st.brewing_potion(nether_wart)
    al_st.brewing_potion(golden_carrot)
    al_st.brewing_potion(fermented_spider_eye)
    al_st.brewing_potion(redstone)

    p = al_st.take_bubble()
    al_st.set_bubble(p)
    p = al_st.take_bubble()
    print(al_st)
    show_data_potion(p)
