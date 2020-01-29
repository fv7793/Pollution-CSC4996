import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

nlp = en_core_web_sm.load()

#takes a full article, returns full sentences
def convertScrapedtoSent(splitContent):

    tokenizedSent = []  
    #tokenize
    for eachPara in splitContent:
        NLPtxt = nlp(eachPara)
        for eachSent in NLPtxt.sents:
            tokenizedSent.append(eachSent.string.strip())

##    for sentence in tokenizedSent:
##        nER = nlp(sentence)
##        print(sentence)
##        for entity in nER.ents:
##            print(entity.text, entity.label_)
    return tokenizedSent



##    for word in nER:
##        if(word.ent_iob_!='O'):
##            print(word.idx, word.pos_, word.tag_, word.ent_iob_)
