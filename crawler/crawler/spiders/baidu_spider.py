# -*- coding: utf-8 -*-

# Define here the models for your scraped spider

import scrapy

class BaiduSpider(scrapy.spiders.Spider):
    name = "baidus"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://www.baidu.com"]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)