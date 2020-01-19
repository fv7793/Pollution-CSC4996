from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.lenconnect.com/news/20200118/overnight-winter-storm-turns-slushy')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='article-body')
splitContent = content.find_all('p')
for block in splitContent:
    if block.contents and block.contents[0] != '':
        print(block.contents[0])
