`# yellowscrapper
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
  
**Execute**:

`scrapy crawl yellow -o yello.json`

**Reference**:
xpath tester:
http://videlibri.sourceforge.net/cgi-bin/xidelcgi
