# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HrTencentCrawlSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    position_addr = scrapy.Field()
    position_date = scrapy.Field()
    position_link = scrapy.Field()

    position_utcnow = scrapy.Field()
    spider_name = scrapy.Field()


class PositionItem(scrapy.Item):
    """
        存储职位详情页数据
    """
    position_link = scrapy.Field()
    # 工作职责
    position_zhize = scrapy.Field()
    # 工作要求
    position_yaoqiu = scrapy.Field()
    # 记录抓取时间
    utcnow = scrapy.Field()
    # 记录数据源
    source = scrapy.Field()
