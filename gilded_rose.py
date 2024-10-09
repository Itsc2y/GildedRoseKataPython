# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in -= 1

            if item.name == "Aged Brie":
                self.increase_quality(item)
                if item.sell_in < 0:
                    self.increase_quality(item)
                continue


            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                else:
                    self.increase_quality(item)
                    if item.sell_in < 10:
                        self.increase_quality(item)
                    if item.sell_in < 5:
                        self.increase_quality(item)
                continue

            if item.name == "Conjured Mana Cake":
                self.decrease_quality(item, 2)
                if item.sell_in < 0:
                    self.decrease_quality(item, 2)
                continue
            
            self.decrease_quality(item)
            if item.sell_in < 0:
                self.decrease_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item, amount = 1):
        if item.quality > 0:
            item.quality -= amount
            if item.quality < 0:
                item.quality = 0
