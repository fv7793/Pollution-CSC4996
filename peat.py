import requests
from bs4 import BeautifulSoup as soup
from dateutil import parser

class Crawler:
    def __init__(self):
        self.baseUrl = ""
        self.keywords = []
        self.searchQuery = ""
        self.articleLinks = []
        self.articleCount = 0
        print("Crawler constructor")

    def setBaseUrl(self, url):
        self.baseUrl = url

    def setKeywords(self, keywords):
        self.keywords = keywords

    def getKeywords(self):
        return self.keywords

    def requestPage(self):
        page = requests.get(self.searchQuery)
        return soup(page.content, 'html.parser')

    def getNextPage(self):
        print("getting next page")

    def scrapeArticleLinks(self):
        print("scraping article links")

    def getArticleLinks(self):
        return self.articleLinks

    def getArticleCount(self):
        return self.articleCount

    def storeInUrlsCollection(self):
        print("storing article urls")


class Scraper(Crawler):
    def __init__(self):
        super().__init__()
        self.articleTitle = ""
        self.articleBody = []
        self.articleDate = ""
        print("Scraper constructor")

    def scrape(self):
        self.scrapeTitle()
        self.scrapePublishingDate()
        self.scrapeBody()

    def scrapeTitle(self):
        print("scraping title")

    def scrapePublishingDate(self):
        print("scraping publishing date")

    def scrapeBody(self):
        print("scraping body")

    def normalizeDate(self, date):
        d = parser.parse(date)
        return d.strftime("%m/%d/%Y")

    def getArticleTitle(self):
        return self.articleTitle

    def getArticleDate(self):
        return self.articleDate

    def getArticleBody(self):
        return self.articleBody

    def storeInArticlesCollection(self):
        print("storing scraped attributes")


class Ourmidland(Scraper):
    def __init__(self, keywords):
        super().__init__()
        self.setKeywords(keywords)
        self.setBaseUrl("https://www.ourmidland.com/")


ourmidland = Ourmidland(["key1", "key2"])


