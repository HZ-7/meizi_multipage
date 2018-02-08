# -*- coding: utf-8 -*-
# 项目管道文件
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy,os
from meizi_multi.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
class MeiziMultiPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
#       获取图片路径
        imagsrc = item['image_src']
#       将图片链接提交给下载器
        yield scrapy.Request(imagsrc)


    # def process_item(self, item, spider):
    #     return item
    def item_completed(self, results, item, info):
#       在result中获取图片保存的实际路径
        image_path = [x['path'] for ok, x in results if ok]
#       为图片创建文件夹
        if not os.path.exists(IMAGES_STORE+item['image_title']):
            os.mkdir(IMAGES_STORE+item['image_title'])
#       为图片重命名
        os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+item['image_title']+"/"+item['image_alt']+".jpg")
