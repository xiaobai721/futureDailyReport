# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FuturedailyreportItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class czceItem(Item):
    Symbol = Field()
    date = Field()
    storageID = Field()
    storageName = Field()
    year = Field()
    level = Field()
    brand = Field()
    number = Field()
    dailyChange = Field()
    effectivePredict = Field()
    premium = Field()
