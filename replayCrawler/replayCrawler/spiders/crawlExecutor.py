import replayCrawler

match_links = []
page_iteration_limit = 1
page_iterator = 0
download_limit = 5
pool_size = 5

crawler = replayCrawler.replaySpider()
url_iter = crawler.ggg_url_generator()
while page_iterator < page_iteration_limit and url_iter is not None:
    match_links += crawler.parse(url_iter)
    url_iter = crawler.next_page()
    page_iterator += 1
crawler.close_driver()

for match in match_links[:download_limit]:
    crawler.download_game(match)
