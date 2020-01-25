import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

nlp = en_core_web_sm.load()

#takes a full article, returns full sentences
def convertScrapedtoSent(splitContent):
    arrayOfPs = []
    for paragraph in splitContent:
	#type = navigable string (beautiful soup type)
	stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
	#type is now str
	arrayOfPs.append(stringPara)

    tokenizedSent = []  
    #tokenize
    for eachPara in arrayOfPs:
	NLPtxt = nlp(eachPara)
	for eachSent in NLPtxt.sents:
		tokenizedSent.append(eachSent.string.strip())
    return tokenizedSent


##for sentence in tokenizedSent:
##    nER = nlp(sentence)
##    print(sentence)
##    for entity in nER.ents:
##        print(entity.text, entity.label_)
##    for word in nER:
##        if(word.ent_iob_!='O'):
##            print(word.idx, word.pos_, word.tag_, word.ent_iob_)
