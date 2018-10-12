# -*- coding: utf-8 -*-
import scrapy


class XcSpider(scrapy.Spider):
    name = 'xc'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def parse(self, response):
        pass
