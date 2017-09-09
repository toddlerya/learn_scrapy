# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    offset = 0
    base_url = "http://hr.tencent.com/position.php?&start={0}"
    first_url = base_url.format(offset)
    start_urls = [first_url]

    def parse(self, response):

        position_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for position in position_list:
            item = TencentItem()
            item['positionName'] = position.xpath('td[1]/a/text()').extract_first()
            item['positionLink'] = "http://hr.tencent.com/" + position.xpath('td[1]/a/@href').extract_first()
            positionType = position.xpath('td[2]/text()').extract()
            if len(positionType):
                item['positionType'] = positionType
            else:
                item['positionType'] = ""
            item['peopleNumber'] = position.xpath('td[3]/text()').extract_first()
            item['workLocation'] = position.xpath('td[4]/text()').extract_first()
            item['publishTime'] = position.xpath('td[5]/text()').extract_first()

            yield item

        self.offset += 10
        print 'offset', self.offset
        next_url = self.base_url.format(self.offset)
        print 'next_url', next_url
        if position_list.extract_first() is not None:
            yield scrapy.Request(next_url, callback=self.parse)
