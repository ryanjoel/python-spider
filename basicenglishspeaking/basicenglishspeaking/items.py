# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicenglishspeakingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    urls = scrapy.Field()
    text = scrapy.Field()
#     def handle_addr(addres):
#         addres = addres.replace('\t','')
#         return 
    pass
