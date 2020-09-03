import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanspiderSpider(scrapy.Spider):
    name = 'maoyanspider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    
    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        items = []
        selector = Selector(response=response)
        movie_list = selector.xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movie_list:
            item = MaoyanItem()
            movie_name = movie.xpath('./div[1]/span[@class="name "]/text()').extract_first()
            catagories = movie.xpath('./div[2]/span/following-sibling::text()').extract_first().strip()
            release_date = movie.xpath('./div[4]/span/following-sibling::text()').extract_first().strip()
            yield item
