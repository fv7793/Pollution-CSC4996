import spacy
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

nlp = en_core_web_sm.load()

def URLtoClassName(URL):
    className = ""
    if 'michigansthumb.com' in URL:
        className = "article-body"
    elif 'monroenews.com' in URL:
        className = "inner"
    elif 'northjersey.com' in URL:
        className = "asset-double-wide"
    elif 'sentinel-standard.com' in URL:
        className = "inner"
    elif 'stignacenews.com' in URL:
        className =  'entry-content'
    elif 'sturgisjournal.com' in URL:
        className = 'inner'
    elif 'thedailyreporter.com' in URL:
        className = 'inner'
    elif 'mlive.com' in URL:
        className = 'entry-content'
    return className

def convertScrapedtoSent(splitContent):
    tokenizedSent = []
    #tokenize
    for eachPara in splitContent:
        NLPtxt = nlp(eachPara)
        for eachSent in NLPtxt.sents:
            tokenizedSent.append(eachSent.string.strip())
    return tokenizedSent


class articleClass:
    def __init__(self, URL, classBRN):
        self.artURL = URL
        self.classN = classBRN
        page = requests.get(URL)
        print("Parsing "+URL)
        bs = BeautifulSoup(page.text, 'html.parser')
        content=bs.find(class_=classBRN)
        splitContent = content.find_all('p')
        arrayOfPs = []
        for paragraph in splitContent:
            if(paragraph.contents):
                stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
                arrayOfPs.append(stringPara)
        self.tokSent = convertScrapedtoSent(arrayOfPs)
        temp = ""
        for sent in self.tokSent:
            temp=temp+" "+sent
        self.wholePara = temp

    def getContent(self):
        return self.wholePara



txtfile = open("sophia-positive200URLS.txt", 'r', encoding='utf-8')
line = txtfile.readline()
articles = []
while line:
    if line!='' and '*' not in line:
        className = URLtoClassName(line)
        articles.append(articleClass(line[:-1], className))
    line=txtfile.readline()
txtfile.close()

outfile = open("sophia-200-article-bodies.txt",'w',encoding='utf-8')
for article in articles:
    outfile.write("-DOCSTART-\n")
    outfile.write(article.getContent()+"\n")


outfile.close()
