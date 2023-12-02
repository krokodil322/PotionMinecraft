from datetime import time
from typing import Union


class Ingredient:
    """Модель описывающая ингредиенты для зелий"""
    __slots__ = (
        'title',
        'time_up',
        'lvl_up',
        'explosion',
        'transform',
    )

    def __init__(
            self,
            title: str,
            time_up: bool,
            lvl_up: bool,
            explosion: bool,
            transform: bool,
    ):
        # название ингредиента
        self.title = title

        # может ли ингредиент увеличить время длительности зелья
        self.time_up = time_up

        # может ли ингредиент поднять уровень зелья
        self.lvl_up = lvl_up

        # может ли ингредиент сделать зелье взрывным
        self.explosion = explosion

        # может ли трансформировать зелье
        self.transform = transform

    def __str__(self):
        return self.title


class Effect:
    """Модель описывающая эффекты от зелий"""
    __slots__ = (
        'title',
        'lvl',
    )

    def __init__(
            self,
            title: str,
            lvl: int = 0,
    ):
        # название эффекта
        self.title = title

        # уровень эффекта
        self.lvl = lvl

    def __str__(self):
        return f'{self.title} {self.lvl}'


class Duration:
    """
    Сущность в которой будут определяться тайминги
    зелий при всех возможных вариантах улучшений
    """
    __slots__ = ('begin', 'extended', 'lvl_up',)
    def __init__(
            self,
            begin: time = time(),
            extended: time = time(),
            lvl_up: time = time(),
    ):
        # обычное не прокаченное зелье
        self.begin = begin

        # с редстоуном
        self.extended = extended

        # со светопылью
        self.lvl_up = lvl_up


class Potion:
    """Модель описывающая зелья"""
    def __init__(
            self,
            title: str,
            ingredients_patterns: list[Union[Ingredient, 'Potion']] = [],
            ingredients: list[Union[Ingredient, 'Potion']] = [],
            possible_effects: tuple[tuple[Effect]] = None,
            effects: list[Effect] = [],
            lvl: int = 0,
            is_lvl_up: bool = False,
            duration: time = time(),
            is_duration_up: bool = False,
            durations_patterns: Duration = None,
            is_explosive: bool = False,
    ):
        # название зелья
        self.title = title

        # список ингредиентов(короче - рецепт) для создания
        self.ingredients_patterns = ingredients_patterns
        # список текущих ингредиентов
        self.ingredients = ingredients

        # список всех возможных эффектов данного типа зелья
        self.possible_effects = possible_effects
        # список текущих эффектов
        self.effects = effects

        # уровень зелья
        self.lvl = lvl
        # можно ли увеличить уровень
        self.is_lvl_up = is_lvl_up

        # в этом объекте будут расписаны все возможные тайминги для зелья
        self.durations_patterns = durations_patterns
        if self.durations_patterns and self.durations_patterns.begin:
            # текущая продолжительность действия
            self.duration = self.durations_patterns.begin
        else:
            self.duration = duration
        # можно ли увеличить время действия
        self.is_duration_up = is_duration_up

        # взрывное не взрывное
        self.is_explosive = is_explosive

    def __eq__(self, other: 'Potion') -> bool:
        """
        Сравнение зелий производится по списку их ингредиентов!
        """
        if isinstance(other, Potion):
            return self.ingredients_patterns == other.ingredients_patterns
        return False

    def __str__(self):
        return self.title

