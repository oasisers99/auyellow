**yellowscrapper**
**Web Crawler**

Designed to crawl a yellowpage website and get the title.

What to be implemented:
Move to the next page to fetch all selected texts.
Calculate word frequency and rank words.
Link it to a web-based applicataion where a user can select variables like:
  - Number of words to fetch
  - Etc.
To add a new website, I will need to develop another script.
  - Or I can take variables from the web.
    - Catching next page css is not so easy, but doable.
  
**To execute**:
1. Go to /auyellow/yellowscrapper/spiders
2. Run: scrapy crawl yellow -o medical.json -t jsonlines 
   (Change the name of medical.json to your category. eg, personalcare.json)
3. Just wait until it ends.

**To get most frequent words**:
1. Go to /auyellow/yellowscrapper/process
2. Run: python jsonparser.py
   - You can also run it on your IDE.
   - Please add or remove stop words in jsonparser.py as you like. :)

**Reference**:
xpath tester:
http://videlibri.sourceforge.net/cgi-bin/xidelcgi

Maybe I can consider to use some API of NZ Government.
Or GoogleMap API: https://developers.google.com/maps/documentation/javascript/places#place_searches


