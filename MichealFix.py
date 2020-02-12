# Detroit Free Press Parser

import requests
from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class FreepCrawler():
    # initialize variables and create list of base urls with the different search keywords
    def __init__(self, *keywords):
        self.urls = []
        self.baseURLs = []
        self.keywords = []
        self.scrapedArticles = []
        with open("searchUrls.txt", "r") as file:
            for line in file:
                for key in keywords:
                    self.keywords.append(key)
                    base = line.strip()
                    self.baseURLs.append(base + key + "/")

    # print all urls that have been crawled


    def printURLs(self):
        for url in self.urls:
            print(url)

        # for each base url, crawl all article links contained in each.  For instance, base url is the search result for polution,
        # so crawlURLs() will retrieve article urls from that page and append them to the urls list

    def crawlURLs(self):
        count = 0
        try:
            for url in self.baseURLs:
                chrome_options1 = Options()
                chrome_options1.add_argument("--headless")
                lessThanYear = True
                page = webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options1)
                page.get(url)
                # This will visit any web browser you want, go to the url, and scroll the predetermined amount of times and then grab the page source after scrolling which will have all of the article links
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
                front = ""
                with open("baseURLs.txt", "r") as file:
                    for line in file:
                        if line.strip() in url:
                            front = line.strip()
                for link in links:
                    if "/story/news/" in link['href']:
                        if "https" not in link['href']:
                            print(front + link['href'])
                            self.urls.append(front + link['href'])
                        else:
                            print(link['href'])
                            self.urls.append(link['href'])
                        count += 1
                print("-------------------------")
                print(count)


        except requests.exceptions.ConnectionError:
            print("[-] Connection refused: too man requests")

        # for each url in the urls list, scrape its content and store in scrapedArticles list as FreepScraper objects

    def scrapeURLs(self):
        for url in self.urls:
            print("scraping " + str(url))
            article = FreepScraper(url)
            self.scrapedArticles.append(article)
        print("\n\n")


    def getURLs(self):
        return self.urls

    def getSearchPageDates(self, source):

        dates = True
        page = soup(source, 'html.parser')
        articleDates = page.find_all(class_="date-created meta-info-text")
        for date in articleDates:
            if "2019" in date.get_text():
                dates = False
        return(dates)

    def getScrapedArticles(self):
        return self.scrapedArticles


    def getScrapedArticle(self, index):
        if index >= 0 and index < len(self.scrapedArticles):
            return self.scrapedArticles[index]
        else:
            print("[-] Index out of range. Acceptable range: 0-" + str(len(self.scrapedArticles) - 1))


class FreepScraper:

    # initialize variables
    def __init__(self, url):
        self.articleURL = url
        self.articleTitle = ""
        self.articleBody = []

        page = requests.get(self.articleURL)
        soup_page = soup(page.content, 'html.parser')
        try:
            self.articleTitle = soup_page.find_all(class_="util-bar-share-summary-title")[0].get_text()
        except IndexError:
            print("Content Locked")
            self.articleTitle = "Content Locked"
        try:
            body = soup_page.find_all(class_="p-text")
        except IndexError:
            print("Content Locked")
            self.articleBody = "Content Locked"

        for paragraph in body:
            self.articleBody.append(paragraph.get_text())


    # set the article title to articleTitle param
    def setArticleTitle(self, articleTitle):
        self.articleTitle = articleTitle

    # set the article url to url param
    def setURL(self, url):
        self.articleURL = url

    # set the article body to body param
    def setArticleBody(self, body):
        self.articleBody = body

    # return the article title
    def getArticleTitle(self):
        return self.articleTitle

    # return the article url
    def getArticleURL(self):
        return self.articleURL

    # return the article body
    def getArticleBody(self):
        return self.articleBody

    # print the article body
    def printArticleBody(self):
        for body in self.articleBody:
            print(body + "\n")


# # scrape and store article title and body. Save article body as array of paragraphs
# def scrape(self):
# 	page = requests.get(self.articleURL)
# 	soup_page = soup(page.content, 'html.parser')
# 	self.articleTitle = soup_page.find_all(class_="util-bar-share-summary-title")[0].get_text()
# 	body = soup_page.find_all(class_="p-text")
#
# 	for paragraph in body:
# 		self.articleBody.append(paragraph.get_text())


crawler = FreepCrawler("pollution", "contamination")
crawler.crawlURLs()
crawler.scrapeURLs()

print("Article Titles")
print("---------------------------------------------------")
for article in crawler.getScrapedArticles():
    print(article.getArticleTitle())
    