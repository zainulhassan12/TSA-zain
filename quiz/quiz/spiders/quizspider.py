import scrapy

from ..items import QuizItem


class qspider(scrapy.Spider):
    name = "quizspider"
    start_urls = [
        'https://www.sanfoundry.com/computer-fundamentals-questions-answers-network-security/'
    ]

    #
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        div = response.css('div.entry-content')
        for line in div:
            item = QuizItem()
            item["question"] = line.css("div.p.selectorgadget_selected::text").extract()
            item["answer"] = line.css("div.p.selectorgadget_selected::text").extract()
            # item["fun_fact"] = line.css("div.p-small p::text").extract().pop()
            yield item
        # for item in div:
        #     item["question"] = response.css('p::text').extract()
        #     item["answer"] = response.xpath('//')


