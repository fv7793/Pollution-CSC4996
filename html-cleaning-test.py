from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.lenconnect.com/news/20200118/overnight-winter-storm-turns-slushy')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find('body')        #class_='article-body')
#THIS IS THE MAIN PROBLEM (the developer has to inspect the html and find the container class for that specific page for this to work
splitContent = content.find_all('p')
for block in splitContent:
    if block.contents and block.contents[0] != '':
        print(block.contents[0])
