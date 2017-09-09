#!/usr/bin/env python
# encoding: utf-8
# auther: toddlerya

import scrapy
from sogou_movie.items import sogouMovieItem


class sogouSpider(scrapy.Spider):
    name = "sogou_movie"
    allow_domain = ["kan.sogou.com"]
    start_urls = ["http://kan.sogou.com/dianying/----/"]

    def parse(self, response):
        for movie in response.xpath('//div[@class="cell cf"]'):
            info = movie.xpath('div[@class="infor"]')
            info_p = info.xpath('dl[@class="cf"]')
            item = sogouMovieItem()
            yield {
                    "detail_page_url": "http://kan.sogou.com" + movie.xpath('a/@href').extract_first(),
                    "cover_img_url": movie.xpath('a/img/@src').extract_first(),
                    "duration": movie.xpath('a/p[@class="text_over"]/text()').extract_first().split()[1],
                    "movie_name": info.xpath('p[@class="tit"]/a/text()').extract_first(),
                    "movie_describe": info.xpath('p[@class="descr"]/text()').extract_first(),
                    "performers": info_p[0].xpath('dd/a/text()').extract(),
                    "director": info_p[1].xpath('dd/a/text()').extract(),
                    "movie_type": info_p[2].xpath('dd/a/text()').extract(),
                    "score": info.xpath('dl[@class="commit cf"]/dd/span/text()').extract_first(),
                    "play_url": "http://kan.sogou.com" + info.xpath('div[@class="btn-wrap"]/a/@href').extract_first(),
            }


            next_page_url = response.xpath('//div[@class="page_num"]/a[@class="next"]/@href').extract_first()
            if next_page_url is not None:
                next_page = response.urljoin(next_page_url)
                yield scrapy.Request(next_page, callback=self.parse)

