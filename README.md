**Australian Yellow Page Scrapper**
**Web Crawler**

Designed to crawl a yellowpage website to get the details of each businss
  
**To execute**:

csv format

1. Go to /auyellow/yellowscrapper/spiders
2. Open yellowscrapper.py
3. Change the category and location as you want
4. Execute: scrapy crawl yellow -t csv -o result.csv 
   Scrapy under Windows system add an empty line between each result. To remove them, go to /auyellow/yellowscrapper/process 
   and run: python emptyLineRemover.py

   Then, in the /auyellow/yellowscrapper/spiders directory, there will be result_noblank.csv

** Please remove the result.csv and result_noblank.csv file before starting a new search **


**Reference**:
xpath tester:
http://videlibri.sourceforge.net/cgi-bin/xidelcgi

#scrapy crawl yellow -o result.json -t jsonlines
#scrapy crawl yellow -t csv -o result.csv 

**Don't use it**
**To get most frequent words**:
1. Go to /auyellow/yellowscrapper/process
2. Run: python jsonparser.py
   - You can also run it on your IDE.
   - Please add or remove stop words in jsonparser.py as you like.