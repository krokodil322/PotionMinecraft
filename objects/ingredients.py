from models.models import Ingredient


# тут созданы все возможные ингредиенты для зелий

redstone = Ingredient(
    title='Редстоун',
    time_up=True,
    lvl_up=False,
    explosion=False,
    transform=False,
)

glowstone = Ingredient(
    title='Светопыль',
    time_up=False,
    lvl_up=True,
    explosion=False,
    transform=False,
)

powder = Ingredient(
    title='Порох',
    time_up=False,
    lvl_up=False,
    explosion=True,
    transform=False,
)

nether_wart = Ingredient(
    title='Адский нарост',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

fermented_spider_eye = Ingredient(
    title='Маринованный паучий глаз',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

sugar = Ingredient(
    title='Сахар',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

glistering_melon_slice = Ingredient(
    title='Золотистый арбуз',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

magma_cream = Ingredient(
    title='Магмовая слизь',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

golden_carrot = Ingredient(
    title='Золотая морковь',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

blaze_powder = Ingredient(
    title='Огненный порошок',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

ghast_tear = Ingredient(
    title='Слеза гаста',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

rabbit_foot = Ingredient(
    title='Кроличья лапка',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

pufferfish = Ingredient(
    title='Иглобрюх',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

spider_eye = Ingredient(
    title='Паучий глаз',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

turtle_shell = Ingredient(
    title='Черепашьий панцирь',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

phantom_membrane = Ingredient(
    title='Фантомная мембрана',
    time_up=False,
    lvl_up=False,
    explosion=False,
    transform=True,
)

INGREDIENTS = {
    1: redstone,
    2: glowstone,
    3: powder,
    4: nether_wart,
    5: fermented_spider_eye,
    6: sugar,
    7: glistering_melon_slice,
    8: magma_cream,
    9: golden_carrot,
    10: blaze_powder,
    11: ghast_tear,
    12: rabbit_foot,
    13: pufferfish,
    14: spider_eye,
    15: turtle_shell,
    16: phantom_membrane,
}
