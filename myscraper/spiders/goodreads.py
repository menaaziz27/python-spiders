from json import load
from scrapy.loader import ItemLoader
from myscraper.items import QuoteItem
import scrapy

class GoodReadsSpider(scrapy.Spider):
    # identity
    name = 'goodreads'
    # requests
    def start_requests(self):
        url = 'https://www.goodreads.com/quotes?page=1'
        
        yield scrapy.Request(url=url, callback=self.parse)

    
     # response
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            loader = ItemLoader(item = QuoteItem(), selector = quote, response = response)
            loader.add_xpath("text", xpath = ".//div[@class='quoteText'][1]/text()[1]")
            loader.add_xpath("author", xpath = ".//div[@class='quoteText']/child::span")
            loader.add_xpath("tags", xpath = ".//div[@class='greyText smallText left']/child::a")
            yield loader.load_item()
            # yield {
            #     'text': quote.xpath(".//div[@class='quoteText'][1]/text()[1]").extract_first(),
            #     'author': quote.xpath(".//div[@class='quoteText']/child::span/text()").extract_first(),
            #     'tags': quote.xpath(".//div[@class='greyText smallText left']/child::a/text()").extract(),
            # }

        # get next page link
        next_page= response.selector.xpath("//a[@class='next_page']/@href").extract_first()
        # if not none request the next page
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        
