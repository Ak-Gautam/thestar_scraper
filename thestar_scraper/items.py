import scrapy

class ThestarScraperItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()  # Optional: adjust based on what you need
