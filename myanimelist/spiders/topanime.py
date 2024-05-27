import scrapy

from myanimelist.items import AnimeItem


class TopanimeSpider(scrapy.Spider):
    name = "topanime"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        for anime in response.css(".ranking-list"):
            url = anime.css("h3 a::attr(href)").get()
            yield scrapy.Request(url, callback=self.parse_anime)

    def parse_anime(self, response):
        item = AnimeItem()
        item["title"] = response.css(".title-name strong::text").get()
        item["title_english"] = response.css(".title-english::text").get()
        item["score"] = response.css(".score-label::text").get()
        item["rank"] = response.css(".ranked strong::text").get()
        item["popularity"] = response.css(".popularity strong::text").get()
        item["members"] = response.css(".members strong::text").get()
        item["description"] = response.css("p[itemprop='description']::text").getall()
        yield item
