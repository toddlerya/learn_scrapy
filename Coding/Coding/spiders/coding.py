# -*- coding: utf-8 -*-
import scrapy


class CodingSpider(scrapy.Spider):
    name = 'coding'
    allowed_domains = ['coding.net']
    start_urls = ['http://coding.net/']

    def parse(self, response):
        pass
