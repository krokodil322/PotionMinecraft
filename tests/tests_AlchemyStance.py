from objects.potions import *
from objects.AlchemyStance import AlchemyStance

import unittest
from copy import deepcopy


class TestAlchemyStance(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = (
            'curr_ingrs',
            'bubble',
        )
        self.al_st = AlchemyStance()
        self.sp = deepcopy(strength_potion)
        self.ip = deepcopy(invisibility_potion)
        self.nvp = deepcopy(night_vision_potion)

    def test_attrs(self):
        """Проверка на наличие необходимых атрибутов"""
        self.assertTrue(all(hasattr(self.al_st, attr) for attr in self.attrs))

    def test_set_bubble(self):
        """Тест метода set_bubble"""
        self.al_st.set_bubble(water_bubble)

        self.assertTrue(len(self.al_st) == 0)

        self.al_st.set_bubble(nether_wart)
        self.assertTrue(len(self.al_st) == 0)

    def test_set_bubble_2(self):
        self.al_st.set_bubble(nether_wart)
        self.assertTrue(len(self.al_st) == 0)

    def test_set_bubble_3(self):
        self.al_st.set_bubble(self.sp)
        self.assertTrue(
            self.al_st.curr_ingrs == strength_potion.ingredients_patterns[0]
        )
        self.assertTrue(
            self.al_st.bubble.effects[0] == strength_potion.possible_effects[0][0]
        )

    def test_set_bubble_4(self):
        self.al_st.set_bubble(self.nvp)
        self.assertTrue(
            self.al_st.curr_ingrs == night_vision_potion.ingredients_patterns[0]
        )
        self.assertTrue(
            self.al_st.bubble.effects[0] == night_vision_potion.possible_effects[0][0]
        )

    def test_brewing_potion(self):
        """Тест главного метода brewing_potion'а"""

        # варка с нуля до зелья силы 2-го
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.assertTrue(self.al_st.bubble == awkward_potion)

        size_before = len(self.al_st)
        self.al_st.brewing_potion(nether_wart)
        size_after = len(self.al_st)
        self.assertEqual(size_before, size_after)

        self.al_st.brewing_potion(blaze_powder)
        self.assertTrue(self.al_st.bubble == strength_potion)

        self.al_st.brewing_potion(powder)
        self.assertTrue(self.al_st.bubble.is_explosive)

        self.al_st.brewing_potion(glowstone)
        self.assertFalse(self.al_st.bubble.is_lvl_up)
        self.assertFalse(self.al_st.bubble.is_duration_up)
        self.assertTrue(self.al_st.bubble.lvl == 2)
        self.assertTrue(
            self.al_st.bubble.effects[0] == strength[1]
        )
        self.assertTrue(
            self.al_st.bubble.duration == \
            strength_potion.durations_patterns.lvl_up
        )

    def test_brewing_potion_2(self):
        """Тест метода breawing_potion часть 2"""

        # варка начиная с зелья силы 2
        self.al_st.set_bubble(self.sp)

        self.al_st.brewing_potion(powder)
        self.assertTrue(self.al_st.bubble.is_explosive)

        self.al_st.brewing_potion(glowstone)
        self.assertFalse(self.al_st.bubble.is_lvl_up)
        self.assertFalse(self.al_st.bubble.is_duration_up)
        self.assertTrue(self.al_st.bubble.lvl == 2)
        self.assertTrue(
            self.al_st.bubble.effects[0] == strength[1]
        )
        self.assertTrue(
            self.al_st.bubble.duration == \
            strength_potion.durations_patterns.lvl_up
        )

    def test_brewing_potion_3(self):
        """Тест метода breawing_potion часть 3"""
        # варка с нуля зелья невидимости
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(golden_carrot)
        self.al_st.brewing_potion(fermented_spider_eye)

        self.assertTrue(self.al_st.bubble == invisibility_potion)

    def test_brewing_potion_4(self):
        """Тест метода breawing_potion часть 4"""
        # сварим начиная с зелья ночного зрения
        self.al_st.set_bubble(self.nvp)
        self.al_st.brewing_potion(fermented_spider_eye)
        self.assertEqual(self.al_st.bubble, invisibility_potion)

        self.al_st.brewing_potion(redstone)
        self.assertTrue(
            self.al_st.bubble.duration == \
            self.al_st.bubble.durations_patterns.extended,
        )

    def test_take_bubble(self):
        """Тест метода take_bubble"""

        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.assertTrue(self.al_st.bubble == awkward_potion)

        size_before = len(self.al_st)
        self.al_st.brewing_potion(nether_wart)
        size_after = len(self.al_st)
        self.assertEqual(size_before, size_after)

        self.al_st.brewing_potion(blaze_powder)

        potion = self.al_st.take_bubble()
        self.assertTrue(potion == strength_potion)

        self.assertFalse(self.al_st.bubble)
        self.assertFalse(self.al_st.curr_ingrs)

        self.al_st.set_bubble(potion)
        self.al_st.brewing_potion(powder)
        self.al_st.brewing_potion(redstone)
        potion = self.al_st.take_bubble()

        self.assertTrue(potion.is_explosive)
        self.assertFalse(potion.is_lvl_up)
        self.assertFalse(potion.is_duration_up)

        self.assertTrue(potion.effects[0] == strength[0])
        self.assertTrue(potion.duration == \
            potion.durations_patterns.extended
        )

    def test_brewing_potion_5(self):
        """Тест метода breawing_potion часть 5"""
        # сварим зелье замедление 2-мя путями

        # через зельку скорости, cварим его
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(sugar)
        self.al_st.brewing_potion(fermented_spider_eye)
        sp = self.al_st.take_bubble()
        self.assertTrue(sp == slowness_potion)

        # через зельку прыгучести, сварим его
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(rabbit_foot)
        self.al_st.brewing_potion(fermented_spider_eye)
        lp = self.al_st.take_bubble()
        self.assertTrue(lp == slowness_potion)

    def test_brewing_potion_6(self):
        """Тест метода breawing_potion часть 6"""
        # сварим зелье мгновенного урона 2-мя путями

        # через зельку здоровья, cварим его
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(glistering_melon_slice)
        self.al_st.brewing_potion(fermented_spider_eye)
        sp = self.al_st.take_bubble()
        self.assertTrue(sp == harming_potion)

        # через зельку отравления, сварим его
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(spider_eye)
        self.al_st.brewing_potion(fermented_spider_eye)
        lp = self.al_st.take_bubble()
        self.assertTrue(lp == harming_potion)

    def test_brewing_potion_7(self):
        """Тест метода breawing_potion часть 7"""

        # сварим зелье замедления прокаченное
        # редстоуном 2-мя спец. путями

        # через зелье прокаченное редом зелье прыгучести
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(rabbit_foot)
        self.al_st.brewing_potion(redstone)
        self.al_st.brewing_potion(fermented_spider_eye)
        potion = self.al_st.take_bubble()

        self.assertTrue(potion == slowness_potion)
        self.assertTrue(
            potion.duration == slowness_potion.durations_patterns.extended
        )
        self.assertTrue(not potion.is_lvl_up)
        self.assertTrue(not potion.is_duration_up)

        # через прокаченное редом зелье стремительности
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(sugar)
        self.al_st.brewing_potion(redstone)
        self.al_st.brewing_potion(fermented_spider_eye)
        potion = self.al_st.take_bubble()

        self.assertTrue(potion == slowness_potion)
        self.assertTrue(
            potion.duration == slowness_potion.durations_patterns.extended
        )
        self.assertTrue(not potion.is_lvl_up)
        self.assertTrue(not potion.is_duration_up)

    def test_brewing_potion_8(self):
        """Тест метода breawing_potion часть 8"""

        #сварим зелье вреда(lvl_up) 2-мя путями

        # через зелье здоровья(lvl_up+)
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(glistering_melon_slice)
        self.al_st.brewing_potion(glowstone)
        self.al_st.brewing_potion(fermented_spider_eye)
        potion = self.al_st.take_bubble()
        self.assertTrue(potion == harming_potion)
        self.assertTrue(potion.duration == 'instant')
        self.assertTrue(potion.lvl == 2)
        self.assertTrue(not potion.is_explosive)
        self.assertTrue(not potion.is_lvl_up)
        self.assertTrue(not potion.is_duration_up)

        # через зелье отравления(lvl_up+)
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(spider_eye)
        self.al_st.brewing_potion(glowstone)
        self.al_st.brewing_potion(fermented_spider_eye)
        potion = self.al_st.take_bubble()
        self.assertTrue(potion == harming_potion)
        self.assertTrue(potion.duration == 'instant')
        self.assertTrue(potion.lvl == 2)
        self.assertTrue(not potion.is_explosive)
        self.assertTrue(not potion.is_lvl_up)
        self.assertTrue(not potion.is_duration_up)

    def test_brewing_potion_9(self):
        """Тест метода breawing_potion часть 9"""

        # сварим зелье невидимости(extended)
        # через зелье ночного зрения(extended)
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(golden_carrot)
        self.al_st.brewing_potion(redstone)
        self.al_st.brewing_potion(fermented_spider_eye)
        print(self.al_st)

    def test_brewing_potion_10(self):
        """Тест метода breawing_potion часть 10"""

        # сварим зелье черепашьей мощи
        self.al_st.set_bubble(water_bubble)
        self.al_st.brewing_potion(nether_wart)
        self.al_st.brewing_potion(turtle_shell)
        # self.al_st.brewing_potion(glowstone)
        print(self.al_st)

    def test_create_all_potions(self):
        """Варка всех зелий по всем путям"""

        def show_potions(collections: list) -> None:
            """
            'Красиво' выводит на экран инфу о зельке
            """
            for p in collections:
                print(
                    f'{p.title} {p.lvl}\n'
                    f'{[str(e) for e in p.effects]} {p.duration}\n'
                    f'{[str(ingr) for ingr in p.ingredients]}\n\n'
                )

        result = []
        for p in POTIONS[2:]:
            for path_ingrs in p.ingredients_patterns:
                self.al_st.set_bubble(water_bubble)
                for ingr in path_ingrs:
                    self.al_st.brewing_potion(ingr)
                np = self.al_st.take_bubble()
                self.assertTrue(p == np)
                result.append(np)

                if np.is_lvl_up:
                    self.al_st.set_bubble(deepcopy(np))
                    self.al_st.brewing_potion(glowstone)
                    res = self.al_st.take_bubble()

                    for e, g_efs in zip(
                            res.effects, res.possible_effects
                    ):
                        if hasattr(g_efs, '__iter__'):
                            self.assertTrue(
                                e == g_efs[res.lvl - 1]
                            )
                        else:
                            self.assertTrue(
                                e == g_efs
                            )
                    result.append(res)

                if np.is_duration_up:
                    self.al_st.set_bubble(deepcopy(np))
                    self.al_st.brewing_potion(redstone)
                    res = self.al_st.take_bubble()

                    self.assertTrue(
                        res.duration == res.durations_patterns.extended
                    )
                    result.append(res)

        # если нужен красивый вывод
        # show_potions(result)


if __name__ == '__main__':
    unittest.main()