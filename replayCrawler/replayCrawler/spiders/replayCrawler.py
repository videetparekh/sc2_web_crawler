
from selenium import webdriver
from time import sleep


class replaySpider:
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    driver = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver-v0.23.0-win64\geckodriver.exe", firefox_profile=firefox_profile)     # Replace the path with the local geckodriver path on your system
    download_driver = None

    def init_download_driver(self):
        self.download_driver = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver-v0.23.0-win64\geckodriver.exe", firefox_profile=self.firefox_profile)      # Replace the path with the local geckdriver path on your system

    def parse(self, response):
        self.driver.get(response)
        matches = self.driver.find_elements_by_xpath(".//a[contains(@href,'/matches/')]")
        match_hrefs = [match.get_attribute("href") for match in matches]
        match_hrefs = list(set(match_hrefs))
        return match_hrefs

    def next_page(self):
        try:
            next_page_element = self.driver.find_element_by_link_text("Next")
            next_page_element.click()
            sleep(5)
            new_page_url = self.driver.current_url
            return new_page_url
        except:
            return None

    def match_download_scraper(self, page_url):
        self.download_driver.get(page_url)
        try:
            download_element = self.download_driver.find_element_by_xpath(".//a[contains(@href,'/matches/')]")
            download_url = download_element.get_attribute("href")
        except:
            download_url = ''
        return download_url

    def close_driver(self):
        self.driver.close()

    def close_download_driver(self):
        self.download_driver.close()
