from scraperInterface import ScraperInterface
from parse import isArticleEvent
from RNNBinary import readBinary
from officialComm import officialComment
from dateRegex import dateInfo
from textColors import bcolors
from Location import locationsInfo
import testCollectionIncidents
import database
import sys


keywords = ["spill"]
scraper = ScraperInterface(keywords)

print("\n" + bcolors.OKGREEN + "[+] " + str(scraper.getArticleCount()) + " articles retrieved" + bcolors.ENDC)

articleTitles = []

for article in scraper.getScrapedArticles():
    articleTitles.append(article['title'])


####################  NLP event recognition  ###########################
confirmedEventArticles = []
confirmedEventCount = 0
print("\nParsing event articles")
print("-----------------------")
for article in scraper.getScrapedArticles():
    if isArticleEvent(article):
        scraper.storeInArticlesCollection(article)
        confirmedEventArticles.append(article)
        confirmedEventCount = confirmedEventCount + 1
        print(bcolors.OKGREEN + "[+] " + article['title'] + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "[-] " + article['title'] + bcolors.ENDC)

print(bcolors.OKGREEN + "\n[+] " + str(confirmedEventCount) + " event articles found" + bcolors.ENDC)

print("\nConfirmed event articles")
print("-------------------------")
i = 0
for article in confirmedEventArticles:
    print(bcolors.OKGREEN + "[+] " + article['title'] + bcolors.ENDC)

    # NOTE: ONLY RUN THESE IF YOU HAVE THE out_base FILE WITH THE CORRECT BINARY IN THE DIRECTORY!!!_____________
    chems, quants = readBinary(article['body'])

    if len(chems)>0:
        print("CHEMICALS")
    for chem in chems:
        print(chem)
    if len(quants)>0:
        print("QUANTITIES")
    for quant in quants:
        print(quant)

    # For getting location information
    local = locationsInfo(article['body'])
    if len(local) > 0:
        print("Location")
    for sent in local:
        print(sent)

    offComm, people = officialComment(article['body'])
    if len(offComm)>0:
        print("OFFICIAL COMMENTS")
    for sent in offComm:
        print(sent)
#    database.Incidents(
#            chemicals=chems,
#            date="date",
#            location="location",
#            officialStatement=offComm,
#            articleLinks=["www.abcdefg"+str(i)+".com"]
#        ).save()
    i += 1
    if len(people)>0:
        print("PEOPLE")
    for ppl in people:
        print(ppl)

    # for pulling date information
    dates = dateInfo(article['body'])
    if len(dates)>0:
        print("DATE")
    for sent in dates:
        print(sent)
