import requests
from bs4 import BeautifulSoup as soup

page1 = requests.get("https://thecountypress.mihomepaper.com/page/1/?s=pollution")
page2 = requests.get("https://thecountypress.mihomepaper.com/page/2/?s=pollution")
page3 = requests.get("https://thecountypress.mihomepaper.com/page/3/?s=pollution")
page = page1.content + page2.content + page3.content
soupPage = soup(page, 'html.parser')

pagex = requests.get("https://www.theoaklandpress.com/search/?sd=desc&l=25&s=start_time&f=html&t=article%2Cvideo%2Cyoutube%"
                     "2Ccollection&app%5B0%5D=editorial&nsa=eedition&q=pollution&o=25", allow_redirects=False)
print(pagex)