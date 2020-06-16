# -*- coding: utf-8 -*-
import scrapy
import json
import csv
from .. items import OlxItem

class OlxbotSpider(scrapy.Spider):

    name = 'olxbot'
    #allowed_domains = ['olx.com']
    url = 'https://www.olx.com.pk/api/relevance/search?category=84&facet_limit=100&location=1000001&location_facet_limit=20&&user=1729bfb42e6xb977cde'
     
     def start_requests(self):
         yield scrapy.Request(url = self.start_urls , callback=self.parse)
     
    def start_requests(self):
        for page in range(0,20):    # For pagination
        
            yield scrapy.Request(url=self.url +'&page='+ str(page),callback =self.parse )
   
	 
	custom_settings = {
        'FEED_EXPORT_FIELDS': ["title","description","display_date","Picture_link","Location","On_road","Price"],
        'FEED_URI' : 'olxfeeds.csv',
        'FEED_FORMAT' : 'csv'  
         #specifies exported fields and order
    	}

    def parse(self, response):
        items =OlxItem()
        data = response.text 
        data =json.loads(data)
        for loader in data['data']:  # to load 'data' key ,values of which contains the following for itteration.

                title        = loader['title']
                description  = loader['description'].replace("\n","")
                display_date = loader['display_date']
                Picture_link     = loader['images'][1]['full']['url']
                Location = loader['locations_resolved']['ADMIN_LEVEL_3_name'],loader['locations_resolved']['ADMIN_LEVEL_1_name'],loader['locations_resolved']['COUNTRY_name']
                On_road      = loader['main_info']
                Price        = loader['price']['value']['display']

                items['title']           =title
                items['description']     =description
                items['display_date']    =display_date
                items['Picture_link']    =Picture_link
                items['Location']        =Location
                items['On_road']         =On_road

                items['Price']           =Price
                yield items
            
      