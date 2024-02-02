import scrapy
from thestar_scraper.items import ThestarScraperItem

class TheStarSpider(scrapy.Spider):
    name = 'thestar'
    allowed_domains = ['www.thestar.com.my']
    start_urls = ['https://www.thestar.com.my/']

    def parse(self, response):
        # Targeting <a> tags directly with the specific attributes
        articles = response.xpath('//a[@data-content-type="Article"]')

        for article in articles:
            item = ThestarScraperItem()
            item['title'] = article.xpath('normalize-space(.)').get()  # Using normalize-space() to trim whitespace
            item['url'] = response.urljoin(article.xpath('@href').get())

            yield item