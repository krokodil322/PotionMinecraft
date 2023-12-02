from models import Effect


# тут реализованы все возможные эффекты для зелий

speed = (
    Effect(title='Скорость', lvl=1),
    Effect(title='Скорость', lvl=2),
)

slowness = (
    Effect(title='Медлительность', lvl=1),
    Effect(title='Медлительность', lvl=2),
    Effect(title='Медлительность', lvl=3),
    Effect(title='Медлительность', lvl=4),
)

strength = (
    Effect(title='Сила', lvl=1),
    Effect(title='Сила', lvl=2),
)

instant_health = (
    Effect(title='Здоровье', lvl=1),
    Effect(title='Здоровье', lvl=2),
)

instant_damage = (
    Effect(title='Мгновенный урон', lvl=1),
    Effect(title='Мгновенный урон', lvl=2),
)

jump_boost = (
    Effect(title='Прыгучесть', lvl=1),
    Effect(title='Прыгучесть', lvl=2),
)

regeneration = (
    Effect(title='Регенерация', lvl=1),
    Effect(title='Регенерация', lvl=2),
)

resistance = (
    Effect(title='Сопротивление урону', lvl=1),
    Effect(title='Сопротивление урону', lvl=2),
    Effect(title='Сопротивление урону', lvl=3),
    Effect(title='Сопротивление урону', lvl=4),
)

fire_resistance = (
    Effect(title='Сопротивление огню', lvl=1),
    Effect(title='Сопротивление огню', lvl=2),
    Effect(title='Сопротивление огню', lvl=3),
    Effect(title='Сопротивление огню', lvl=4),
)

water_breathing = (
    Effect(title='Подводное дыхание', lvl=1),
)

invisibility = (
    Effect(title='Невидимость', lvl=1),
)

night_vision = (
    Effect(title='Ночное зрение', lvl=1),
)

weakness = (
    Effect(title='Слабость', lvl=1),
)

poison = (
    Effect(title='Отравление', lvl=1),
    Effect(title='Отравление', lvl=2),
)

slow_falling = (
    Effect(title='Медленного падения', lvl=1),
)