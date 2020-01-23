import spacy
from spacy import displacy
from spacy.matcher import Matcher
from collections import Counter
import en_core_web_sm
from nltk import tokenize
from bs4 import BeautifulSoup
import requests
from spacy.lang.en.stop_words import STOP_WORDS

page = requests.get('https://www.mlive.com/news/grand-rapids/2019/08/coal-ash-from-west-michigan-power-plant-might-be-contaminating-drinking-water-wells.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='entry-content')#'asset-double-wide')

nlp = en_core_web_sm.load()

splitContent = content.find_all('p')
arrayOfPs = []

for paragraph in splitContent:
    stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
    arrayOfPs.append(stringPara)

tokenizedSent = []  
#nltk tokenize
for eachPara in arrayOfPs:
    listOfSent =(tokenize.sent_tokenize(eachPara))
    for sent in listOfSent:
        tokenizedSent.append(sent)
        
newSentences = []
for sent in tokenizedSent:
    NLPtxt = nlp(sent)
    filtered = ""
    for word in NLPtxt:
        #testWord = nlp.vocab[word]
        if word.is_stop == False and word.is_punct==False:
            filtered=filtered+" "+str(word)
        elif str(word)=='"' or str(word)=='.':
            filtered=filtered+str(word)
    newSentences.append(filtered)

for sent in newSentences:
    print(sent)










