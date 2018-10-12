# -*- coding: utf-8 -*-
import sys
import io
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
from scrapy.http.cookies import CookieJar

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']
    download_delay = 2
    visted_urls = set()
    cookie_dict =None
    def parse(self, response):
        # print(response.text)
        # hxs = Selector(response=response).xpath('//a[re:test(@href,"/all/hot/recent/\d+")]/@href').extract()
        # for url in hxs:
        #     # print(url)
        #     md5_url = self.md5(url)
        #     if md5_url in self.visted_urls:
        #         pass
        #     else:
        #         print(url)
        #         url = 'http://dig.chouti.com%s' % url
        #         self.visted_urls.add(md5_url)
        #         yield Request(url=url, callback=self.parse)
        cookie_obj =CookieJar()
        cookie_obj.extract_cookies(response,response.request)
        print(cookie_obj._cookies)
        #带上用户名密码+cookie
        yield Request(
            url="http://dig.chouti.com/login",
            method='POST',
            body="phone=8618217780492&password=xc8451166&oneMonth=1",
            headers={'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"},
            cookies=cookie_obj._cookies,
            callback=self.check_login
        )
    def check_login(self,response):
        print(response.text)
        yield Request(url="http://dig.chouti.com/",callback=self.good)

    def good(self,response):
        id_list = Selector(response=response).xpath('//div[@share-linkid]/@share-linkid').extract()
        for nid in id_list:
            print(nid)
            url = "http://dig.chouti.com/link/vote?linksId=%s" % nid
            yield Request(
                url=url,
                method="POST",
                cookies=self.cookie_dict,
                callback=self.show
            )

        # page_urls = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        # for page in page_urls:
        #     url = "http://dig.chouti.com%s" % page
        #     yield Request(url=url,callback=self.good)


    def show(self,response):
        print(response.text)











    def md5(self, url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()
