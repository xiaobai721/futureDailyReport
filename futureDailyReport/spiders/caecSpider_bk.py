import scrapy
from scrapy.selector import Selector
from futureDailyReport.items import czceItem

class czecSpider(scrapy.Spider):
    name = "czec"
    allowed_domains = ["www.czce.com.cn"]

    def start_requests(self):
        start_urls = [
            'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20170612/FutureDataWhsheet.htm'
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

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