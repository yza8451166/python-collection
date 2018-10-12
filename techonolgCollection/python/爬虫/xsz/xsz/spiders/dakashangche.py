# -*- coding: utf-8 -*-
import scrapy
import sys,io
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.http import Request
from ..items import XszItem
from scrapy.dupefilters import RFPDupeFilter
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
class DakashangcheSpider(scrapy.Spider):
    name = 'dakashangche'
    allowed_domains = ['dakashangche.org']
    start_urls = ['https://www.dakashangche.org/']
    download_delay = 2

    def parse(self, response):
        # print(response.text)
        print(1)
        hxs_img = Selector(response=response).xpath('//div[@class="post-info"]/div[@class="post-thumbnail"]\
        /a/img/@lazydata-src').extract()
        hxs_page = Selector(response=response).xpath('//div[@class="page-nav"]/a/@href').extract()
        # print(hxs_img)
        # print(type(hxs_page))

        item = XszItem()
        item['image_urls'] = hxs_img
        yield item



        img_list= []
        for obj in hxs_img:
            print(obj)
        #
        #     item = XszItem()
        #
        #     srcs = obj.xpath('.//div[@class="post-thumbnail"]/a/img/@lazydata-src').extract()
        #     print(srcs)
        #     item['image_urls'] = srcs
        #     yield item



        for i in hxs_page:

            yield Request(url=i,callback=self.parse)

            print(i)



        # print(2)

            # img_src = obj.xpath('.//div[@class="post-thumbnail"]/a/img/@src').extract()
            # title = obj.xpath('.//h2[@class="post-title"]/a/text()').extract()

            # print(img_src)
            # print(title)
            # item_obj = XszItem(title=title,img_src=img_src)
            # yield item_obj


