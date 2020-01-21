import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.freep.com/story/news/local/michigan/oakland/2020/01/10/madison-heights-green-ooze-slime-pfas/4437379002/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-double-wide')

nlp = en_core_web_sm.load()

splitContent = content.find_all('p')
arrayOfPs = []

i=0;
for paragraph in splitContent:
    if i > 4: #only want the 1st ~10 sentences of the article *for now* (avoid the filtering of the embedded tags and tricky format stuff
        break
    else:
        #print(type(paragraph.contents[0])) #type = navigable string (beautiful soup type)
        stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
        #print(type(stringPara)) #str
        arrayOfPs.append(stringPara)
        i=i+1
    
#nltk tokenize
for eachPara in arrayOfPs:
    print(eachPara)

    
#print([(X.text, X.label_) for X in doc.ents])
