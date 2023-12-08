from models.models import Duration

import unittest


class TestDuration(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'begin',
            'extended',
            'lvl_up',
        )
        self.d = Duration()

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.d, attr) for attr in self.attrs))


if __name__ == '__main__':
    unittest.main()