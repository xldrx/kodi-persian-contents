from scrapy import Spider, Selector, Request
from ..items import Channel

class IPSpider(Spider):
    name, start_urls = 'ip_spider', ['http://iranproud.com/movies']


    def parse_channel(self, response):
        hxs = Selector(response)
        item = response.meta['record']
        item['video_url'] = hxs.xpath("body//div[@id='divVideoHolder']/@videosrc").extract()[0]
        # item["title"] = hxs.xpath("body//div[@id='divTitrGrid']/text()").extract()[0]

        return item

    def parse(self, response):
        hxs = Selector(response)

        for record in hxs.xpath("//body//a"):
            item = Channel()
            page_url= "http://iranproud.com%s" % record.xpath('@href').extract()[0]
            # item["img_url"] = record.xpath('img/@src').extract()[0]

            request = Request(page_url, callback=self.parse_channel)
            request.meta['record'] = item
            yield request
