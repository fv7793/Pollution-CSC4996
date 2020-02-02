import requests
from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver
import os
from sys import platform
from selenium.webdriver.chrome.options import Options


class FreepCrawler():
    # initialize variables and create list of base urls with the different search keywords
    def __init__(self, *keywords):
        self.urls = []
        self.baseURLs = []
        self.keywords = []

        for key in keywords:
            self.keywords.append(key)
            self.baseURLs.append("https://www.freep.com/search/" + key + "/")


    # print all urls that have been crawled
    def printURLs(self):
        for url in self.urls:
            print(url)

    # for each base url, crawl all article links contained in each.  For instance, base url is the search result for polution,
    # so crawlURLs() will retrieve article urls from that page and append them to the urls list
    def crawlURLs(self):
        try:
            for url in self.baseURLs:
                lessThanYear = True
                if platform == "darwin":
                    chromeDriverPath = os.path.abspath(os.getcwd()) + "/chromedriver_mac"
                else:
                    chromeDriverPath = os.path.abspath(os.getcwd()) + "/chromedriver_win32.exe"

                options = Options()
                options.add_argument('--headless')
                driver = webdriver.Chrome(chromeDriverPath, options=options)
                driver.get(url)

                while lessThanYear:
                    i = 0
                    while i < 4:
                        page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        source = page.page_source
                        # Will call the function that holds dates and catch a date that is from 2018 and end the loop, therefore only grabbing articles after 12/31/2018
                        lessThanYear = self.getSearchPageDates(source)
                        i += 1

                soup_page = soup(source, 'html.parser')
                links = soup_page.find_all('a', href=True)

            for link in links:
                if "/story/news/local/michigan/" in link['href']:
                    self.urls.append("https://www.freep.com" + link['href'])

        except requests.exceptions.ConnectionError:
            print("[-] Connection refused: too man requests")

    def getSearchPageDates(self, source):

        dates = True
        page = soup(source, 'html.parser')
        articleDates = page.find_all(class_="date-created meta-info-text")
        for date in articleDates:
            print(date.get_text())
            print("-------")
            if "2018" in date.get_text():
                dates = False
        return(dates)

    def getURLs(self):
        return self.urls


    def getURLs(self):
        return self.urls
