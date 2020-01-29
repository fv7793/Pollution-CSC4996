
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
    #global array of scores with same indices (l)
#global array of med articles (urls)
    #global array of scores with same indices (m)
#global array of small articles (urls)
    #global array of scores with same indices (s)

#function that given "s","m","l" (based on numSent) can return the ideal float (0-50) for correctly identifying the highest number of articles of that size
    #loop 0-50 by .1
        #loop over that global array of urls
            #match each url with score (say Y/N based on val of loop)
            #see if Y/N was correct (add to correct or incorrect)
        #calculate the accuracy of this weight limit (# correct/#total articles of that size) -> (store if the best)
    #return best limit
        

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
    #get every URL and break into 'p' blocks

    #tokenization by convertScrapedtoSent
    #determine s/m/l -> add url to that global array
    #calculate the weight (rules/nlp/POS tagging) -> add weight to that global array

#calculate accuracy/best weight limit for s, then m, then l
    














