from models import Effect
from objects.effects import strength

import unittest
from copy import deepcopy


class TestEffect(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'title',
            'lvl',
        )
        self.e = Effect('Сила', 2)
        self.e_eq = deepcopy(strength[1])

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.e, attr) for attr in self.attrs))

    def test_equal_effects(self):
        """Проверка сравнения объектов Effect"""
        self.assertTrue(self.e == self.e_eq)


if __name__ == '__main__':
    unittest.main()