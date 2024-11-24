import re
import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.xpath(
            '//a[starts-with(@href, "pep-")]/@href'
        ).getall()
        unique_links = list(set(links))
        for link in unique_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': re.search(r'\d+', response.xpath(
                '//*[@id="pep-page-section"]/header/ul/li[3]'
            ).get())[0],
            'name': response.xpath(
                '//*[@id="pep-content"]'
            ).css('h1::text').get(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
