import scrapy
from ..items import OkItem


class Spyder(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        items = OkItem()
        box = response.css('article.product_pod')
        for i in box:
            title = i.css('a::text').extract()
            price = i.css('p.price_color::text').extract()
            items['book'] = title
            items['price'] = price

            yield items

        next = response.css('li.next a::attr(href)').get()
        if next is not None:
            yield response.follow(next, callback=self.parse)
