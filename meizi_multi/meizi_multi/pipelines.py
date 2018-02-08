# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy,os
from meizi_multi.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
class MeiziMultiPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imagsrc = item['image_src']
        yield scrapy.Request(imagsrc)


    # def process_item(self, item, spider):
    #     return item
    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not os.path.exists(IMAGES_STORE+item['image_title']):
            os.mkdir(IMAGES_STORE+item['image_title'])
        os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+item['image_title']+"/"+item['image_alt']+".jpg")