
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests

nlp = en_core_web_sm.load()

pPt = Matcher(nlp.vocab)
pollPats = []
pollPats.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}},{"POS":"ADP","OP":"?"},{"POS":"DET","OP":"?"},{"POS":"ADP","OP":"?"},{"POS": "PROPN"}])
pollPats.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}},{"POS":"ADP","OP":"?"},{"POS":"DET","OP":"?"},{"POS":"ADP","OP":"?"},{"POS": "NOUN"}])
i=0
for pat in pollPats:
    pPt.add("pat"+str(i),None,pat)
    i=i+1

#article class
class articleClass:
    def __init__(self, URL, classBRN, isEvent):
        self.artURL = URL
        self.classN = classBRN
        self.event = isEvent
        page = requests.get(URL)
        bs = BeautifulSoup(page.text, 'html.parser')
        content=bs.find(class_=classBRN)
        splitContent = content.find_all('p')
        arrayOfPs = []
        for paragraph in splitContent:
            stringPara = str(paragraph.contents[0]) #CONVERT TO UNICODE
            arrayOfPs.append(stringPara)
        self.tokSent = convertScrapedtoSent(arrayOfPs)
        self.numSent = len(self.tokSent)

    def getTS(self):
        return self.tokSent

    def isEvent(self):
        return self.event



#function - given article object
def isArticleEvent(articleObj):
    isEvent = False
    temp = articleObj.getTS()
    for sentence in temp:
        nER = nlp(sentence)
        matchesInSent = pPt(nER)
        if matchesInSent:
            isEvent = True
        for mID, s, e in matchesInSent:
            strID = nlp.vocab.strings[mID]  #convert from span object to string
            startToEnd = nER[s:e]
            #print(mID, strID, s, e, startToEnd.text)
    return isEvent
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
    return tokenizedSent




#main
#for each URL
    #initialize an article class obj
articleObjs = []

