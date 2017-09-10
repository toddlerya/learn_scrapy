# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class CodingPipeline(object):
    def __init__(self):
        self.w = open("coding_tweet.jl", 'wb')

    def process_item(self, item, spider):
        info = (json.dumps(dict(item), ensure_ascii=False) + '\n').encode('utf-8')
        self.w.write(info)
        return item

    def close_spider(self, spider):
        self.w.close()

