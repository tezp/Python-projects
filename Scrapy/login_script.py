# -*- coding: utf-8 -*-
import scrapy


class LoginScriptSpider(scrapy.Spider):
    name = 'login_script'
    login_url = 'http://quotes.toscrape.com/login'
    start_urls=[login_url]

    def parse(self, response):
        csrf_token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        data = {
                'csrf_token':csrf_token,
                'username':'123',
                'password':'123'
                }
        yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.parse_after_login)
        
    #data after login .
    def parse_after_login(self,response):
        for q in response.css('div.quote'):
            yield{
                    'author_name':q.css('small.author::text')[0].extract(),
                    'author_url':q.css('small.author~a[href*="goodreads.com"]::attr(href)').extract_first()
                    
                    }
