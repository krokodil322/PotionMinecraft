from objects.potions import *
from objects.AlchemyStance import AlchemyStance

from models import *

import unittest
from datetime import time


class TestAlchemyStance(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'curr_ingrs',
            'potion',
        )
        self.al_st = AlchemyStance()
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
        self.nvp = Potion(
            title='Зелье ночного зрения',
            ingredients_patterns=[
                water_bubble,
                nether_wart,
                golden_carrot,
            ],
            possible_effects=(
                night_vision,
            ),
            durations_patterns=Duration(
                begin=time(minute=3),
                extended=time(minute=8),
            ),
            is_duration_up=True,
        )

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.al_st, attr) for attr in self.attrs))

    def test_set_bubble(self):
        """Тест метода set_bubble"""
        self.al_st.set_bubble(water_bubble)

        self.assertTrue(len(self.al_st) == 1)

        self.al_st.set_bubble(nether_wart)
        self.assertTrue(len(self.al_st) == 1)

    def test_set_bubble_2(self):
        self.al_st.set_bubble(nether_wart)
        self.assertTrue(len(self.al_st) == 0)

    def test_set_bubble_3(self):
        self.al_st.set_bubble(self.sp)
        self.assertEqual(self.al_st.curr_ingrs, strength_potion.ingredients_patterns)
        self.assertTrue(self.al_st.potion.effects[0] == strength_potion.possible_effects[0][0])

    def test_set_bubble_4(self):
        self.al_st.set_bubble(self.nvp)
        self.assertEqual(self.al_st.curr_ingrs, night_vision_potion.ingredients_patterns)
        self.assertTrue(self.al_st.potion.effects[0] == night_vision_potion.possible_effects[0][0])

    def test_brewing_potion(self):
        """Тест главного метода brewing_potion'а"""

        # варка с нуля до зелья силы 2-го
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.assertTrue(self.al_st.potion == awkward_potion)

        size_before = len(self.al_st)
        self.al_st.brewing_potion(nether_wart)
        size_after = len(self.al_st)
        self.assertEqual(size_before, size_after)

        self.al_st.brewing_potion(blaze_powder)
        self.assertTrue(self.al_st.potion == strength_potion)

        self.al_st.brewing_potion(powder)
        self.assertTrue(self.al_st.potion.is_explosive)

        self.al_st.brewing_potion(glowstone)
        self.assertFalse(self.al_st.potion.is_lvl_up)
        self.assertFalse(self.al_st.potion.is_duration_up)
        self.assertTrue(self.al_st.potion.lvl == 2)
        self.assertTrue(
            self.al_st.potion.effects[0] == strength[1]
        )
        self.assertTrue(
            self.al_st.potion.duration == \
            strength_potion.durations_patterns.lvl_up
        )

    def test_brewing_potion_2(self):
        """Тест метода breawing_potion часть 2"""

        # варка начиная с зелья силы 2
        self.al_st.set_bubble(self.sp)

        self.al_st.brewing_potion(powder)
        self.assertTrue(self.al_st.potion.is_explosive)

        self.al_st.brewing_potion(glowstone)
        self.assertFalse(self.al_st.potion.is_lvl_up)
        self.assertFalse(self.al_st.potion.is_duration_up)
        self.assertTrue(self.al_st.potion.lvl == 2)
        self.assertTrue(
            self.al_st.potion.effects[0] == strength[1]
        )
        self.assertTrue(
            self.al_st.potion.duration == \
            strength_potion.durations_patterns.lvl_up
        )

    def test_brewing_potion_3(self):
        """Тест метода breawing_potion часть 3"""
        # варка с нуля зелья невидимости
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(golden_carrot)
        self.al_st.brewing_potion(fermented_spider_eye)

        self.assertTrue(self.al_st.potion == invisibility_potion)

    def test_brewing_potion_4(self):
        """Тест метода breawing_potion часть 4"""
        # сварим начиная с зелья ночного зрения
        self.al_st.set_bubble(self.nvp)
        self.al_st.brewing_potion(fermented_spider_eye)
        self.assertEqual(self.al_st.potion, invisibility_potion)

        self.al_st.brewing_potion(redstone)
        self.assertTrue(
            self.al_st.potion.duration == \
            self.al_st.potion.durations_patterns.extended,
        )

    def test_take_bubble(self):
        """Тест метода take_bubble"""

        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.assertTrue(self.al_st.potion == awkward_potion)

        size_before = len(self.al_st)
        self.al_st.brewing_potion(nether_wart)
        size_after = len(self.al_st)
        self.assertEqual(size_before, size_after)

        self.al_st.brewing_potion(blaze_powder)

        potion = self.al_st.take_bubble()
        self.assertTrue(potion == strength_potion)

        self.assertFalse(self.al_st.potion)
        self.assertFalse(self.al_st.curr_ingrs)

        self.al_st.set_bubble(potion)
        self.al_st.brewing_potion(powder)
        self.al_st.brewing_potion(redstone)
        potion = self.al_st.take_bubble()

        self.assertTrue(potion.is_explosive)
        self.assertFalse(potion.is_lvl_up)
        self.assertFalse(potion.is_duration_up)

        self.assertTrue(potion.effects[0] == strength[0])
        print(potion.duration, potion.durations_patterns)
        # self.assertTrue(potion.duration == \
        #     potion.durations_patterns.extended
        # )


if __name__ == '__main__':
    unittest.main()