import scrapy


class TopanimeSpider(scrapy.Spider):
    name = "topanime"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        for anime in response.css(".ranking-list"):
            url = anime.css("h3 a::attr(href)").get()
            yield scrapy.Request(url, callback=self.parse_anime)

    def parse_anime(self, response):
        title = response.css(".title-name strong::text").get()
        title_english = response.css(".title-english::text").get()
        score = response.css(".score-label::text").get()
        rank = response.css(".ranked::text").get()
        popularity = response.css(".popularity::text").get()
        description_texts = response.css(
            "p[itemprop='description']::text"
        ).getall()
        members = response.css(".members strong::text").get()
        yield {
            "title": title,
            "title_english": title_english,
            "score": score,
            "rank": rank,
            "popularity": popularity,
            "description": " ".join(
                [
                    clean_text
                    for text in description_texts
                    if (clean_text := text.strip())
                ]
            ),
            "members": members,
        }
