import scrapy

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
        item = AnimeItem()
        item["title"] = response.css(".title-name strong::text").get()
        item["title_english"] = response.css(".title-english::text").get()
        item["description"] = response.css("p[itemprop='description']::text").getall()

        for div in response.css(".spaceit_pad"):
            label = div.css(".dark_text::text").get()
            if label is None:
                continue

            key = label.lower().replace(":", "")
            if key in item.fields:
                if key in ["demographic", "producers", "studios", "genres"]:
                    selector = "a::text"
                else:
                    selector = "::text"
                item[key] = div.css(selector).getall()
        yield item
