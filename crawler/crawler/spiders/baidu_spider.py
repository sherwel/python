# -*- coding: utf-8 -*-

# Define here the models for your scraped spider

import scrapy


class CrawlerSpider(scrapy.spiders.Spider):
    name = "baidu"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.baidu.com"]
    def parse(self, response):
        