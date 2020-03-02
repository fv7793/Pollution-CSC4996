from websites import *
import database
import sys

class Peat:
    def __init__(self, keywords):
        self.keywords = keywords
        self.websites = []

        # self.websites.append(Ourmidland(keywords))
        # self.websites.append(MarionPress(keywords))
        self.websites.append(TheCountyPress(keywords))
        # self.websites.append(LakeCountyStar(keywords))
        # self.websites.append(NorthernExpress(keywords))
        # self.websites.append(ManisteeNews(keywords))
        # self.websites.append(MichiganChronicle(keywords))
        # self.websites.append(HarborLightNews(keywords))
        # self.websites.append(TheDailyNews(keywords))
        # self.websites.append(LeelanauNews(keywords))
        # self.websites.append(HoughtonLakeResorter(keywords))
        # self.websites.append(IronMountainDailyNews(keywords))
        # self.websites.append(MiningJournal(keywords))
        # self.websites.append(TheAlpenaNews(keywords))

        # TODO: not working
        # self.websites.append(LakeOrionReview(keywords))
        # self.websites.append(ClarkstonNews(keywords))

    def getUrls(self):
        urls = []
        for site in self.websites:
            for url in site.getArticleLinks():
                urls.append(url)
        return urls

    def getScrapedArticles(self):
        articles = []
        for site in self.websites:
            for article in site.getScrapedArticles():
                articles.append(article)
        return articles

    def storeInArticlesCollection(self, article):
        try:
            database.Articles(
                url=['url'],
                title=['title'],
                publishingDate=article['publishingDate']
            ).save()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            pass











