from peat import Crawler, Scraper

class Ourmidland(Scraper):
    def __init__(self, keywords):
        super().__init__()
        self.setKeywords(keywords)
        self.setBaseUrl("https://www.ourmidland.com/")
        self.setSearchQueryStructure("https://www.ourmidland.com/search/?action=search&searchindex=solr&query=PEATKEY&page=PEATPAGE")
        self.crawl()
        self.scrapeAll()

    def filterLinksForArticles(self, links):
        filteredLinks = []
        for link in links:
            if "/article/" in link:
                link = "https://www.ourmidland.com" + link
                filteredLinks.append(link)
        return filteredLinks

    def scrapePublishingDate(self, newspaperArticleObj=None):
        return None


# http://www.marion-press.com/

class MarionPress(Scraper):
    def __init__(self, keywords):
        super().__init__()
        self.setKeywords(keywords)
        self.setBaseUrl("http://www.marion-press.com/")
        self.setSearchQueryStructure("http://www.marion-press.com/page/PEATPAGE/?s=PEATKEY&x=0&y=0")
        self.crawl()
        self.scrapeAll()

    def filterLinksForArticles(self, links):
        filteredLinks = []
        for link in links:
            linkSplit = link.split("/")
            if len(linkSplit) > 6:
                if linkSplit[3].isnumeric() and linkSplit[4].isnumeric():
                    filteredLinks.append(link)
        return filteredLinks

    def scrapePublishingDate(self, newspaperArticleObj=None):
        return None




