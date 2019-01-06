import replayCrawler
import csv
import time


def push_download_links_to_file(links):
    file_path = "%%%%%PATH%%%%%"    # Replace with the path to the CSV file where the replay links will be stored
    file = open(file_path, 'a+')
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for link in links:
        file_writer.writerow([link])
    file.close()


page_iterator = 0

crawler = replayCrawler.replaySpider()
#url_init = "https://gggreplays.com/matches#?page=601"
url_init = raw_input("Url: ")
page_iteration_limit = int(raw_input("Page Iteration Limit: "))


t_init = time.time()
while page_iterator < page_iteration_limit and url_init is not None:
    download_urls = []
    t_iter_init = time.time()

    print "Parsing page", page_iterator+1

    new_match_links = crawler.parse(url_init)

    print "Match URLs generated."

    crawler.init_download_driver()

    for match in new_match_links:
        download_urls.append(crawler.match_download_scraper(match))
    push_download_links_to_file(download_urls)
    print 'Replay Download URLs generated.'

    crawler.close_download_driver()

    url_init = crawler.next_page()
    page_iterator += 1

    t_iter = time.time()
    print "Iteration time for 10 matches: ", t_iter-t_iter_init, "s. Single match iteration time: ", (t_iter-t_iter_init)/10, "s"

crawler.close_driver()
t_fin = time.time()
print "Process complete. Total Execution time: ", t_fin-t_init, "s"
