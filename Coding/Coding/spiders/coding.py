# -*- coding: utf-8 -*-
import scrapy
import json
from Coding.items import CodingItem


class CodingSpider(scrapy.Spider):
    name = 'coding'
    allowed_domains = ['coding.net']
    start_urls = ['https://coding.net/api/tweet/public_tweets?size=100&filter=false']

    def parse(self, response):

        load_json = json.loads(response.body, encoding='utf-8')

        resp_code = load_json['code']

        content_json = load_json['data']

        if resp_code is not 0:
            return

        for content in content_json:
            item = CodingItem()

            # 冒泡信息
            item['tweet_id'] = content['id']
            item['tweet_owner_id'] = content['owner_id']
            item['tweet_created_at'] = content['created_at']
            item['tweet_sort_time'] = content['sort_time']
            item['tweet_likes'] = content['likes']
            item['tweet_rewards'] = content['rewards']
            item['tweet_comments'] = content['comments']
            item['tweet_comment_list'] = content['comment_list']
            item['tweet_device'] = content['device']
            item['tweet_location'] = content['location']
            item['tweet_coord'] = content['coord']
            item['tweet_address'] = content['address']
            item['tweet_content'] = content['content']
            item['tweet_activity_id'] = content['activity_id']
            item['tweet_liked'] = content['liked']
            item['tweet_like_users'] = content['like_users']
            item['tweet_reward_users'] = content['reward_users']
            # 冒泡发布人信息
            item['owner_job'] = content['owner']['job']
            item['owner_sex'] = content['owner']['sex']
            item['owner_location'] = content['owner']['location']
            item['owner_company'] = content['owner']['company']
            item['owner_slogan'] = content['owner']['slogan']
            item['owner_avatar'] = content['owner']['avatar']
            item['owner_created_at'] = content['owner']['created_at']
            item['owner_last_logined_at'] = content['owner']['last_logined_at']
            item['owner_global_key'] = content['owner']['global_key']
            item['owner_name_pinyin'] = content['owner']['name_pinyin']
            item['owner_path'] = content['owner']['path']
            item['owner_status'] = content['owner']['status']
            item['owner_id'] = content['owner']['id']
            item['owner_vip'] = content['owner']['vip']
            item['owner_follows_count'] = content['owner']['follows_count']
            item['owner_fans_count'] = content['owner']['fans_count']
            item['owner_followed'] = content['owner']['followed']
            item['owner_follow'] = content['owner']['follow']

            yield item