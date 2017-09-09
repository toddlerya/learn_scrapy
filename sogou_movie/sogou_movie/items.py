# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SogouMovieItem(scrapy.Item):
    # define the fields for your item here like:
    detail_page_url = scrapy.Field()
    cover_img_url = scrapy.Field()
    duration = scrapy.Field()
    movie_name = scrapy.Field()
    movie_describe = scrapy.Field()
    performers = scrapy.Field()
    director = scrapy.Field()
    movie_type = scrapy.Field()
    score = scrapy.Field()
    play_url = scrapy.Field()
