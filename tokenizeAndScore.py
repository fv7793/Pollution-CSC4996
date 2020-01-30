
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

nlp = en_core_web_sm.load()

#article class
    #URL
    #numSent
    #array of tokenized sent
    #class breakdown name (html)
    #T/F (is or is not an actual event)

    #get tokSent
    #constructor - URL, class breakdown name, T/F
        #run BS, get p blocks
        #call tokenizing and store in object's tS array
        #calculate numsent by len() of tS
        #T/F
    #isEvent
        #returns T/F


#function - given article object
    #run at least 2 rules on it
    #returns if it was found to be T/F
        

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




#main
#for each URL
    #initialize an article class obj
    
    #determine T/F by function call of rules
#calculate accuracy
    #num of obj correctly found T/F / num total obj
    #num false +, num false -, num true +, num true -
    














