# -*- coding: utf-8 -*-
import scrapy,re

from meizi_multi.items import MeiziMultiItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.meizitu.com']
    base_url = 'http://www.meizitu.com/a/pure'
    offset = 1
#    拼接出起始url
    start_urls = [base_url+"_"+str(offset)+".html"]

    def parse(self, response):
#       获取所有图片所在节点的列表
        node_list = response.xpath('//*[@id="maincontent"]/div[1]/ul/li')
        page_num = 0
#       从html节点中获取所要爬取的循环次数
        if len(response.css('#wp_page_numbers > ul > li:last-child > a::attr(href)')) != 0:
            last_li = response.css('#wp_page_numbers > ul > li:last-child > a::attr(href)').extract()[0]
            page_num = re.findall('\d{2}',last_li)[0]
        for node in node_list:
            # page_title = node.xpath('./div/h3/a//text()').extract()[0]
#           获取单页图片URL
            page_url = node.xpath('./div/div/a/@href').extract()[0]
#           将URL转交给下面的页面处理函数
            yield  scrapy.Request(url=page_url,callback=self.parse_page)

        if self.offset < int(page_num)+1:
            self.offset += 1
            next_url = self.base_url + "_" + str(self.offset) + ".html"
            yield scrapy.Request(url=next_url,callback=self.parse)

    def parse_page(self,response):
#         根据URL获取图片的标题，链接等
         image_title = response.xpath('//*[@id="maincontent"]/div[1]/div[1]/h2/a//text()').extract()[0]
         image_list = response.xpath('//*[@id="maincontent"]/div[2]/p[1]/img | //*[ @ id = "picture"]/p/img')
         for image in image_list:
             image_src = image.xpath('./@src').extract()[0]
             image_alt = image.xpath('./@alt').extract()[0]
#            将图片的标题、链接存储在item中，用来给图片创建文件夹、文件名
             item = MeiziMultiItem()
             item['image_title'] = image_title
             item['image_src'] = image_src
             item['image_alt'] = image_alt
#            将item提交给管道文件处理
             yield item
