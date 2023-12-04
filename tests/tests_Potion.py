from objects.potions import *

import unittest


class TestPotion(unittest.TestCase):
    def setUp(self) -> None:
        self.sp = Potion(
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
        self.ip = Potion(
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
        self.attrs = (
            'title',
            'ingredients_patterns',
            'ingredients',
            'possible_effects',
            'effects',
            'lvl',
            'is_lvl_up',
            'duration',
            'durations_patterns',
            'is_duration_up',
            'is_explosive',
        )

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.sp, attr) for attr in self.attrs))

    def test_equal_potions(self):
        """Проверка корректности сравнения 2-ух зелий"""
        self.assertFalse(self.sp == self.ip)
        self.assertEqual(self.sp, strength_potion)


if __name__ == '__main__':
    unittest.main()