import requests
from bs4 import BeautifulSoup as soup
from dateutil import parser

class Crawler:
    def __init__(self):
        print("Crawler object created")
        self.baseUrl = ""
        self.keywords = []
        self.searchQueryStructure = ""
        self.articleLinks = []
        self.articleCount = 0

    def crawl(self):
        # TODO: implement
        print("crawling")
        soupPage = self.getSoupPage("pollution")

    def setBaseUrl(self, url):
        self.baseUrl = url

    def setKeywords(self, keywords):
        self.keywords = keywords

    def getKeywords(self):
        return self.keywords

    def setSearchQueryStructure(self, query):
        # TODO: implement
        self.searchQuery = query

    def getSoupPage(self,keyword):
        query = self.searchQuery.replace("PEATKEY", keyword)
        page = requests.get(query)
        return soup(page.content, 'html.parser')

    def getNextPage(self):
        # TODO: implement
        print("getting next page")

    def scrapeArticleLinks(self):
        # TODO: implement
        print("scraping article links")

    def getArticleLinks(self):
        return self.articleLinks

    def getArticleCount(self):
        return self.articleCount

    def storeInUrlsCollection(self):
        # TODO: implement
        print("storing article urls")


class Scraper(Crawler):
    def __init__(self):
        super().__init__()
        print("Scraper object created")
        self.articleTitle = ""
        self.articleBody = []
        self.articleDate = ""

    def scrape(self):
        self.scrapeTitle()
        self.scrapePublishingDate()
        self.scrapeBody()

    def scrapeTitle(self):
        # TODO: implement
        print("scraping title")

    def scrapePublishingDate(self):
        # TODO: implement
        print("scraping publishing date")

    def scrapeBody(self):
        # TODO: implement
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
        # TODO: implement
        print("storing scraped attributes")


class Ourmidland(Scraper):
    def __init__(self, keywords):
        super().__init__()
        self.setKeywords(keywords)
        self.setBaseUrl("https://www.ourmidland.com/")
        self.setSearchQueryStructure("https://www.ourmidland.com/search/?action=search&firstRequest=1&searchindex=solr&query=PEATKEY")
        self.crawl()
        self.scrape()

ourmidland = Ourmidland(["key1", "key2"])


