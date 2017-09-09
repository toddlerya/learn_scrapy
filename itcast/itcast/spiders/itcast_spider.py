#!/usr/bin/env python
# encoding: utf-8
# author: toddlerya

import scrapy
from itcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allow_domain = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath('//div[@class="li_txt"]')

        for node in node_list:
            item = ItcastItem()
            name = node.xpath('h3/text()').extract()
            title = node.xpath('h4/text()').extract()
            info = node.xpath('p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]


            yield item



