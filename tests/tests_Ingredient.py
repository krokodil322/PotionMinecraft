from models import Ingredient

import unittest


class TestIngredient(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'title', 'time_up',
            'lvl_up', 'explosion',
            'transform',
        )
        self.i = Ingredient('Редстоун', True, False, False, False)

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.i, attr) for attr in self.attrs))


if __name__ == '__main__':
    unittest.main()

