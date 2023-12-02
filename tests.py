from models import *
from essences import AlchemyStance

from objects.potions import *

import unittest


class TestIngredient(unittest.TestCase):
    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        attrs = (
            'title', 'time_up',
            'lvl_up', 'explosion',
            'transform',
        )
        i = Ingredient('Редстоун', True, False, False, False)
        self.assertTrue(all(hasattr(i, attr) for attr in attrs))


class TestEffect(unittest.TestCase):
    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        attrs = (
            'title',
            'lvl',
        )
        e = Effect('Сила', 2)
        self.assertTrue(all(hasattr(e, attr) for attr in attrs))


class TestDuration(unittest.TestCase):
    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        attrs = (
            'begin',
            'extended',
            'lvl_up',
        )
        d = Duration()
        self.assertTrue(all(hasattr(d, attr) for attr in attrs))


class TestPotion(unittest.TestCase):
    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        attrs = (
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
        p = strength_potion
        self.assertTrue(all(hasattr(p, attr) for attr in attrs))

    def test_equal_potions(self):
        """Проверка корректности сравнения 2-ух зелий"""
        p1 = strength_potion
        p2 = invisibility_potion
        self.assertFalse(p1 == p2)

        p3 = Potion(
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
        self.assertEqual(p1, p3)


class TestAlchemyStance(unittest.TestCase):
    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        attrs = (
            'curr_ingrs',
            'potion',
        )
        al_st = AlchemyStance()
        self.assertTrue(all(hasattr(al_st, attr) for attr in attrs))

    def test_set_bubble(self):
        """Тест метода set_bubble"""
        al_st = AlchemyStance()
        al_st.set_bubble(water_bubble)

        self.assertTrue(len(al_st) == 1)

        al_st.set_bubble(nether_wart)
        self.assertTrue(len(al_st) == 1)

        al_st = AlchemyStance()
        al_st.set_bubble(nether_wart)
        self.assertTrue(len(al_st) == 0)

        al_st = AlchemyStance()
        al_st.set_bubble(strength_potion)
        self.assertEqual(al_st.curr_ingrs, strength_potion.ingredients_patterns)
        self.assertTrue(al_st.potion.effects[0] is strength_potion.effects[0])

        al_st = AlchemyStance()
        al_st.set_bubble(night_vision_potion)
        self.assertEqual(al_st.curr_ingrs, night_vision_potion.ingredients_patterns)
        self.assertTrue(al_st.potion.effects[0] is night_vision_potion.effects[0])

    def test_brewing_potion(self):
        """Тест главного метода brewing_potion'а"""

        # варка с нуля до зелья силы 2-го
        al_st = AlchemyStance()
        al_st.set_bubble(water_bubble)
        al_st.brewing_potion(nether_wart)
        self.assertEqual(al_st.potion, awkward_potion)

        size_before = len(al_st)
        al_st.brewing_potion(nether_wart)
        size_after = len(al_st)
        self.assertEqual(size_before, size_after)

        al_st.brewing_potion(blaze_powder)
        self.assertTrue(al_st.potion is strength_potion)

        al_st.brewing_potion(powder)
        self.assertTrue(al_st.potion.is_explosive)

        al_st.brewing_potion(glowstone)
        self.assertFalse(al_st.potion.is_lvl_up)
        self.assertFalse(al_st.potion.is_duration_up)
        self.assertTrue(al_st.potion.lvl == 2)
        self.assertTrue(
            al_st.potion.effects[0] is strength[1]
        )
        self.assertTrue(
            al_st.potion.duration == \
            strength_potion.durations_patterns.lvl_up
        )

    def test_brewing_potion(self):
        """Тест метода breawing_potion часть 2"""

        # варка начиная с зелья силы 2
        al_st = AlchemyStance()
        al_st.set_bubble(strength_potion)

        al_st.brewing_potion(powder)
        self.assertTrue(al_st.potion.is_explosive)

        al_st.brewing_potion(glowstone)
        self.assertFalse(al_st.potion.is_lvl_up)
        self.assertFalse(al_st.potion.is_duration_up)
        self.assertTrue(al_st.potion.lvl == 2)
        self.assertTrue(
            al_st.potion.effects[0] is strength[1]
        )
        self.assertTrue(
            al_st.potion.duration == \
            strength_potion.durations_patterns.lvl_up
        )

    def test_brewing_potion(self):
        """Тест метода breawing_potion часть 3"""
        # варка с нуля зелья невидимости
        al_st = AlchemyStance()
        al_st.set_bubble(water_bubble)
        al_st.brewing_potion(nether_wart)
        al_st.brewing_potion(golden_carrot)
        al_st.brewing_potion(fermented_spider_eye)

        self.assertEqual(al_st.potion, invisibility_potion)

        # сварим начиная с зелья ночного зрения
        al_st = AlchemyStance()
        al_st.set_bubble(night_vision_potion)
        al_st.brewing_potion(fermented_spider_eye)
        self.assertEqual(al_st.potion, invisibility_potion)

        al_st.brewing_potion(redstone)
        self.assertEqual(
            al_st.potion.duration,
            al_st.potion.durations_patterns.extended,
        )

    def test_take_bubble(self):
        """Тест метода take_bubble"""

        al_st = AlchemyStance()
        al_st.set_bubble(water_bubble)
        al_st.brewing_potion(nether_wart)
        self.assertEqual(al_st.potion, awkward_potion)

        size_before = len(al_st)
        al_st.brewing_potion(nether_wart)
        size_after = len(al_st)
        self.assertEqual(size_before, size_after)

        al_st.brewing_potion(blaze_powder)
        potion = al_st.take_bubble()
        self.assertEqual(potion, strength_potion)

        self.assertFalse(al_st.potion)
        self.assertFalse(al_st.curr_ingrs)

        al_st.set_bubble(potion)
        al_st.brewing_potion(powder)
        al_st.brewing_potion(redstone)
        potion = al_st.take_bubble()

        self.assertTrue(potion.is_explosive)
        self.assertFalse(potion.is_lvl_up)
        self.assertFalse(potion.is_duration_up)

        self.assertEqual(potion.effects[0], strength[0])
        self.assertEqual(
            potion.duration,
            potion.durations_patterns.extended
        )


if __name__ == '__main__':
    unittest.main()

