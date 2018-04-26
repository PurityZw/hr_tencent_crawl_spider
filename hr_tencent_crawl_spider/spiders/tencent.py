# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hr_tencent_crawl_spider.items import HrTencentCrawlSpiderItem, PositionItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?']

    rules = (
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'), callback='parse_page', follow=False),
    )

    def parse_item(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            i = HrTencentCrawlSpiderItem()

            i['position_name'] = node.xpath('./td[1]/a/text()').extract_first()
            i['position_type'] = node.xpath('./td[2]/text()').extract_first()
            i['position_num'] = node.xpath('./td[3]/text()').extract_first()
            i['position_addr'] = node.xpath('./td[4]/text()').extract_first()
            i['position_date'] = node.xpath('./td[5]/text()').extract_first()
            i['position_link'] = node.xpath('./td[1]/a/@href').extract_first()

            yield i


    def parse_page(self, response):
        item = PositionItem()
        """
        :param response:
        :return:
        """

        item['position_link'] = response.url
        item["position_zhize"] = "; ".join(response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract())
        item["position_yaoqiu"] = "; ".join(response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract())

        yield item