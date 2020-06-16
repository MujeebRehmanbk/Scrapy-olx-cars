# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title =scrapy.Field()
    description = scrapy.Field()
    display_date = scrapy.Field()
    Picture_link = scrapy.Field()
    Location = scrapy.Field()
    On_road = scrapy.Field()
    Price = scrapy.Field()
    
    
    