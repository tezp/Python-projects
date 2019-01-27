# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('I am in ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'Author ': quote.css('small.author::text').extract_first(),
                'Text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }
        author_urls = response.css('div.quote>span > a::attr(href)').extract()
        for url in author_urls:
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_author_details)

        next_page_url = response.urljoin(response.css('li.next > a::attr(href)').extract_first())
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_author_details(self, response):
        items = {
            'author_name': response.css('h3.author-title::text')[0].extract(),
            'dob': response.css('span.author-born-date::text')[0].extract()
        }
        yield items
