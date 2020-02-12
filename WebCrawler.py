import random
from lib2to3.pgen2 import driver

import requests
from bs4 import BeautifulSoup as soup, BeautifulSoup, SoupStrainer
import time
from selenium import webdriver
# Gets the all urls from a website
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

#To do rotate user agents and rotate proxys
# Launches a chrometab which goes to all the urls that were specified.
def goToSearchUrl(link):
    chrome_options1 = Options()
    chrome_options1.add_argument("--headless")
    chrome_options1.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
    driver = webdriver.Chrome('C:/Users/mhere/OneDrive/Desktop/chromedriver', options=chrome_options1)
    page1=driver.get(link)
    print("Page")
    print(link)
    pageSource=driver.page_source
    time.sleep(2)
    #driver.quit()
    return pageSource

# Allows us to change the keyword for every website we need to collect data on.
def readAndReplaceFromFileWebLinks(key):
    urls = []
    num= []
    with open("WebLinks.txt", "r") as file:
        for line in file:
            #Imports the words from the key file to replace the keyword in every search url
            with open("Keyword.txt", "r") as keyFile:
                for key in keyFile:
                    line.replace("Pollution", key)
                    for numbers in range(1,2):
                        urls.append(line.replace("Pollution", key.rstrip()).replace("pageNum", str(numbers)).rstrip())
    print("Urls")
    print(urls)
    return urls
    print(url)
# Allows us to change the keyword for every website we need to collect data on.
def readFromFileWebLinks(key):
    urls = []
    num= []
    with open("WebLinks.txt", "r") as file:
        for line in file:
            urls.append(line.rstrip())
    print("Urls")
    print(urls)
    return urls

def getClassesForDates():
    dates= []
    with open("Date.txt", "r") as file:
        for line in file:
            dates.append(line.rstrip())
    print(dates)
    return dates

#Reads the classes which contain the article links in from classes.txt
def readFromFileClasses():
    classes = []
    with open("Classes.txt", "r") as file:
        for line in file:
            classes.append(line.rstrip())
    return classes

def mapClassesToTUrls(finalClasses):
    dict = {}
    for x in range(len(finalClasses)-1):
        className = finalClasses[x]
        url = urlsFromFile[x]
        dict1 = {url: className}
        dict.update(dict1)
    return dict

#Strips the artcile links of unneeded html and puts them in Results.txt
def getHyperlinkToArticle(file):
    hyperlink = str(weblink.find("a", href=True))
    if (hyperlink != "None"):
        formattedHyperlink=hyperlink.split('"', 2)[1]
        results.append(formattedHyperlink)
        file.writelines(formattedHyperlink)
        file.writelines('\n')
        print(str(weblink.find("a", href=True)).split('"', 2)[1])

def articlePusblishedIn2019To2020(dateSpan):
    print(dateSpan.__contains__("2020"))
    if dateSpan.contains("2019"):
        return True
    else:
        return False

key= []
print(key)
#final urls replaced with urls from file
urlsFromFile = readFromFileWebLinks(key)
finalClasses = readFromFileClasses()
mappedClasses = mapClassesToTUrls(finalClasses)
articleClasssesForDates = getClassesForDates()
results = []
resultsFile = open("Results.txt", "w")
for url in mappedClasses:
        #generate correct urls using keyword and page
        finalUrls = readAndReplaceFromFileWebLinks(key)
        for link in finalUrls:
            page=goToSearchUrl(link)
            classSearchTerm = mappedClasses.get(link)
            soup = BeautifulSoup(page, 'html.parser')
            weblinks=soup.find_all(True, {'class': [finalClasses]})
           # soup1 = BeautifulSoup(page, 'html.parser')
            #dates=soup1.find_all(True, {'class': [articleClasssesForDates]})
            #print("Date")
            #print(dates)
            #counter=0
            for weblink in weblinks:
                #if articlePusblishedIn2019To2020(dates[counter]):
                    getHyperlinkToArticle(resultsFile)
                    #counter=counter+1
resultsFile.close()

