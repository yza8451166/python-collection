# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import requests
import os
from . import settings

class XszPipeline(object):

    def __init__(self, conn_str):
        self.conn_str = conn_str

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        conn_str = crawler.settings.get('DB')
        return cls(conn_str)

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        self.conn = open(self.conn_str, 'a')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.conn.close()

    def process_item(self, item, spider):
        img = "%s\n%s\n\n" % (item['title'], item['img_src'])
        f = open('news1.json', 'a')
        f.write(img)
        f.close()

        return item  # 交给下一个
        # raise DropItem()#丢弃


class imgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print(3)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item


class ImageDownloadPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:  # 如何‘图片地址’在项目中
            images = []  # 定义图片空集

            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images
        return item