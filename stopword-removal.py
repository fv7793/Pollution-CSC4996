import spacy
from spacy import displacy
from spacy.matcher import Matcher
from collections import Counter
import en_core_web_sm

from bs4 import BeautifulSoup
import requests
from spacy.lang.en.stop_words import STOP_WORDS

import nlp_spacy


nlp = en_core_web_sm.load()
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

##END OF RULES -----------------------------------------------------------------------

numShort = 0
numMed = 0
numLong = 0
avgShort = 0.0
avgMed = 0.0
avgLong = 0.0
    
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




def contentToOutput(content):
    global numShort
    global numMed
    global numLong

    global avgShort
    global avgMed
    global avgLong
##START SCRAPING AND PARSING -----------------------------------------
    splitContent = content.find_all('p')
    arrayOfPs = []

    for paragraph in splitContent:
        stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
        arrayOfPs.append(stringPara)
    tokenizedSent = nlp_spacy.convertScrapedtoSent(arrayOfPs)

##FILTER OUT STOPWORDS -----------------------------------------------
    newSentences = []
    numSentences = 0
    for sent in tokenizedSent:
        numSentences = numSentences+1
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
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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

    if(numSentences<=20):
        numShort = numShort+1
        avgShort = avgShort+totalArtVal
    elif numSentences>50:
        numLong = numLong+1
        avgLong= avgLong+totalArtVal
    else:
        numMed = numMed+1
        avgMed= avgMed+totalArtVal
    print("NUM SENT:", numSentences)
    print("RESULTING VALUE: ", totalArtVal)





#2
page = requests.get('https://www.crainsdetroit.com/article/20180309/news01/654831/toxic-chemicals-found-in-new-baltimore-mount-clemens-ira-township')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='field--name-field-paragraph-body')

contentToOutput(content)

#3
page = requests.get('https://www.crainsdetroit.com/article/20180417/news01/658401/testing-finds-contaminated-wells-near-grand-rapids-area-airport')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='field--name-field-paragraph-body')

contentToOutput(content)

#4
page = requests.get('https://www.crainsdetroit.com/article/20180403/news01/656966/synthetic-coolant-leaks-from-power-cables-in-michigan-waters')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='field--name-field-paragraph-body')

contentToOutput(content)

#5
page = requests.get('https://www.dailytribune.com/news/concerns-grow-over-tainted-sewage-sludge-spread-on-lapeer-croplands/article_6c8bc1a6-a71c-5775-a3b9-f6db18248d26.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-content')

contentToOutput(content)

#6
page = requests.get('http://www.pressandguide.com/news/tlaib-statement-on-revere-copper-site-collapse-into-detroit-river/article_c1ef5fa8-1a0e-11ea-a18b-3b3e5b366236.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-content')

contentToOutput(content)

#7
page = requests.get('https://www.candgnews.com/news/officials-search-for-petroleum-leak-source-into-clinton-river-116417')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='article-body-text')

contentToOutput(content)

#8
page = requests.get('https://www.lansingstatejournal.com/story/news/2019/10/14/11-million-gallons-sewage-water-dumped-grand-red-cedar-river/3975129002/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-double-wide')

contentToOutput(content)

#9
page = requests.get('https://www.lansingstatejournal.com/story/news/local/2019/04/22/racer-trust-proposes-fix-dioxane-pollution-lansing-township-gm-water-quality/3330212002/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-double-wide')

contentToOutput(content)

#10
page = requests.get('https://www.mlive.com/news/kalamazoo/2019/03/contamination-plume-leaves-manufacturing-property-in-kalamazoo-township.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='entry-content')

contentToOutput(content)

#11
page = requests.get('https://www.mlive.com/news/detroit/2018/10/detroit_schools_to_spend_38_mi.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='entry-content')

contentToOutput(content)

#12
page = requests.get('https://www.mlive.com/news/2019/03/toxic-pollution-at-wolverine-tannery-is-extensive-data-confirms.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='entry-content')

contentToOutput(content)

#13
page = requests.get('https://www.mlive.com/news/grand-rapids/2019/08/coal-ash-from-west-michigan-power-plant-might-be-contaminating-drinking-water-wells.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='entry-content')

contentToOutput(content)

#14
page = requests.get('https://www.candgnews.com/news/officials-investigate-plumbrook-drain-oil-report--111626')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='article-body-text')

contentToOutput(content)

#15
page = requests.get('https://www.candgnews.com/news/royal-oak-warns-residents-of-action-level-lead-in-water-115688')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='article-body-text')

contentToOutput(content)

#16
page = requests.get('https://www.mininggazette.com/news/2019/08/mass-city-mercury-spill-contained/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='article')

contentToOutput(content)

#17
page = requests.get('https://www.freep.com/story/news/local/michigan/oakland/2020/01/10/madison-heights-green-ooze-slime-pfas/4437379002/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-double-wide')

contentToOutput(content)

#18
page = requests.get('https://www.freep.com/story/news/local/michigan/2017/03/24/mercury-rising-scientists-puzzled-metals-jump-great-lakes-fish/99306786/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-double-wide')

contentToOutput(content)

avgShort = avgShort/numShort
avgMed = avgMed/numMed
avgLong = avgLong/numLong
print("SHORT: ", numShort, "AVG: ", avgShort)
print("MED: ", numMed, "AVG: ", avgMed)
print("LONG: ", numLong, "AVG: ", avgLong)
