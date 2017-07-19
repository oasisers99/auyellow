import scrapy
import csv

#######################  Category & Region ##############################
# location also can be city or suburb
category = "childcare"
location = "australia"
##########################################################################

class YellowSpider(scrapy.Spider):

    #scraper info
    global category
    global location

    name = "yellow"
    start_urls = [
        'https://www.yellowpages.com.au/search/listings?clue='+category+'&locationClue='+location,
    ]

    # start parsing!
    def parse(self, response):

        global category

        # Target the main list that does not have ads. Parse details of each business
        for yellow in response.xpath("//div[@class='cell in-area-cell middle-cell']"):
            
            name = yellow.xpath(".//a[@class='listing-name']/text()").extract_first()
            address = yellow.xpath(".//p[@class='listing-address mappable-address' or @class='listing-address mappable-address mappable-address-with-poi']/text()").extract_first()
            address = str(address).replace(',' , '')
            suburb_state = yellow.xpath(".//p[@class='listing-address mappable-address' or @class='listing-address mappable-address mappable-address-with-poi']/@data-address-suburb").extract_first()
            latitude = yellow.xpath(".//p[@class='listing-address mappable-address' or @class='listing-address mappable-address mappable-address-with-poi']/@data-geo-latitude").extract_first()
            longitude = yellow.xpath(".//p[@class='listing-address mappable-address' or @class='listing-address mappable-address mappable-address-with-poi']/@data-geo-longitude").extract_first()
            website = yellow.xpath(".//a[@class='contact contact-main contact-url ']/@href").extract_first()
            phone = yellow.xpath(".//span[@class='contact-text']/text()").extract_first()

            slist = str(suburb_state).split(' ')
            size = len(slist)
            state = slist[size-1]
            
            if(size > 2):
                del slist[size-1]
                suburb = ' '.join(slist)
            elif(size <= 2):
                suburb = slist[0]

            slist = str(address).split(' ')
            postcode = slist[len(slist) - 1]

            yield {
                'category': category,
                'name': name,
                'address': address,
                'suburb': suburb,
                'state': state,
                'postcode': postcode,
                'lat': latitude,
                'long': longitude,
                'website': website,
                'phone': phone
            }

        # Target the 'next' page link.
        next_page = response.xpath("//a[@class='pagination navigation'][last()]/@href").extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        