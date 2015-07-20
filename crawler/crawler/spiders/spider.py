# -*- coding: utf-8 -*-

# Define here the models for your scraped spider

import scrapy


class CrawlerSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://www.baidu.com"]
    filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)