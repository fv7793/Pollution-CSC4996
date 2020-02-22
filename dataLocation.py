#given the body of the article
#use POS tagging to find official statement
#find any date mentioned

#call the RNN binary on the body (what format should it be in?? how to call from script??)

#enter everything into the database

import spacy
import en_core_web_sm
from spacy.matcher import Matcher

nlp = en_core_web_sm.load()
pPt = Matcher(nlp.vocab)
pPt.add("pat1",None,
        [{"POS": "PROPN"},{"POS": "PUNCT", "OP":"?"}, {"POS": "DET", "OP":"?"},{"LEMMA": {"IN": [
                            "director","engineer","governer","mayor","manager",
                           "official","commissioner","representative", "chief", "coordinator"]}}]
        )
pPt.add("pat2",None,
        [{"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued", "warned"]}},
        {"POS":"NOUN","OP":"*"},{"LEMMA": {"IN": ["director","engineer","governer","mayor","manager",
                           "official","commissioner","representative","cheif","coordinator"]}}]
        )
pPt.add("pat3",None,[{"LEMMA": {"IN": ["official","Official"]}},
                     {"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued","warned"]}}]) #lemmatized words (said/discussed/etc.)

pPt.add("pat4",None,
        [{"LEMMA": {"IN": ["According", "according"]}}])

negP = Matcher(nlp.vocab)
negP.add("pat1",None,
        [{"LEMMA": {"IN": ["foundation", "non-profit", "company","spokesperson",
                           "spokeswoman","spokesman"]}}])
class locatedData:
    def __init__(self):
        chemicals = []
        date = ""
        #official stmt should be tuples (stmt, official title, name [optional])
        officialStmts = []
        quantities = []
        locations = []
        primaryLoc = ""
        #other locations (rivers, addresses, etc)??
        #otherLoc = []
        


def convertScrapedtoSent(splitContent):
    tokenizedSent = []
    #tokenize
    NLPtxt = nlp(splitContent)
    for eachSent in NLPtxt.sents:
        tokenizedSent.append(eachSent.string.strip())
    return tokenizedSent

txtfile = open("articlebodies.txt", 'r', encoding='utf-8')
line = txtfile.readline()
results = []
i=1
while(line):
    temp = convertScrapedtoSent(line)
    if '-DOCSTART-' in line:
        print("\nArticle "+str(i)+":")
        i = i+1
    for sent in temp:
        nER = nlp(sent)        
        matchesInSent = pPt(nER)
        neg1 = negP(nER)
        temp = nlp(sent.lower())
        secondMatch = pPt(temp)
        neg2 = negP(nER)
        if neg1 or neg2:
            continue
        elif matchesInSent or secondMatch:
            results.append(sent)
            print(sent)
            for entity in nER.ents:
                if entity.label_=="PERSON":
                    print("Name: ",entity.text, entity.label_)
    line = txtfile.readline()
    

txtfile.close()







##articleData = []
##for article in positiveArticles:
##    fullBody = ""
##
##    thisArticleData = locatedData()
##    
##    for paragraph in article.getArticleBody():
##        fullBody+=paragraph
##
##    sentences = convertScrapedtoSent(fullBody)
##    for sent in sentences:
##        #call location functions
##
##    #put found data into thisArticleData objects
##    articleData.append(thisArticleData)



