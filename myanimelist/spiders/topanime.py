import scrapy


class TopanimeSpider(scrapy.Spider):
    name = "topanime"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        for anime in response.css(".ranking-list"):
            yield {
                "title": anime.css("h3 a::text").get(),
                "url": anime.css("h3 a::attr(href)").get(),
            }
