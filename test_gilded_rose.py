# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2)]
        gr = GildedRose(items)

        gr.update_quality()
     
        assert gr.items[0] == Item(vest, 0, 3)
    
    def test_brie_item_should_increase_after_one_day(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0] == Item(brie, 1, 0)

    def test_quality_should_no_more_than_fifty(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 50)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0] == Item(brie, 1, 51)

if __name__ == '__main__':
    unittest.main()
