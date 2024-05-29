# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    title = scrapy.Field()
    title_english = scrapy.Field()
    description = scrapy.Field()

    type = scrapy.Field()
    episodes = scrapy.Field()
    status = scrapy.Field()
    aired = scrapy.Field()
    premiered = scrapy.Field()
    broadcast = scrapy.Field()
    producers = scrapy.Field()
    studios = scrapy.Field()
    source = scrapy.Field()
    genres = scrapy.Field()
    demographic = scrapy.Field()
    duration = scrapy.Field()
    rating = scrapy.Field()

    score = scrapy.Field()
    ranked = scrapy.Field()
    popularity = scrapy.Field()
    members = scrapy.Field()
    favorites = scrapy.Field()
