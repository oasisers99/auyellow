import scrapy

#scrapy crawl yellow -o medical.json -t jsonlines
class YellowSpider(scrapy.Spider):
    name = "yellow"
    start_urls = [
        'https://www.yellowpages.com.au/search/listings?clue=medical&locationClue=australia',
    ]


    def parse(self, response):
        # Target the main list that does not have ads.
        idx = 1
        for yellow in response.xpath("//div[@class='cell in-area-cell middle-cell']"):
            # print(yellow)
            yield {
                'category': 'medical',
                'business_name': yellow.xpath("//a[@class='listing-name']/text()").extract()[idx],
                # 'business_name': yellow.xpath("//a[@class='listing-name']/text()").extract_first()
                'business_addr': yellow.xpath("//p[@class='listing-address mappable-address mappable-address-with-poi']/text()").extract()[idx],
                #'author': quote.css('small.author::text').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
            }
            idx = idx + 1
        # Target the 'next' page link.
        next_page = response.xpath("//a[@class='pagination navigation'][last()]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


# //*[@id="search-results-page"]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div[2]/a
# //*[@id="search-results-page"]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div/div[18]/div/div/div[1]/div/div/div[2]/a
# //*[@id="search-results-page"]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div/div[19]/div/div/div[1]/div/div/div[2]/a
# //*[@id="search-results-page"]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div/div[24]/div/div/div[1]/div/div/div[2]/a
   # yield{
   #              "business_name": response.xpath('//*[@id="search-results-page"]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div/div['+str(idx)+']/div/div/div[1]/div/div/div[2]/a').select("string()").extract_first()
   #          #.css("::attr(data-address-line)").extract()[idx],