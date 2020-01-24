##print every noun and past tense verb!
##print every preposition and object of preposition!!
##print every proper noun object of the preposition and preposition!!
##adjective proper nouns

##LATER-----
    #lemmatize key words for pollution
    #units
    #locating chemical based on position of words (find high lvl of then find chemical by looking at the next word??)
        #lemmatized word for pollution by/with
        #found ____ in
    #on ___ in proper noun


import spacy
from spacy import displacy
from spacy.matcher import Matcher
from collections import Counter
import en_core_web_sm
from nltk import tokenize
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.mlive.com/news/grand-rapids/2019/08/coal-ash-from-west-michigan-power-plant-might-be-contaminating-drinking-water-wells.html')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='entry-content')#'asset-double-wide')

nlp = en_core_web_sm.load()

splitContent = content.find_all('p')
arrayOfPs = []

for paragraph in splitContent:
    #print(type(paragraph.contents[0])) #type = navigable string (beautiful soup type)
    stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
    #print(type(stringPara)) #str
    arrayOfPs.append(stringPara)

tokenizedSent = []  
#nltk tokenize
for eachPara in arrayOfPs:
    #print(eachPara)
    listOfSent =(tokenize.sent_tokenize(eachPara))
    for sent in listOfSent:
        tokenizedSent.append(sent)

##START OF RULES --------------------------------------------------

patternsOfPOS = []
#(high)* levels of (a/the)* _____ chemical
patternsOfPOS.append([{"POS": "ADJ","OP":"?"},{"LEMMA": "levels"}, {"POS": "ADJ","OP":"?"},{"POS": "NOUN"}])
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
patternsOfPOS.append([{"POS":"NOUN"},{"POS":"VERB"}, {"POS":"ADV","OP":"*"}, {"POS":"ADJ","OP":"*"},{"POS":"NOUN"}])
#near (the)* (proper noun location)
patternsOfPOS.append([{"POS": "ADP"},{"POS": "NNP"}])
##direction (of)* city
patternsOfPOS.append([{"POS": "ADJ"}, {"POS": "NNP"}])

<<<<<<< HEAD
#LATER
#lemmatize key words for pollution
#units
=======
>>>>>>> fb39793ca5a1ba2abb929cc160adc0f41c778e3a

listOfMatchPats = Matcher(nlp.vocab)

#ADDS ALL PATTERNS TO THE MATCHER VOCAB LIST ----------------------------------------------
pNum = 0
for pattern in patternsOfPOS:
    listOfMatchPats.add("p"+str(pNum), None, pattern) #p1 = matchID, no callback, matches the pattern
    pNum=pNum+1

#MATCH AND PRINT ALL PATTERNS
for sentence in tokenizedSent:
    nER = nlp(sentence)
    #print(sentence)
    matchesInSent = listOfMatchPats(nER)
    if matchesInSent:
        print("----------------------")
    for mID, s, e in matchesInSent:
        strID = nlp.vocab.strings[mID]  #convert from span object to string
        startToEnd = nER[s:e]  #string match idx from start to end
        print(mID, strID, s, e, startToEnd.text)
##    for entity in nER.ents:
##        print(entity.text, entity.label_)
##    for word in nER:
##        if(word.ent_iob_!='O'):
##          print(word.pos_, word.tag_)


