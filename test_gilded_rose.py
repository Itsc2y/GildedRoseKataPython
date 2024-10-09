# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_conjured_items_degrade_twice_as_fast_as_normal_items(self):
        name = "Conjured Mana Cake"
        items = [Item(name, 1, 2)]  
        gr = GildedRose(items)

        gr.update_quality()
        expected_item = Item(name, 0, 0) 
        assert (
            (gr.items[0].name == expected_item.name) and
            (gr.items[0].sell_in == expected_item.sell_in) and
            (gr.items[0].quality == expected_item.quality)
    )
        
    def test_conjured_items_degrade_twice_fast_after_sell_day(self):
        name = "Conjured Mana Cake"
        items = [Item(name, -1, 4)]  
        gr = GildedRose(items)

        gr.update_quality()
        expected_item = Item(name, -2, 0) 
        assert (
            (gr.items[0].name == expected_item.name) and
            (gr.items[0].sell_in == expected_item.sell_in) and
            (gr.items[0].quality == expected_item.quality)
    )
    
    def test_conjured_items_quality_no_less_then_0(self):
        name = "Conjured Mana Cake"
        items = [Item(name, -1, 3)]  
        gr = GildedRose(items)

        gr.update_quality()
        expected_item = Item(name, -2, 0) 
        assert (
            (gr.items[0].name == expected_item.name) and
            (gr.items[0].sell_in == expected_item.sell_in) and
            (gr.items[0].quality == expected_item.quality)
    )

if __name__ == '__main__':
    unittest.main()
