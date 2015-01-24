from scrapy import Spider, Selector, Request
from ..items import Channel

class IPSpider(Spider):
    name, start_urls = 'ip_spider', ['http://iranproud.com/movies']


    def parse(self, response):
        hxs = Selector(response)

        for video in hxs.xpath("body//div[@id='divVideoHolder']/@videosrc").extract():
            item = Channel()
            item['video_url'] = video
            item['title'] = hxs.xpath("body//div[@id='divTitrGrid']/text()").extract()
            yield item


        for record in hxs.xpath("//body//a"):
            extracted = record.xpath('@href').extract()
            if len(extracted) == 0 or "/movies/" not in extracted[0]:
                continue

            item = Channel()
            page_url= "http://iranproud.com%s" % extracted[0] if extracted[0].startswith('/') else extracted[0]
            # item["img_url"] = record.xpath('img/@src').extract()[0]

            request = Request(page_url, callback=self.parse)
            request.meta['record'] = item
            yield request

