# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CodingItem(scrapy.Item):
    # define the fields for your item here like:
    # tweet info
    tweet_id = scrapy.Field()
    tweet_owner_id = scrapy.Field()
    tweet_created_at = scrapy.Field()
    tweet_sort_time = scrapy.Field()
    tweet_likes = scrapy.Field()
    tweet_rewards = scrapy.Field()
    tweet_comments = scrapy.Field()
    tweet_comment_list = scrapy.Field()  # 评论人列表
    tweet_device = scrapy.Field()
    tweet_location = scrapy.Field()
    tweet_coord = scrapy.Field()
    tweet_address = scrapy.Field()
    tweet_content = scrapy.Field()
    tweet_activity_id = scrapy.Field()
    tweet_liked = scrapy.Field()
    tweet_like_users = scrapy.Field()  # 点赞人列表
    tweet_reward_users = scrapy.Field()  # 打赏人列表

    # tweet owner info
    owner_job = scrapy.Field()
    owner_sex = scrapy.Field()
    owner_location = scrapy.Field()
    owner_company = scrapy.Field()
    owner_slogan = scrapy.Field()
    owner_avatar = scrapy.Field()
    owner_created_at = scrapy.Field()
    owner_last_logined_at = scrapy.Field()
    owner_global_key = scrapy.Field()
    owner_name = scrapy.Field()
    owner_name_pinyin = scrapy.Field()
    owner_path = scrapy.Field()
    owner_status = scrapy.Field()
    owner_id = scrapy.Field()
    owner_vip = scrapy.Field()
    owner_follows_count = scrapy.Field()
    owner_fans_count = scrapy.Field()
    owner_followed = scrapy.Field()
    owner_follow = scrapy.Field()