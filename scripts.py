from objects.ingredients import INGREDIENTS
from objects.potions import POTIONS


# тут вспомогательные скрипты которые не участвуют в основной работе программы


def get_ingredients_names() -> None:
    """
    Выводит на экран информацию об ингредиентах в формате:
    ingredient_name - id
    """
    for indx, ingr in INGREDIENTS.items():
        print(f'{ingr} - {indx}')


def get_all_recipes_potions() -> None:
    """
    Выводит на экран все рецепты зелий в формате:
    Potion: ingr1 -> ingr2 -> ... ingrN
    """
    for potion in POTIONS:
        for ingrs in potion.ingredients_patterns:
            titles = map(str, ingrs)
            recipe = ' -> '.join(titles)
            print(f'{potion.title}: {recipe}')


if __name__ == '__main__':
    get_ingredients_names()
    get_all_recipes_potions()