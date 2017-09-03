#!/usr/bin/env python
# encoding: utf-8
# auther: toddlerya

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                    'text': quote.xpath('span[@class="text"]/text()').extract_first(),
                    'author': quote.xpath('span/small[@class="author"]/text()').extract_first(),
                    'tags': quote.xpath('div/a[@class="tag"]/text()').extract(),
           }

