from models import Ingredient
from objects.ingredients import redstone

import unittest
from copy import deepcopy


class TestIngredient(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'title', 'time_up',
            'lvl_up', 'explosion',
            'transform',
        )
        self.i = Ingredient('Редстоун', True, False, False, False)
        self.i_eq = deepcopy(redstone)

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.i, attr) for attr in self.attrs))

    def test_equal_ingredients(self):
        """Проверка сравнения объектов Ingredient"""
        self.assertTrue(self.i == self.i_eq)


if __name__ == '__main__':
    unittest.main()

