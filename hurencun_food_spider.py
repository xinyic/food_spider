# encoding: utf-8

import scrapy

FEED_EXPORT_ENCODING = 'utf-8'

class FoodSpider(scrapy.Spider):
    name = "food"
    start_urls = [
        'http://huarencun.com/index.php/ae-e-grocery-1.html',
    ]

    def parse(self, response):
        for item in response.css('div.col-main li.item'):
            yield {
                'name': item.css('h5 a::text').extract_first().strip(),
                'price': item.css('span.price::text').extract_first().strip(),
                'online_store_name': u'华人村',
                'link': item.css("h5 a::attr('href')").extract_first()
            }

        next_page = response.css("a.next::attr('href')").extract_first()
        print("=" * 80)
        print(next_page)
        print("=" * 80)
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)

