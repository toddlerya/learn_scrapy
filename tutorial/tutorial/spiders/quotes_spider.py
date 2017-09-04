#!/usr/bin/env python
# encoding: utf-8
# auther: toddlerya

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                    'text': quote.xpath('span[@class="text"]/text()').extract_first(),
                    'author': quote.xpath('span/small[@class="author"]/text()').extract_first(),
                    'tags': quote.xpath('div/a[@class="tag"]/text()').extract(),
           }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            next_page = response.urljoin(next_page_url)
            yield scrapy.Request(next_page, callback=self.parse)

