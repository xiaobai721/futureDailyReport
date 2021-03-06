# -*- coding: utf-8 -*-
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from futureDailyReport.items import czceItem

class czecSpider(BaseSpider):
    name = "czec"
    allowed_domains = ["www.czce.com.cn"]
    start_urls = [
        "http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20170612/FutureDataWhsheet.htm"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.select('//table[@width = 800 and @align = "center"]')
        items = []
        for site in sites:
            item = czceItem()
            symbols = site.select('//tr[1]//b/text()').extract()

            item['Symbol'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').extract()
            items.append(item)
        return items
