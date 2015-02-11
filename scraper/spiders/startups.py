#!/usr/bin/env python
# scrapes http://bostonstartupsguide.com/ for info
#
# Copyright (c) 2015 @tylucaskelley

from scrapy.spider import Spider
from scrapy.selector import Selector
from scraper.items import Startup


class Scraper(Spider):
    name = "scraper"
    allowed_domains = ["bostonstartupsguide.com"]
    start_urls = ["http://bostonstartupsguide.com"] + ['http://bostonstartupsguide.com/page/{0}/'.format(i) for i in range(2, 56)]

    def parse(self, response):
        items = []

        for sel in response.css('#content-inside > div'):
            item = Startup()
            item['name'] = str(sel.css('div > div.startup1.normal > strong > a::text').extract()[0])
            item['link'] = str(sel.css('div > div.startup1.normal > strong > a::attr(href)').extract()[0])
            item['industry'] = str(sel.css('div > div.startup4 > span > a:nth-child(1)::text').extract()[0])
            items.append(item)

        return items
