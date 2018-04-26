# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from .items import HrTencentCrawlSpiderItem, PositionItem
import json


class HrTencentCrawlSpiderPipeline(object):
    def open_spider(self, spider):
        self.f = open('tencent_list.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, HrTencentCrawlSpiderItem):
            item['position_utcnow'] = str(datetime.utcnow())
            item['spider_name'] = spider.name

            self.f.write(json.dumps(dict(item)) + ',\n')
        return item

    def close_spider(self, spider):
        self.f.close()

class PositionCrawlSpiderPipeline(object):
    def open_spider(self, spider):
        self.f = open('position.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            item['utcnow'] = str(datetime.utcnow())
            item['source'] = spider.name

            self.f.write(json.dumps(dict(item)) + ',\n')
        return item

    def close_spider(self, spider):
        self.f.close()


