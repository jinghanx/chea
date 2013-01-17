from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import TutorialItem, ZipcodeItem

class HuashangSpider(CrawlSpider):
    name = 'Huashang'
    allowed_domains = ['esearch411.com']
    start_urls = [
            #'http://www.esearch411.com/default.asp'
            #'http://www.esearch411.com/yp/clist.asp?cid=1'
            #'http://www.esearch411.com/yp/custlist.asp?cid=1&catid=578'
            'http://www.esearch411.com/yp/custlist.asp?cid=1&catid=593'
            ]
    rules = (Rule(SgmlLinkExtractor(allow=(r"http://www.esearch411.com/yp/custlist*", )), callback='parse_override'),
            Rule(SgmlLinkExtractor(allow=(r"http://www.esearch411.com/yp/clist*", )))
            )
    #rules = (Rule(SgmlLinkExtractor(allow=(r"http://www.esearch411.com/html/*/*", )), callback='parse_zipcode'),
    #        Rule(SgmlLinkExtractor(allow=(r"http://www.esearch411.com/yp/.*cid.*", ), deny=(r"http://www.esearch411.com/yp/.*%.*", ))))
    def helper(self, l):
        if not l:
            return ''
        else:
            return l[0]

    def parse_override(self, response):
        hxs = HtmlXPathSelector(response)
        category = hxs.select("//td[@class='TDBorder' and @height='12']")
        category = category[0]
        category_1 = self.helper(category.select('font/a[2]/text()').extract()).replace(',', '')
        category_2 = category.select('font/text()').extract()
        if len(category_2) < 2:
            return
        category_2 = category_2[1].strip('> ').replace(',','')
        stores = hxs.select("//tr[@bgcolor='#CCCCCC' or @bgcolor='#fdeffe']")
        items = []
        for store in stores[:-1]:
            item = TutorialItem()
            item['category_1'] = category_1
            item['category_2'] = category_2
            item['name_english'] = self.helper(store.select('td[1]/span/a/font/text()').extract()).replace(',','')
            item['name_chinese'] = self.helper(store.select('td[2]/span/a/font/text()').extract()).replace(',','')
            item['city'] = self.helper(store.select('td[4]/font/text()').extract()).replace(',', '')
            item['address'] = self.helper(store.select('td[3]/font/text()').extract()).replace(',', '')
            item['number'] = self.helper(store.select('td[5]/font/text()').extract()).replace(',', '')
            items.append(item)
        return items

    def parse_zipcode(self, response):
        hxs = HtmlXPathSelector(response)
        items = hxs.select("//table[@border='0' and @cellspacing='0' and @align='center']/tbody")
        items = items[0]
        items = items.select('tr')
        print len(items)
        res = []
        for item in items:
            item = ZipcodeItem()
            item['number'] = items.select('td[3]/font/span/text()').extract()
            item['zipcode'] = items.select('td[2]/font/span/text()').extract()
            res.append(item)
        return res

