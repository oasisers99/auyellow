import scrapy

#scrapy crawl yellow -o tanning.json -t jsonlines
class YellowSpider(scrapy.Spider):
    name = "yellow"
    start_urls = [
        'https://www.yellowpages.com.au/search/listings?clue=massage&locationClue=australia',
    ]


    def parse(self, response):
        # Target the main list that does not have ads.
        for yellow in response.xpath("//div[@class='cell in-area-cell middle-cell']//a[@class='listing-name']"):
            yield {
                'text': yellow.css("::text").extract_first(),
                #'author': quote.css('small.author::text').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
            }

        # Target the 'next' page link.
        next_page = response.xpath("//a[@class='pagination navigation'][last()]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)