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

page = requests.get('https://www.freep.com/story/news/local/michigan/oakland/2020/01/10/madison-heights-green-ooze-slime-pfas/4437379002/')
bs = BeautifulSoup(page.text, 'html.parser')
content=bs.find(class_='asset-double-wide')

nlp = en_core_web_sm.load()

splitContent = content.find_all('p')
arrayOfPs = []

i=0;
##THIS LINE LIMIT WILL BE GONE WHEN WE ARE HANDED CLEAN DATA
for paragraph in splitContent:
    if i > 4: #only want the 1st ~10 sentences of the article *for now* (avoid the filtering of the embedded tags and tricky format stuff
        break
    else:
        #print(type(paragraph.contents[0])) #type = navigable string (beautiful soup type)
        stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
        #print(type(stringPara)) #str
        arrayOfPs.append(stringPara)
        i=i+1

tokenizedSent = []  
#nltk tokenize
for eachPara in arrayOfPs:
    #print(eachPara)
    listOfSent =(tokenize.sent_tokenize(eachPara))
    for sent in listOfSent:
        tokenizedSent.append(sent)

# Matches "love cats" or "likes flowers"
expat = [{"LEMMA": {"IN": ["like", "love"]}},
            {"POS": "NOUN"}]
##print every noun and past tense verb!
pattern1 = [{"POS":"NOUN"},{"POS":"VBD"}]
##print every preposition and object of preposition!!
pattern2 = [{"POS":"prep"},{"POS":"pobj"}]
pattern3 = [{"POS":"pobj"},{"POS":"prep"}]
##print every proper noun object of the preposition and preposition!!
pattern4 = [{"POS": "NNP"}, {"POS": "prep"}]
pattern5 = [{"POS": "prep"}, {"POS": "NNP"}]
##adjective proper nouns
pattern6 = [{"POS": "ADJ"}, {"POS": "NNP"}]

listOfMatchPats = Matcher(nlp.vocab)
listOfMatchPats.add("p1", None, pattern1) #p1 = matchID, no callback, matches the pattern
listOfMatchPats.add("p2", None, pattern2)
listOfMatchPats.add("p3", None, pattern3)
listOfMatchPats.add("p4", None, pattern4)
listOfMatchPats.add("p5", None, pattern5)
listOfMatchPats.add("p6", None, pattern6)


for sentence in tokenizedSent:
    nER = nlp(sentence)
    #print(sentence)
    matchesInSent = listOfMatchPats(nER)
    if matchesInSent:
        print("xxxxx")
    for mID, s, e in matchesInSent:
        strID = nlp.vocab.strings[mID]  #convert from span object to string
        startToEnd = nER[s:e]  #string match idx from start to end
        print(mID, strID, s, e, startToEnd.text)
##    for entity in nER.ents:
##        print(entity.text, entity.label_)
##    for word in nER:
##        if(word.ent_iob_!='O'):
##          print(word.pos_, word.tag_)


