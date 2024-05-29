# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyanimelistPipeline:
    def process_item(self, item, spider):
        for key in item.fields:
            if (
                key not in item
                or not item[key]
                or isinstance(item[key], str)
            ):
                continue
            texts = [
                t.strip()
                for t in item[key]
                if t.strip() and key not in t.lower()
            ]
            if key in ["producers", "studios", "genres"]:
                item[key] = ", ".join(texts)
            elif key in ["score", "ranked"]:
                item[key] = " ".join(texts[:1])
            else:
                item[key] = " ".join(texts)
        return item
