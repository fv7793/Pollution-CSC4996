# import requests
# from bs4 import BeautifulSoup as soup
#
# page = requests.get("https://www.northernexpress.com/search/?query=pollution&content=news")
# soupPage = soup(page.content, 'html.parser')
# h3 = soupPage.find_all("h3")
# for link in h3:
#     print(link.a['href'])

link = "https://www.ironmountaindailynews.com/opinion/2015/06/michigan-utilities-work-to-comply-with-air-pollution-rule/"
newLink = link.split("/")
print(len(newLink))