articleObjs.append(articleClass('https://www.crainsdetroit.com/article/20180309/news01/654831/toxic-chemicals-found-in-new-baltimore-mount-clemens-ira-township', 'field--name-field-paragraph-body', True))
articleObjs.append(articleClass('https://www.crainsdetroit.com/article/20180417/news01/658401/testing-finds-contaminated-wells-near-grand-rapids-area-airport', 'field--name-field-paragraph-body', True))
articleObjs.append(articleClass('https://www.crainsdetroit.com/article/20180403/news01/656966/synthetic-coolant-leaks-from-power-cables-in-michigan-waters', 'field--name-field-paragraph-body', True))
articleObjs.append(articleClass('https://www.dailytribune.com/news/concerns-grow-over-tainted-sewage-sludge-spread-on-lapeer-croplands/article_6c8bc1a6-a71c-5775-a3b9-f6db18248d26.html', 'asset-content', True))
articleObjs.append(articleClass('http://www.pressandguide.com/news/tlaib-statement-on-revere-copper-site-collapse-into-detroit-river/article_c1ef5fa8-1a0e-11ea-a18b-3b3e5b366236.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.candgnews.com/news/officials-search-for-petroleum-leak-source-into-clinton-river-116417', 'article-body-text', True))
articleObjs.append(articleClass('https://www.lansingstatejournal.com/story/news/2019/10/14/11-million-gallons-sewage-water-dumped-grand-red-cedar-river/3975129002/', 'asset-double-wide', True))
articleObjs.append(articleClass('https://www.lansingstatejournal.com/story/news/local/2019/04/22/racer-trust-proposes-fix-dioxane-pollution-lansing-township-gm-water-quality/3330212002/', 'asset-double-wide', True))
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2019/03/contamination-plume-leaves-manufacturing-property-in-kalamazoo-township.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/detroit/2018/10/detroit_schools_to_spend_38_mi.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/2019/03/toxic-pollution-at-wolverine-tannery-is-extensive-data-confirms.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2019/08/coal-ash-from-west-michigan-power-plant-might-be-contaminating-drinking-water-wells.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.candgnews.com/news/officials-investigate-plumbrook-drain-oil-report--111626', 'article-body-text', True))
articleObjs.append(articleClass('https://www.candgnews.com/news/royal-oak-warns-residents-of-action-level-lead-in-water-115688', 'article-body-text', True))
articleObjs.append(articleClass('https://www.mininggazette.com/news/2019/08/mass-city-mercury-spill-contained/', 'article', True))
articleObjs.append(articleClass('https://www.freep.com/story/news/local/michigan/oakland/2020/01/10/madison-heights-green-ooze-slime-pfas/4437379002/', 'asset-double-wide', True))
articleObjs.append(articleClass('https://www.freep.com/story/news/local/michigan/2017/03/24/mercury-rising-scientists-puzzled-metals-jump-great-lakes-fish/99306786/', 'asset-double-wide', True))
articleObjs.append(articleClass('https://www.petoskeynews.com/news/community/michigan-says-soybeans-must-be-destroyed-due-to-soil/article_c9afc10b-2dc2-5c2b-97d5-26b55d8bf933.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.petoskeynews.com/charlevoix/black/toxic-land-one-family-s-story/article_0e18578b-66fa-56ff-9f4b-77666799cab1.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.petoskeynews.com/ap/state/cleanup-of-contaminated-site-is-expected-to-cost-millions/article_9d317aec-edf6-59ee-b35d-1351e5876012.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.petoskeynews.com/featured-pnr/leak-reported-from-wastewater-pump-station-line-in-harbor-springs/article_c15ca4d0-6cdf-5dc6-ac94-ab259e9a2d77.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.petoskeynews.com/gaylord/news/local/crews-clean-up-fuel-oil-spill-along-walloon-lake-shore/article_ec93ee17-73f6-5461-911a-45164fc0ed79.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.petoskeynews.com/news/state-region/michigan-sues-m-dupont-over-forever-chemicals-in-water/article_5a3d491d-45cf-5876-b216-2d6417a0a63c.html', 'asset-content', True))
#articleObjs.append(articleClass('https://michiganchronicle.com/2018/04/03/pollution-and-southwest-detroit/', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/ann-arbor/2020/01/sewer-line-break-leaks-50-gallons-in-augusta-township.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2019/10/hazmat-crew-called-to-nitrogen-tank-leak-near-ford-airport-roads-blocked.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/muskegon/2019/09/edgewood-elementary-in-muskegon-heights-evacuated-due-to-gas-leak-in-roadway.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2019/09/city-inspecting-pipes-under-kalamazoo-after-two-sewage-leaks-into-river.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/flint/2019/08/buick-city-site-will-close-sewer-that-leaks-pfas-into-the-flint-river.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/flint/2019/05/crews-work-to-repair-lapeer-sewer-line-gas-leak.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2019/06/two-people-treated-at-hospital-after-barrel-leaks-chemical-fumes-blow-toward-business.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/muskegon/2020/01/estimated-132000-gallons-of-untreated-sewage-spill-after-pipe-break-near-muskegon.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2018/10/no_threat_to_public_after_leak.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/saginaw/2018/09/chemical_leak_at_semiconductor.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2014/03/up_to_755_gallons_of_crude_oil.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.mlive.com/news/2019/09/110k-fine-levied-for-downtown-grand-rapids-air-pollution.html', 'entry-content', True))
articleObjs.append(articleClass('https://www.record-eagle.com/state/superfund-cleanup-considered-for-detroit-green-goo-site/article_428248df-1ac8-5063-8ce0-02a4c1cf4481.html', 'asset-content', True))
articleObjs.append(articleClass('https://www.mibiz.com/sections/manufacturing/state-continues-air-pollution-probe-at-grand-rapids-medical-sterilizer?highlight=WyJwb2xsdXRpb24iXQ==', 'pigeon-first-p', True))

totalNum = len(articleObjs)
numCorrect = 0
n=0
for article in articleObjs:
    n=n+1
    result = isArticleEvent(article)
    print(""+str(n)+" " + str(result))
    if result==article.isEvent():
        numCorrect = numCorrect+1
    #determine T/F by function call of rules
#calculate accuracy
accuracy = numCorrect/totalNum
print("FINAL ACCURACY = "+str(accuracy))
    #num of obj correctly found T/F / num total obj
    #num false +, num false -, num true +, num true -
    














