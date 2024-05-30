import scrapy
from scrapy.loader import ItemLoader

from myanimelist.items import AnimeItem


class TopanimeSpider(scrapy.Spider):
    name = "topanime"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]
    anime_count = 0

    def parse(self, response):
        anime_limit = getattr(self, "anime_limit", 50)
        if anime_limit is not None:  # TODO: Improve error handling
            anime_limit = int(anime_limit)

        for anime in response.css(".ranking-list"):
            url = anime.css("h3 a::attr(href)").get()
            yield scrapy.Request(url, callback=self.parse_anime)
            self.anime_count += 1

            if self.anime_count >= anime_limit:
                break

        if self.anime_count < anime_limit:
            next_page_url = response.css("a.next::attr(href)").get()
            if next_page_url is not None:
                next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_anime(self, response):
        loader = ItemLoader(item=AnimeItem(), response=response)
        loader.add_css('title_original', '.title-name')
        loader.add_css('title_english', '.title-english')
        loader.add_css('description', "p[itemprop='description']")

        for div in response.css(".spaceit_pad"):
            label = div.css(".dark_text::text").get()
            if label is None:
                continue

            key = label.lower().replace(":", "")
            if key in loader.item.fields:
                if key in ["demographic", "producers", "studios", "genres"]:
                    selector = "a::text"
                else:
                    selector = "::text"
                loader.add_value(key, div.css(selector).getall())
        yield loader.load_item()
