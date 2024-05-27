# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyanimelistPipeline:
    def process_item(self, item, spider):
        item["description"] = " ".join(
            [
                clean_text
                for text in item["description"]
                if (clean_text := text.strip())
            ]
        )
        return item
