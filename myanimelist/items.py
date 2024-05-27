# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    title = scrapy.Field()
    title_english = scrapy.Field()
    score = scrapy.Field()
    rank = scrapy.Field()
    popularity = scrapy.Field()
    description = scrapy.Field()
    members = scrapy.Field()
