# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 存取爬取所需数据
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiziMultiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # page_title = scrapy.Field()
    image_title = scrapy.Field()
    image_src = scrapy.Field()
    image_alt = scrapy.Field()
    # page_url = scrapy.Field()
