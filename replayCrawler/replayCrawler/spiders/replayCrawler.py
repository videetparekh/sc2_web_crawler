import scrapy
from selenium import webdriver
from time import sleep
import urllib2
import os

class replaySpider(scrapy.Spider):
    name = "replaySpider"
    driver = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver-v0.23.0-win64\geckodriver.exe")
    url_init = "https://gggreplays.com/matches#?page=1"

    @staticmethod
    def ggg_url_generator():
        url_init = "https://gggreplays.com/matches#?page=1"
        return url_init

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

    def download_game(self, page_url):
        download_driver = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver-v0.23.0-win64\geckodriver.exe")
        download_driver.get(page_url)
        download_element = download_driver.find_elements_by_xpath(".//a[contains(@href,'/matches/')]")
        download_url = download_element[0].get_attribute("href")
        replay_name = "ggtracker_"+(page_url.split("/")[-1])
        file_name = replay_name + ".SC2Replay"
        folder_path = "d:/Users/Administrator/Desktop/StarCraft II Research/Replays/" + replay_name
        file_path = folder_path + "/" + file_name

        get_file = urllib2.urlopen(download_url)
        file_data = get_file.read()

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(file_path, 'wb') as f:
            f.write(file_data)
        download_driver.close()

    def close_driver(self):
        self.driver.close()