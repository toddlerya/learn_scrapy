# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class TencentPipeline(object):
    def __init__(self):
        self.w = open("tencent_position.jl", 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        content = content.encode('utf-8')
        self.w.write(content)
        return item

    def close_spider(self, spider):
        self.w.close()