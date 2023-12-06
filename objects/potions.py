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
        [
            nether_wart,
        ],
    ],
)

healing_potion = Potion(
    title='Зелье здоровья',
    ingredients_patterns=[
        [
            nether_wart,
            glistering_melon_slice,
        ],
    ],
    duration='instant',
    possible_effects=(
        instant_health,
    ),
    is_lvl_up=True,
)

fire_resistance_potion = Potion(
    title='Зелье огнестойкости',
    ingredients_patterns=[
        [
            nether_wart,
            magma_cream,
        ],
    ],
    possible_effects=(
        fire_resistance,
    ),
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
    ),
    is_duration_up=True,
)

regeneration_potion = Potion(
    title='Зелье регенерации',
    ingredients_patterns=[
        [
            nether_wart,
            ghast_tear,
        ],
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
        [
            nether_wart,
            blaze_powder,
        ],
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
        [
            nether_wart,
            sugar,
        ],
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
        [
            nether_wart,
            golden_carrot,
        ],
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
        [
            nether_wart,
            golden_carrot,
            fermented_spider_eye,
        ],
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

leaping_potion = Potion(
    title='Зелье прыгучести',
    ingredients_patterns=[
        [
            nether_wart,
            rabbit_foot,
        ],
    ],
    possible_effects=(
        jump_boost,
    ),
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8),
        lvl_up=time(minute=1, second=30),
    ),
    is_lvl_up=True,
    is_duration_up=True,
)

water_breathing = Potion(
    title='Зелье подводного дыхания',
    ingredients_patterns=[
        [
            nether_wart,
            pufferfish,
        ],
    ],
    possible_effects=(
      water_breathing,
    ),
    durations_patterns=Duration(
        begin=time(minute=3),
        extended=time(minute=8)
    ),
    is_duration_up=True,
)

slow_falling_potion = Potion(
    title='Зелье медленного падения',
    ingredients_patterns=[
        [
            nether_wart,
            phantom_membrane,
        ],
    ],
    possible_effects=(
        slow_falling,
    ),
    durations_patterns=Duration(
        begin=time(minute=1, second=30),
        extended=time(minute=4),
    ),
    is_duration_up=True,
)

# зелья с негативными эффектами

poison_potion = Potion(
    title='Зелье отравления',
    ingredients_patterns=[
        [
            nether_wart,
            spider_eye,
        ],
    ],
    possible_effects=(
        poison,
    ),
    durations_patterns=Duration(
        begin=time(second=45),
        extended=time(minute=1, second=30),
        lvl_up=time(second=21, microsecond=6),
    ),
    is_duration_up=True,
    is_lvl_up=True,
)

weakness_potion = Potion(
    title='Зелье слабости',
    ingredients_patterns=[
        [
            fermented_spider_eye,
        ],
    ],
    possible_effects=(
        weakness,
    ),
    durations_patterns=Duration(
        begin=time(minute=1, second=30),
        extended=time(minute=4),
    ),
    is_duration_up=True,
)

slowness_potion = Potion(
    title='Зелье замедления',
    ingredients_patterns=[
        [
            nether_wart,
            sugar,
            fermented_spider_eye,
        ],
        [
            nether_wart,
            rabbit_foot,
            fermented_spider_eye,
        ],
    ],
    possible_effects=(
        slowness,
    ),
    durations_patterns=Duration(
        begin=time(minute=1, second=30),
        extended=time(minute=4),
        lvl_up=time(second=20),
    ),
    is_duration_up=True,
    is_lvl_up=True,
)

harming_potion = Potion(
    title='Зелье мгновенного урона',
    ingredients_patterns=[
        [
            nether_wart,
            spider_eye,
            fermented_spider_eye,
        ],
        [
            nether_wart,
            glistering_melon_slice,
            fermented_spider_eye,
        ]
    ],
    duration='instant',
    possible_effects=(
        instant_damage,
    ),
    is_lvl_up=True,
)

# имеет особенный вид эффектов(их 2)
turtle_master_potion = Potion(
    title='Зелье черепашьей мощи',
    ingredients_patterns=[
        [
            nether_wart,
            turtle_shell,
        ],
    ],
    possible_effects=(
        slowness[1],
        resistance,
    ),
    durations_patterns=Duration(
        begin=time(second=20),
        extended=time(second=40),
        lvl_up=time(second=20),
    ),
    is_duration_up=True,
    is_lvl_up=True,
)

# этот брат нужен для удобного импорта всех имён!
# НЕ НАРУШАТЬ ПОРЯДОК 1-ых 2-ух зелий ТАК КАК
# В ТЕСТЕ TestAlchemyStance test_create_all_potions
# ИСПОЛЬЗУЕТСЯ СРЕЗ POTIONS[2:]
POTIONS = (
    water_bubble,
    awkward_potion,
    fire_resistance_potion,
    harming_potion,
    healing_potion,
    invisibility_potion,
    leaping_potion,
    night_vision_potion,
    poison_potion,
    regeneration_potion,
    slow_falling_potion,
    slowness_potion,
    spoiled_potion,
    strength_potion,
    swiftness_potion,
    turtle_master_potion,
    weakness_potion,
)

if __name__ == '__main__':
    # вывести все объекты этого файла на экран
    res = ['water_bubble']
    for obj in dir():
        if obj.endswith('_potion'):
            res.append(obj)
    print(f'RES: {res}')

