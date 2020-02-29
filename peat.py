import requests
from bs4 import BeautifulSoup as soup
from dateutil import parser
import newspaper

class Crawler:
    def __init__(self):
        self.baseUrl = ""
        self.keywords = []
        self.articleLinks = []
        self.articleCount = 0

    def crawl(self):
        links = []
        for keyword in self.keywords:
            query = self.searchQuery.replace("PEATKEY", keyword).replace("PEATPAGE","1")
            page = requests.get(query)

            soupLinks = self.scrapeArticleLinks(page)

            for link in soupLinks:
                if link['href'] not in links:
                    links.append(link['href'])

        self.articleLinks = self.filterLinksForArticles(links)

    def filterLinksForArticles(self, links):
        return links

    def setBaseUrl(self, url):
        self.baseUrl = url

    def setKeywords(self, keywords):
        self.keywords = keywords

    def getKeywords(self):
        return self.keywords

    def setSearchQueryStructure(self, query):
        self.searchQuery = query

    def scrapeArticleLinks(self, page):
        # TODO: implement
        soupPage = soup(page.content, "html.parser")
        return soupPage.find_all('a', href=True)

    def getArticleLinks(self):
        return self.articleLinks

    def getArticleCount(self):
        return self.articleCount

    def storeInUrlsCollection(self):
        # TODO: implement
        pass


class Scraper(Crawler):
    def __init__(self):
        super().__init__()
        self.titles = []
        self.scrapedArticles = []

    def scrapeAll(self):
        for article in self.articleLinks:
            print("scraping: ",article)
            self.scrape(article)

    def scrape(self, url):
        article = newspaper.Article(url)
        article.download()
        article.parse()

        if self.scrapeTitle(article) not in self.titles:

            article = {
                "url": url,
                "title": self.scrapeTitle(article),
                "publishDate": self.scrapePublishingDate(article),
                "body": self.scrapeBody(article)}

            self.scrapedArticles.append(article)
            self.titles.append(article["title"])

    def scrapeTitle(self, newspaperArticleObj=None):
        return newspaperArticleObj.title

    def scrapePublishingDate(self, newspaperArticleObj=None):
        date = newspaperArticleObj.publish_date
        return self.normalizeDate(date)

    def scrapeBody(self, newspaperArticleObj=None):
        return newspaperArticleObj.text

    def normalizeDate(self, date):
        print(date)
        if date is None:
            return date
        d = parser.parse(date)
        return d.strftime("%m/%d/%Y")

    def getScrapedArticles(self):
        return self.scrapedArticles

    def storeInArticlesCollection(self):
        # TODO: implement
        pass






