# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import scrapy
from w3lib.html import remove_tags

def remove_quotations(value):
    return value.replace("\n", "").replace(u"\u201d", '').replace(u"\u201c", '')

class QuoteItem(scrapy.Item):
    text = scrapy.Field(
        input_processor = MapCompose(str.strip, remove_quotations),
        output_processor = TakeFirst()
    )
    author = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_quotations, str.strip),
        output_processor = TakeFirst()
    )

    tags = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(",")
    )
