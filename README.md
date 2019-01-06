# StarCraft II Replay Crawler

### Dependencies

- selenium
- urllib2
- geckodriver (Mozilla Firefox simulator)

### Replay Crawler

ReplayCrawler.py contains the crawl and scrape logic for gggreplays.com. It uses the library *selenium* to simulate a page on a Mozilla Firefox web browser. Each page is generated on one browser and a second browser is opened to access every replay link on that page. Once the replay links on those pages are generated, it stores those links in a csv file. 



### Crawl Executor

CrawlExecutor.py drives the replay crawler and contains the main function which is seeded by a page number accessed from the user. A page iteration limit is also requested from the user. This defines how many pages will be iterated over in a single execution. 



### Replay Download Script

This works as an independent script. It requires a path to the csv file where the replay links are stored. It requires a start bound and an iteration limit (the number downloads to perform).



### Paths

All paths have been defaulted and replaced with comments