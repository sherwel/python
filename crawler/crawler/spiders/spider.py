# -*- coding: utf-8 -*-
from scrapy import log
from scrapy.spiders import Spider
from scrapy.mail import MailSender
from crawler.items import DefaultItem


class DefaultSpider(Spider):
    name = "default"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://www.baidu.com"]
    def parse(self, response):
    	items = []
    	for sel in response.xpath('//head/script'):
    		item = DefaultItem()
    		item['title'] = sel.extract()
    		items.append(item)
        return items
    #日志
    log.msg("This is a warning", level=log.WARNING)