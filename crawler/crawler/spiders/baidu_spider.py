# -*- coding: utf-8 -*-

# Define here the models for your scraped spider

import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://www.baidu.com"]
    def parse(self, response):
        pass