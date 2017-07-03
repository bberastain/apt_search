import scrapy


class Practice(scrapy.Spider):
    name = "practice"

    def start_requests(self):
        urls = [
            'https://sfbay.craigslist.org/search/eby/hhh?nh=48&nh=58&nh=61&nh=62&nh=66&max_price=2000&bedrooms=2&availabilityMode=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for listing in response.css('.hdrlnk'):
            yield {
                'text': listing.extract(),
            }
