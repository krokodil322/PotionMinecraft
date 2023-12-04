from models import Effect

import unittest


class TestEffect(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'title',
            'lvl',
        )
        self.e = Effect('Сила', 2)

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.e, attr) for attr in self.attrs))