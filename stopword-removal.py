import spacy
from spacy import displacy
from spacy.matcher import Matcher
from collections import Counter
import en_core_web_sm

from nltk import tokenize
from bs4 import BeautifulSoup
import requests
from spacy.lang.en.stop_words import STOP_WORDS

def switchStmt(pattern):
     patWeight= {
        "p0": 1.0,
        "p1":1.0,
        "p2":.5,
        "p3":.25,
        "p4":.75,
        "p5":.5,
        "p6":.5,
        "p7":.1,
        "p8":.1,
        #"p9", #SPECIAL
        #"p10", #SPECIAL
        "p11":.75,
        "p12":.75,
        "p13":1.0
    }
    return patWeight.get(pattern, 0.0)






page = requests.get('https://www.mininggazette.com/news/2019/08/mass-city-mercury-spill-contained/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='article')#'entry-content')#'asset-double-wide')

nlp = en_core_web_sm.load()


##START SCRAPING AND PARSING -----------------------------------------
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

##FILTER OUT STOPWORDS -----------------------------------------------
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

##--->RESULT: newSentences is an array of strings (each string is a sentence)





##START OF RULES --------------------------------------------------

patternsOfPOS = []
#(high)* levels of (a/the)* _____ chemical
#W = 1
patternsOfPOS.append([{"POS": "ADJ","OP":"?"},{"LEMMA": "levels"}, {"POS": "ADJ","OP":"?"},{"POS": "NOUN"}])
#(chemical) levels
#W = 1
patternsOfPOS.append([{"POS": "NOUN"},{"LEMMA": "levels"}])
#--->reported/found/occured on Month #
#W = .5
patternsOfPOS.append([{"LEMMA": {"IN": ["reported", "found", "occurred", "sighted"]}}, {"POS":"NOUN"}, {"POS":"NUM", "OP":"*"}])
##--->in a statement
#W = .25
patternsOfPOS.append([{"LEMMA": "statement"}])
#officials said/announced/etc ______
#W = .75
    ###IDEA!!! On finding this phrase, go back to original text and just store the whole sentence
patternsOfPOS.append([{"LEMMA": {"IN": ["official"]}},{"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued"]}}])  #lemmatized words (said/discussed/etc.)
#--->according to the _______
#W = .5
patternsOfPOS.append([{"LEMMA": {"IN": ["accord"]}},{"POS": "NOUN"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["accord"]}},{"POS": "NNP"}])
#??? ---> ??? highly dangerous chemical / testing showed ___ levels
#W = .1 (TOOOOOOOO GENERAL)
patternsOfPOS.append([{"POS":"NOUN"},{"POS":"VERB"}, {"POS":"ADV","OP":"*"}, {"POS":"ADJ"},{"POS":"NOUN"}])
patternsOfPOS.append([{"POS":"NOUN"},{"POS":"VERB"}, {"POS":"ADV"}, {"POS":"ADJ","OP":"*"},{"POS":"NOUN"}])

##POLLUTION-RELATED RULES
#polluted/contaminated ___ proper noun or regular noun
#W = 1 (BUT ONLY IF THEY PASS THE SECOND TEST!!!)
patternsOfPOS.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}},{"POS": "NNP"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}},{"POS": "NOUN"}])

#9 or 10, then go look in original

## rules for units examplehttps://www.lansingstatejournal.com/story/news/2019/10/14/11-million-gallons-sewage-water-dumped-grand-red-cedar-river/3975129002/
# number UNIT of
#W = .75
patternsOfPOS.append([{"POS": "CD"},{"LEMMA": {"IN": ["gallon", "ppt", "ppb", "ton"]}}])
#W = .75
patternsOfPOS.append([{"LEMMA": {"IN": ["cause","source"]}},{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}}])
#W = 1
patternsOfPOS.append([{"POS": "NOUN"},{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}}])


listOfMatchPats = Matcher(nlp.vocab)
pPt = Matcher(nlp.vocab)

pollPats = []
pollPats.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}},{"POS":"ADP","OP":"?"},{"POS":"DET","OP":"?"},{"POS":"ADP","OP":"?"},{"POS": "NNP"}])
pollPats.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}},{"POS":"ADP","OP":"?"},{"POS":"DET","OP":"?"},{"POS":"ADP","OP":"?"},{"POS": "NOUN"}])
i=0
for pat in pollPats:
    pPt.add("pat"+str(i),None,pat)
    i=i+1
    
#ADDS ALL PATTERNS TO THE MATCHER VOCAB LIST ----------------------------------------------
pNum = 0
for pattern in patternsOfPOS:
    listOfMatchPats.add("p"+str(pNum), None, pattern) #p1 = matchID, no callback, matches the pattern
    pNum=pNum+1

#MATCH AND PRINT ALL PATTERNS ----------------------------------------
totalArtVal = 0.0
k = 0
for sentence in newSentences:
    nER = nlp(sentence)
    #print(sentence)
    matchesInSent = listOfMatchPats(nER)
    if matchesInSent:
        print("----------------------")
    for mID, s, e in matchesInSent:
        strID = nlp.vocab.strings[mID]  #convert from span object to string
        if(strID=="p9" or strID=="p10"):
            ##if it was one of the pollution patterns
            testStr=tokenizedSent[k]
            posPol = nlp(testStr)
            matches = pPt(posPol)
            if matches:
                print("******************")
            for m, st, en in matches:
                sID = nlp.vocab.strings[m]
                sTE = posPol[st:en]
                print(m, sID, st, en, sTE.text)
                print("******************")
                totalArtVal = totalArtVal+1.0
        else:
            ##if it was NOT one of the pollution patterns
            totalArtVal = totalArtVal+switchStmt(strID)
        startToEnd = nER[s:e]  #string match idx from start to end
        print(mID, strID, s, e, startToEnd.text)
    k=k+1

print("RESULTING VALUE: ", totalArtVal)




















