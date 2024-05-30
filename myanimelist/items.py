import scrapy
from itemloaders.processors import Join, MapCompose
from w3lib.html import remove_tags


def clean_text(text):
    cleaned = text.replace("\r", " ").replace("\n", " ")
    return " ".join(cleaned.split())


def normalize_number(text):
    return text.replace(",", "").replace("#", "").strip()


class AnimeItem(scrapy.Item):
    title_original = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    title_english = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    description = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_text),
    )

    type = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    episodes = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    status = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    aired = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    premiered = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    broadcast = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    source = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    demographic = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    duration = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    rating = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )
    score = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
    )

    ranked = scrapy.Field(
        input_processor=MapCompose(remove_tags, normalize_number),
    )
    popularity = scrapy.Field(
        input_processor=MapCompose(remove_tags, normalize_number),
    )
    members = scrapy.Field(
        input_processor=MapCompose(remove_tags, normalize_number),
    )
    favorites = scrapy.Field(
        input_processor=MapCompose(remove_tags, normalize_number),
    )

    studios = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join(", "),
    )
    producers = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join(", "),
    )
    genres = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join(", "),
    )
