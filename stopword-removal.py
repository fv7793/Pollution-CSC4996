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
patternsOfPOS.append([{"POS": "ADJ","OP":"?"},{"LEMMA": "levels"}, {"POS": "ADJ","OP":"?"},{"POS": "NOUN"}])
#(chemical) levels
patternsOfPOS.append([{"POS": "NOUN"},{"LEMMA": "levels"}])
#--->reported/found/occured on Month #
patternsOfPOS.append([{"LEMMA": {"IN": ["reported", "found", "occurred", "sighted"]}}, {"POS":"NOUN"}, {"POS":"NUM", "OP":"*"}])
##--->in a statement
patternsOfPOS.append([{"LEMMA": "statement"}])
#officials said/announced/etc ______
    ###IDEA!!! On finding this phrase, go back to original text and just store the whole sentence
patternsOfPOS.append([{"POS": "NOUN"},{"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued"]}}])  #lemmatized words (said/discussed/etc.)
#--->according to the _______
patternsOfPOS.append([{"LEMMA": {"IN": ["accord"]}},{"POS": "ADP"},{"POS": "NOUN"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["accord"]}},{"POS": "ADP"},{"POS": "NNP"}])
#??? ---> ??? highly dangerous chemical / testing showed ___ levels
patternsOfPOS.append([{"POS":"NOUN"},{"POS":"VERB"}, {"POS":"ADV","OP":"*"}, {"POS":"ADJ"},{"POS":"NOUN"}])
patternsOfPOS.append([{"POS":"NOUN"},{"POS":"VERB"}, {"POS":"ADV"}, {"POS":"ADJ","OP":"*"},{"POS":"NOUN"}])
#near (the)* (proper noun location)
patternsOfPOS.append([{"POS": "ADP"},{"POS": "NNP"}])
##direction (of)* city
patternsOfPOS.append([{"POS": "ADJ"}, {"POS": "NNP"}])

##POLLUTION-RELATED RULES
#polluted/contaminated the (1) proper noun (2) regular noun
patternsOfPOS.append([{"LEMMA": {"IN": ["polluted", "contaminated"]}},{"POS": "NNP"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["polluted", "contaminated"]}},{"POS": "NOUN"}])
#pollution/contamination at the (1) proper noun (2) regular noun
patternsOfPOS.append([{"LEMMA": {"IN": ["pollute", "contaminate"]}},{"POS": "NNP"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["pollute", "contaminate"]}},{"POS": "NOUN"}])
#spilled/poured into the (1) proper noun (2) regular noun
patternsOfPOS.append([{"LEMMA": {"IN": ["spilled", "poured"]}}, {"POS": "NNP"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["spilled", "poured"]}}, {"POS": "NOUN"}])
#spill/contamination found near (1) proper noun (2) regular noun
patternsOfPOS.append([{"LEMMA": {"IN": ["spill", "contamination"]}}, {"POS": "NNP"}])
patternsOfPOS.append([{"LEMMA": {"IN": ["spill", "contamination"]}}, {"POS": "NOUN"}])
## rules for units examplehttps://www.lansingstatejournal.com/story/news/2019/10/14/11-million-gallons-sewage-water-dumped-grand-red-cedar-river/3975129002/
# number UNIT of
patternsOfPOS.append([{"POS": "CD"},{"LEMMA": {"IN": ["spill", "contamination"]}}, {"POS": "NOUN"}])
# number UNIT poured/spilled/polluted/contaminated

listOfMatchPats = Matcher(nlp.vocab)

#ADDS ALL PATTERNS TO THE MATCHER VOCAB LIST ----------------------------------------------
pNum = 0
for pattern in patternsOfPOS:
    listOfMatchPats.add("p"+str(pNum), None, pattern) #p1 = matchID, no callback, matches the pattern
    pNum=pNum+1

#MATCH AND PRINT ALL PATTERNS ----------------------------------------
for sentence in newSentences:
    nER = nlp(sentence)
    #print(sentence)
    matchesInSent = listOfMatchPats(nER)
    if matchesInSent:
        print("----------------------")
    for mID, s, e in matchesInSent:
        strID = nlp.vocab.strings[mID]  #convert from span object to string
        startToEnd = nER[s:e]  #string match idx from start to end
        print(mID, strID, s, e, startToEnd.text)




















