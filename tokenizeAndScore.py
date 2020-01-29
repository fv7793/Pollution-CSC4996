#function to take full
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

nlp = en_core_web_sm.load()

#Dictionary
#{'url':'Y'or'N'}
#18 positives, DFP crawler results, 5-10 clear negatives

#global array of large articles (urls)
    
#global array of med articles (urls)
#global array of small articles (urls)

#function that given "s","m","l" (numSent) can return the ideal float (0-50) for confirming the

#takes a full article, returns full sentences
def convertScrapedtoSent(splitContent):
    tokenizedSent = []
    #tokenize
    for eachPara in splitContent:
        NLPtxt = nlp(eachPara)
        for eachSent in NLPtxt.sents:
            tokenizedSent.append(eachSent.string.strip())

    for sentence in tokenizedSent:
        nER = nlp(sentence)
        #print(sentence)
        for entity in nER.ents:
            print(entity.text, entity.label_)
    return tokenizedSent


#function














