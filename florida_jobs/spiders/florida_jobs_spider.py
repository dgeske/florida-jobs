#!/usr/bin/env python
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

from florida_jobs.items import FloridaJobsItem

def _select_data(r, xpath):
    '''Return the first element if it exists, else return None'''
    data = r.select(xpath).extract()
    return data[0] if data else None

class florida_jobs_spider(BaseSpider):
    name = "florida_jobs"
    allowed_domains = ["b3.caspio.com"]
    start_urls=["http://b3.caspio.com/dp.asp?appSession=268284288226221&RecordID=&PageID=2&PrevPageID=1&cpipage=1&CPISortType=&CPIorderBy="]

    def parse(self, response):
        
        self.log('A response from %s just arrived!' % response.url)
        
        sel = Selector(response)
        items = []
        rows = sel.xpath("//tr[@class='cbResultSetEvenRow' or @class='cbResultSetOddRow']")
        for r in rows:
            item = FloridaJobsItem()
            item['name'] = _select_data(r, "td[1]/a/text()")
            item['employer'] = _select_data(r, "td[2]/text()")
            item['location'] = _select_data(r, "td[3]/text()")
            item['position'] = _select_data(r, "td[4]/text()")
            item['department'] = _select_data(r, "td[5]/text()")
            item['hire_date'] = _select_data(r, "td[6]/text()")
            item['salary'] = _select_data(r, "td[7]/text()")
            yield item

        next = sel.xpath("//a[@class='cbResultSetNavigationLinks' and img[@alt='Next']]/@href").extract()
        next10 = sel.xpath("//a[@class='cbResultSetNavigationLinks' and img[@alt='Next10']]/@href").extract()
        if next:
            url = "http://b3.caspio.com/" + next[0];
            print "next url: " + url
            yield Request(url, callback=self.parse)
        elif next10:
            url = "http://b3.caspio.com/" + next10[0];
            print "next url: " + url
            yield Request(url, callback=self.parse)
