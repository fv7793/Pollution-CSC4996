# Detroit Free Press Parser

import requests
from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from freepScraper import FreepScraper


class FreepCrawler():
    # initialize variables and create list of base urls with the different search keywords
    def __init__(self, *keywords):
        self.urls = []
        self.baseURLs = []
        self.keywords = []
        self.scrapedArticles = []

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
        lessThanYear = True
        try:
            for url in self.baseURLs:
                page = webdriver.Chrome(ChromeDriverManager().install())
                page.get(url)
        # This will visit any web browser you want, go to the url, and scroll the predetermined amount of times and then grab the page source after scrolling which will have all of the article links

                while lessThanYear:
                    page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(4)
                    source = page.page_source
                    #Will call the gunction that holds dates and catch a date that is from 2018 and end the loop, therefore only grabbing articles after 12/31/2019
                    dates = self.getSearchPageDates(source)
                    for date in dates:
                        if "2018" in date:
                            lessThanYear = False

                soup_page = soup(source, 'html.parser')
                links = soup_page.find_all('a', href=True)

            for link in links:
                if "/story/news/local/michigan/" in link['href']:
                    self.urls.append("https://www.freep.com" + link['href'])

        except requests.exceptions.ConnectionError:
            print("[-] Connection refused: too man requests")

        # for each url in the urls list, scrape its content and store in scrapedArticles list as FreepScraper objects

    def scrapeURLs(self):
        for url in self.urls:
            print("scraping " + str(url))
            article = FreepScraper(url)
            self.scrapedArticles.append(article)
        print("\n\n")

    def getSearchPageDates(self, source):
        page = soup(source, 'html.parser')
        articleDates = page.find_all(class_= 'date_created meta-info-text')
        dates = []
        for date in articleDates:
            dates.append(date.get_text())
        return(dates)

    def getURLs(self):
        return self.urls


    def getScrapedArticles(self):
        return self.scrapedArticles


    def getScrapedArticle(self, index):
        if index >= 0 and index < len(self.scrapedArticles):
            return self.scrapedArticles[index]
        else:
            print("[-] Index out of range. Acceptable range: 0-" + str(len(self.scrapedArticles) - 1))

