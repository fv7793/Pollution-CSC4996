import requests
from bs4 import BeautifulSoup as soup
from dateutil import parser
import newspaper
import database
import sys

class Crawler:
    def __init__(self):
        self.baseUrl = ""
        self.keywords = []
        self.articleLinks = []
        self.articleCount = 0

    def crawl(self):
        print("Crawling: " + self.baseUrl)
        links = []
        for keyword in self.keywords:
            query = self.searchQuery.replace("PEATKEY", keyword).replace("PEATPAGE","1")

            page = requests.get(query)

            soupLinks = self.scrapeArticleLinks(page)

            for link in soupLinks:
                if link['href'] not in links:
                    links.append(link['href'])

        self.articleLinks = self.filterLinksForArticles(links)
        self.storeInUrlsCollection()

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
        # TODO: try overriding this in the website classes and use tree structure of search pages
        #  to get article urls
        soupPage = soup(page.content, "html.parser")
        return soupPage.find_all('a', href=True)

    def getArticleLinks(self):
        return self.articleLinks

    def getArticleCount(self):
        return self.articleCount

    def getArticleCount(self):
        return self.baseUrl

    def storeInUrlsCollection(self):
        for url in self.getArticleLinks():
            try:
                database.Urls(url=url).save()
            except:
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
            self.storeInArticlesCollection(article["url"], article["publishDate"], article["title"])

    def scrapeTitle(self, newspaperArticleObj=None):
        title = newspaperArticleObj.title
        if title is None:
            return ""
        else:
            return title

    def scrapePublishingDate(self, newspaperArticleObj=None):
        # TODO: improve
        # date = newspaperArticleObj.publish_date
        # if date is None:
        #     return ""
        # else:
        #     return self.normalizeDate(date)
        return ""

    def scrapeBody(self, newspaperArticleObj=None):
        body = newspaperArticleObj.text
        if body is None:
            return ""
        else:
            return body

    def normalizeDate(self, date):
        d = parser.parse(date)
        return d.strftime("%m/%d/%Y")

    def getScrapedArticles(self):
        return self.scrapedArticles

    def storeInArticlesCollection(self,url,date,title):
        # TODO: implement
        try:
            database.Articles(
                publishingDate=date,
                title=title,
                url=url
            ).save()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            pass






