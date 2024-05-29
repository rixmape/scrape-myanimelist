import scrapy

from myanimelist.items import AnimeItem


class TopanimeSpider(scrapy.Spider):
    name = "topanime"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]
    anime_limit = 500
    anime_count = 0

    def parse(self, response):
        for anime in response.css(".ranking-list"):
            url = anime.css("h3 a::attr(href)").get()
            yield scrapy.Request(url, callback=self.parse_anime)
            self.anime_count += 1

            if self.anime_count >= self.anime_limit:
                break

        if self.anime_count < self.anime_limit:
            next_page_url = response.css("a.next::attr(href)").get()
            if next_page_url is not None:
                next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(next_page_url, callback=self.parse)

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
