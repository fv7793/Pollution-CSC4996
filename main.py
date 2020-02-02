
from freepCrawler import FreepCrawler
from freepScraper import FreepScraper
import mongoengine

crawler = FreepCrawler("pollution", "contamination", "pollute", "contaminate", "spill", "leak", "dump", "chemical", "toxic")
crawler.crawlURLs()

scrapedArticles = []
crawlCount = 0

db = mongoengine.connect(db="Pollution")
db.drop_database('Pollution')

for url in crawler.getURLs():
    print("scraping " + str(url))
    article = FreepScraper(url)
    article.storeInDatabase()
    scrapedArticles.append(article)
    crawlCount = crawlCount + 1

print("\n[+] Crawled " + str(crawlCount) + " articles\n")
print("Article Titles")
print("---------------------------------------------------")

for article in scrapedArticles:
    print(article.getArticleTitle())

