from objects.effects import *
from objects.ingredients import *

from models import Potion, Duration

from datetime import time


# тут описаны основные рецепты зелий и привязка эффектов к ним

water_bubble = Potion(
    title='Пузырёк воды',
)

spoiled_potion = Potion(
    title='Испорченное зелье',
)

awkward_potion = Potion(
    title='Неуклюжее зелье',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
    ],
)

healing_potion = Potion(
    title='Зелье здоровья',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        glistering_melon_slice,
    ],
    possible_effects=(
        instant_health,
    ),
    is_lvl_up=True,
)

fire_resistance_potion = Potion(
    title='Зелье огнестойкости',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        magma_cream,
    ],
    possible_effects=(
        fire_resistance,
    ),
    is_lvl_up=True,
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
        lvl_up=time(minute=8),
    ),
    is_duration_up=True,
)

regeneration_potion = Potion(
    title='Зелье регенерации',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        ghast_tear,
    ],
    possible_effects=(
        regeneration,
    ),
    is_lvl_up=True,
    durations_patterns=Duration(
        begin=time(second=45),
        extended=time(minute=1, second=30),
        lvl_up=time(second=22),
    ),
    is_duration_up=True,
)

strength_potion = Potion(
    title='Зелье силы',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        blaze_powder,
    ],
    possible_effects=(
        strength,
    ),
    is_lvl_up=True,
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
        lvl_up=time(minute=1, second=30),
    ),
    is_duration_up=True,
)

swiftness_potion = Potion(
    title='Зелье скорости',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        sugar,
    ],
    possible_effects=(
        speed,
    ),
    is_lvl_up=True,
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
        lvl_up=time(minute=1, second=30),
    ),
    is_duration_up=True,
)

night_vision_potion = Potion(
    title='Зелье ночного зрения',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        golden_carrot,
    ],
    possible_effects=(
        night_vision,
    ),
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
    ),
    is_duration_up=True,
)

invisibility_potion = Potion(
    title='Зелье невидимости',
    ingredients_patterns=[
        water_bubble,
        nether_wart,
        golden_carrot,
        fermented_spider_eye,
    ],
    possible_effects=(
        invisibility,
    ),
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
    ),
    is_duration_up=True,
)

# этот брат нужен для удобного импорта всех имён!
POTIONS = [
    spoiled_potion, awkward_potion, water_bubble,
    fire_resistance_potion, healing_potion, invisibility_potion,
    night_vision_potion, regeneration_potion, strength_potion,
    swiftness_potion,
]


if __name__ == '__main__':
    # вывести все объекты этого файла на экран
    res = [water_bubble]
    for obj in dir():
        if obj.endswith('_potion'):
            res.append(obj)
    print(f'RES: {res}')

