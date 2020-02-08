# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class VacsSpider(scrapy.Spider):
    name = 'vacs'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://seattle.craigslist.org/search/skc/vac']

    def parse(self, response):
        vacs=response.xpath('//p[@class="result-info"]')
        for vac in vacs:
            title =  vac.xpath('a/text()').extract_first()
            posted_date = vac.xpath('time[@class="result-date"]/text()').extract_first() #Posted Date Answer
            rental_price = vac.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first() #Rental Price Answer
            housing = vac.xpath('span[@class="result-meta"]/span[@class="housing"]/text()').extract_first("")[21:-29] #No of Bedrooms
            address = vac.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1] #Neighborhood
            url = vac.xpath('a/@href').extract_first()
            
            yield Request(url,callback=self.parse_page, meta={'Title':title, 'Posted Date':posted_date, 'Rental Price':rental_price, '#Bedrooms':housing, "Neighborhood":address})
            
        #titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract() # Title
        #for title in titles:
            #yield{'Title':title} #convert to dictionary
            
    def parse_page(self, response):
        description = "".join(line for line in response.xpath('//section[@id="postingbody"]/text()').extract()) #Description
        response.meta['Description'] = description.strip() #(4) remove spaces at the beginning
        
        #ad_text = "".join(line for line in response.xpath('//p[@class="attrgroup"/span[1]/b/text()').extract_first()
        #response.meta['Ad Text'] = ad_text #Still need to work on this.
                          
        yield response.meta
        pass
