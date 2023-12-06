from objects.potions import *

import unittest
from copy import deepcopy


class TestPotion(unittest.TestCase):
    def setUp(self) -> None:
        self.sp = deepcopy(strength_potion)
        self.ip = deepcopy(invisibility_potion)
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