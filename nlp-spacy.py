import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from nltk import tokenize
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

tokenizedSent = []  
#nltk tokenize
for eachPara in arrayOfPs:
    #print(eachPara)
    listOfSent =(tokenize.sent_tokenize(eachPara))
    for sent in listOfSent:
        tokenizedSent.append(sent)
    
doc = nlp('I just bought 2 shares at 9 a.m. because the stock went up 30% in just 2 days according to the WSJ')
displacy.render(doc, style='ent', jupyter=True)

for sentence in tokenizedSent:
    nER = nlp(sentence)
    #displacy.serve(nER, style='ent') #this starts a server, don't use
    #displacy.render(nER, style="ent")
    print(sentence)
    for entity in nER.ents:
        print(entity.text, entity.label_)
    for word in nER:
        if(word.ent_iob_!='O'):
            print(word.idx, word.pos_, word.tag_, word.ent_iob_)
    

    
#print([(X.text, X.label_) for X in doc.ents])
