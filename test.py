import requests
from bs4 import BeautifulSoup as soup
import newspaper
from dateutil import parser

# page = requests.get("https://www.northernexpress.com/search/?query=pollution&content=news")
# soupPage = soup(page.content, 'html.parser')
# h3 = soupPage.find_all("h3")
# for link in h3:
#     print(link.a['href'])

page = requests.get("https://thecountypress.mihomepaper.com/articles/howell-bill-improves-technical-error-in-2018-solid-waste-statute/")
soupPage = soup(page.content, 'html.parser')
date = soupPage.find("span", {"class": "byline__time"})
d = parser.parse(date.get_text())

links = newspaper.build('https://thecountypress.mihomepaper.com/', memoize_articles=False)
for article in links.articles:
    print(article.url)


