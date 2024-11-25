import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (PEP_ALLOWED_DOMAINS, PEP_SPIDER_NAME,
                                PEP_START_URLS)


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = PEP_ALLOWED_DOMAINS
    start_urls = PEP_START_URLS

    def parse(self, response):
        links = response.xpath(
            '//a[starts-with(@href, "pep-")]/@href'
        ).getall()
        unique_links = list(set(links))
        for link in unique_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.xpath(
                'translate(//*[@id="pep-page-section"]'
                '/header/ul/li[3]/text(), "PEP ", "")'
            ).get(),
            'name': response.xpath(
                '//*[@id="pep-content"]/h1/text()'
            ).get(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
