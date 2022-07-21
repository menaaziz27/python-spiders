import scrapy

class GoodReadsSpider(scrapy.Spider):
    # identity
    name = 'goodreads'
    # requests
    def start_requests(self):
        urls = [
            'https://www.goodreads.com/quotes?page=1',
            'https://www.goodreads.com/quotes?page=2',
            'https://www.goodreads.com/quotes?page=3',
            'https://www.goodreads.com/quotes?page=4',
            'https://www.goodreads.com/quotes?page=5',
            'https://www.goodreads.com/quotes?page=6',
            'https://www.goodreads.com/quotes?page=7',
            'https://www.goodreads.com/quotes?page=8',
            'https://www.goodreads.com/quotes?page=9',
            'https://www.goodreads.com/quotes?page=10',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
     # response
    def parse(self, response):
        page_number = response.url.split('=')[1]
        _file = f'${page_number}.html'
        with open(_file, 'wb') as f: 
            f.write(response.body)
