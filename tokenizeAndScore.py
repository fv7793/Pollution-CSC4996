
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

pollPats.append([{"POS": "NOUN"},{"LEMMA": {"IN": ["levels","contamination"]}}])
pollPats.append([{"POS": "NOUN"},{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}}])


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
        print("Parsing "+URL)
        bs = BeautifulSoup(page.text, 'html.parser')
        content=bs.find(class_=classBRN)
        splitContent = content.find_all('p')
        arrayOfPs = []
        for paragraph in splitContent:
            if(paragraph.contents):
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

#POSITIVES (key terms for identifying if “contamination event”)
#1
articleObjs.append(articleClass('https://www.crainsdetroit.com/article/20180309/news01/654831/toxic-chemicals-found-in-new-baltimore-mount-clemens-ira-township', 'field--name-field-paragraph-body', True))
#2
articleObjs.append(articleClass('https://www.crainsdetroit.com/article/20180417/news01/658401/testing-finds-contaminated-wells-near-grand-rapids-area-airport', 'field--name-field-paragraph-body', True))
#3
articleObjs.append(articleClass('https://www.crainsdetroit.com/article/20180403/news01/656966/synthetic-coolant-leaks-from-power-cables-in-michigan-waters', 'field--name-field-paragraph-body', True))
#4
articleObjs.append(articleClass('https://www.dailytribune.com/news/concerns-grow-over-tainted-sewage-sludge-spread-on-lapeer-croplands/article_6c8bc1a6-a71c-5775-a3b9-f6db18248d26.html', 'asset-content', True))
#5
articleObjs.append(articleClass('http://www.pressandguide.com/news/tlaib-statement-on-revere-copper-site-collapse-into-detroit-river/article_c1ef5fa8-1a0e-11ea-a18b-3b3e5b366236.html', 'asset-content', True))
#6
articleObjs.append(articleClass('https://www.candgnews.com/news/officials-search-for-petroleum-leak-source-into-clinton-river-116417', 'article-body-text', True))
#7
articleObjs.append(articleClass('https://www.lansingstatejournal.com/story/news/2019/10/14/11-million-gallons-sewage-water-dumped-grand-red-cedar-river/3975129002/', 'asset-double-wide', True))
#8
articleObjs.append(articleClass('https://www.lansingstatejournal.com/story/news/local/2019/04/22/racer-trust-proposes-fix-dioxane-pollution-lansing-township-gm-water-quality/3330212002/', 'asset-double-wide', True))
#9
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2019/03/contamination-plume-leaves-manufacturing-property-in-kalamazoo-township.html', 'entry-content', True))
#10
articleObjs.append(articleClass('https://www.mlive.com/news/detroit/2018/10/detroit_schools_to_spend_38_mi.html', 'entry-content', True))
#11
articleObjs.append(articleClass('https://www.mlive.com/news/2019/03/toxic-pollution-at-wolverine-tannery-is-extensive-data-confirms.html', 'entry-content', True))
#12
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2019/08/coal-ash-from-west-michigan-power-plant-might-be-contaminating-drinking-water-wells.html', 'entry-content', True))
#13
articleObjs.append(articleClass('https://www.candgnews.com/news/officials-investigate-plumbrook-drain-oil-report--111626', 'article-body-text', True))
#14
articleObjs.append(articleClass('https://www.candgnews.com/news/royal-oak-warns-residents-of-action-level-lead-in-water-115688', 'article-body-text', True))
#15
articleObjs.append(articleClass('https://www.mininggazette.com/news/2019/08/mass-city-mercury-spill-contained/', 'article', True))
#16
articleObjs.append(articleClass('https://www.freep.com/story/news/local/michigan/oakland/2020/01/10/madison-heights-green-ooze-slime-pfas/4437379002/', 'asset-double-wide', True))
#17
articleObjs.append(articleClass('https://www.freep.com/story/news/local/michigan/2017/03/24/mercury-rising-scientists-puzzled-metals-jump-great-lakes-fish/99306786/', 'asset-double-wide', True))
#18
articleObjs.append(articleClass('https://www.petoskeynews.com/news/community/michigan-says-soybeans-must-be-destroyed-due-to-soil/article_c9afc10b-2dc2-5c2b-97d5-26b55d8bf933.html', 'asset-content', True))
#19
articleObjs.append(articleClass('https://www.petoskeynews.com/charlevoix/black/toxic-land-one-family-s-story/article_0e18578b-66fa-56ff-9f4b-77666799cab1.html', 'asset-content', True))
#20
articleObjs.append(articleClass('https://www.petoskeynews.com/ap/state/cleanup-of-contaminated-site-is-expected-to-cost-millions/article_9d317aec-edf6-59ee-b35d-1351e5876012.html', 'asset-content', True))
#21
articleObjs.append(articleClass('https://www.petoskeynews.com/featured-pnr/leak-reported-from-wastewater-pump-station-line-in-harbor-springs/article_c15ca4d0-6cdf-5dc6-ac94-ab259e9a2d77.html', 'asset-content', True))
#22
articleObjs.append(articleClass('https://www.petoskeynews.com/gaylord/news/local/crews-clean-up-fuel-oil-spill-along-walloon-lake-shore/article_ec93ee17-73f6-5461-911a-45164fc0ed79.html', 'asset-content', True))
#23
articleObjs.append(articleClass('https://www.petoskeynews.com/news/state-region/michigan-sues-m-dupont-over-forever-chemicals-in-water/article_5a3d491d-45cf-5876-b216-2d6417a0a63c.html', 'asset-content', True))
#24
#articleObjs.append(articleClass('https://michiganchronicle.com/2018/04/03/pollution-and-southwest-detroit/', 'entry-content', True))
#25
articleObjs.append(articleClass('https://www.mlive.com/news/ann-arbor/2020/01/sewer-line-break-leaks-50-gallons-in-augusta-township.html', 'entry-content', True))
#26
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2019/10/hazmat-crew-called-to-nitrogen-tank-leak-near-ford-airport-roads-blocked.html', 'entry-content', True))
#27
articleObjs.append(articleClass('https://www.mlive.com/news/muskegon/2019/09/edgewood-elementary-in-muskegon-heights-evacuated-due-to-gas-leak-in-roadway.html', 'entry-content', True))
#28
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2019/09/city-inspecting-pipes-under-kalamazoo-after-two-sewage-leaks-into-river.html', 'entry-content', True))
#29
articleObjs.append(articleClass('https://www.mlive.com/news/flint/2019/08/buick-city-site-will-close-sewer-that-leaks-pfas-into-the-flint-river.html', 'entry-content', True))
#30
articleObjs.append(articleClass('https://www.mlive.com/news/flint/2019/05/crews-work-to-repair-lapeer-sewer-line-gas-leak.html', 'entry-content', True))
#31
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2019/06/two-people-treated-at-hospital-after-barrel-leaks-chemical-fumes-blow-toward-business.html', 'entry-content', True))
#32
articleObjs.append(articleClass('https://www.mlive.com/news/muskegon/2020/01/estimated-132000-gallons-of-untreated-sewage-spill-after-pipe-break-near-muskegon.html', 'entry-content', True))
#33
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2018/10/no_threat_to_public_after_leak.html', 'entry-content', True))
#34
articleObjs.append(articleClass('https://www.mlive.com/news/saginaw/2018/09/chemical_leak_at_semiconductor.html', 'entry-content', True))
#35
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2014/03/up_to_755_gallons_of_crude_oil.html', 'entry-content', True))
#36
articleObjs.append(articleClass('https://www.mlive.com/news/2019/09/110k-fine-levied-for-downtown-grand-rapids-air-pollution.html', 'entry-content', True))
#37
articleObjs.append(articleClass('https://www.record-eagle.com/state/superfund-cleanup-considered-for-detroit-green-goo-site/article_428248df-1ac8-5063-8ce0-02a4c1cf4481.html', 'asset-content', True))
#38
articleObjs.append(articleClass('https://www.mibiz.com/sections/manufacturing/state-continues-air-pollution-probe-at-grand-rapids-medical-sterilizer?highlight=WyJwb2xsdXRpb24iXQ==', 'pigeon-first-p', True))
#39
articleObjs.append(articleClass('https://www.mlive.com/news/kalamazoo/2020/01/pfas-found-at-former-portage-landfill-nearby-private-wells-being-tested.html', 'entry-content', True))
#40
articleObjs.append(articleClass('https://www.mlive.com/news/2019/05/toxic-piles-of-mystery-foam-near-detroit-was-pfas-but-from-where.html', 'entry-content', True))
#41
articleObjs.append(articleClass('https://www.mlive.com/news/ann-arbor/2020/01/pfas-found-in-ann-arbor-compost-thats-used-as-fertilizer-park-soil.html', 'entry-content', True))
#42
articleObjs.append(articleClass('https://www.lansingstatejournal.com/story/news/2019/12/03/lead-water-lansing-school-district-everett-high-school/2594569001/', 'asset-double-wide', True))
#43
articleObjs.append(articleClass('https://www.mlive.com/news/2018/10/more_pfas_contamination_found.html', 'entry-content', True))
#44
articleObjs.append(articleClass('https://www.mlive.com/news/2017/09/wolverine_beltline_landfill_pf.html', 'entry-content', True))
#45
articleObjs.append(articleClass('https://huroncountyview.mihomepaper.com/articles/fire-agencies-spend-12-hours-containing-spill-after-100-gallons-of-fuel-drain-into-lake/', 'entry-content', True))
#46
articleObjs.append(articleClass('https://huroncountyview.mihomepaper.com/articles/miller-st-clair-river-spill-shows-need-for-real-time-water-monitoring/', 'entry-content', True))
#47
articleObjs.append(articleClass('https://www.cadillacnews.com/news/local/chemical-spill-at-yoplait-evacuates-downtown/article_7429336c-34fc-55d0-861f-e13f0426f699.html', 'asset-content', True))
#48
articleObjs.append(articleClass('https://www.cadillacnews.com/news/gallons-of-wastewater-spill-into-hersey-river/article_e5748350-24aa-51cf-a7c7-5494d5d4ccbd.html', 'asset-content', True))
#49
articleObjs.append(articleClass('https://www.leaderpub.com/2012/03/07/mercury-spill-locks-down-school/', 'story_detail', True))
#50
articleObjs.append(articleClass('https://www.battlecreekenquirer.com/story/news/local/2019/12/24/enbridge-leak-oil-kalamazoo-river-2010-spill/2741783001/', 'asset-double-wide', True))

#NEGATIVES (clear/unambiguous)
#1
articleObjs.append(articleClass('https://www.dailytribune.com/news/local/royal-oak-manor-works-with-city-to-ease-senior-parking/article_28c0dd38-439a-11ea-bf32-679e16d6156e.html', 'asset-content', False))
#2
articleObjs.append(articleClass('https://www.dailytribune.com/news/fatal-crashes-involving-drivers-who-test-positive-for-marijuana-have/article_50fc0af8-c027-5d07-a4ca-bbc9c7eeea7e.html', 'asset-content', False))
#3
articleObjs.append(articleClass('https://www.dailytribune.com/news/copscourts/fbi-arrests-for-string-of-taco-bell-armed-robberies/article_3312efbf-a7f4-5b42-bb9e-0374f7a04685.html', 'asset-content', False))
#4
articleObjs.append(articleClass('https://www.dailytribune.com/lifestyles/health/first-case-of-person-to-person-spread-of-coronavirus-reported/article_c3c33e09-d8fe-5a95-a3ff-d1ddebf1cdd1.html', 'asset-content', False))
#5
articleObjs.append(articleClass('https://www.mlive.com/news/ann-arbor/2020/01/troopers-dressed-as-star-wars-stormtroopers-take-polar-plunge-for-special-olympics.html', 'entry-content', False))
#6
articleObjs.append(articleClass('https://www.freep.com/story/sports/mlb/tigers/2020/01/30/detroit-tigers-shortstop-jordy-mercer-return/2857336001/', 'asset-double-wide', False))
#7
articleObjs.append(articleClass('https://www.freep.com/story/news/2020/01/30/175-eateries-cited-priority-violations-december/4501118002/', 'asset-double-wide', False))
#8
articleObjs.append(articleClass('https://www.freep.com/story/news/local/michigan/oakland/2020/01/30/motorist-drives-into-concrete-slab-near-8-mile/2856904001/', 'asset-double-wide', False))
#9
articleObjs.append(articleClass('https://www.freep.com/story/sports/nfl/lions/2020/01/30/tua-tagovailoa-2020-nfl-draft-leigh-steinberg-detroit-lions/2854162001/', 'asset-double-wide', False))
#10
articleObjs.append(articleClass('https://www.freep.com/story/news/local/michigan/detroit/2020/01/30/moses-champion-fbi-fast-food-robber-busted-after-terrorizing-suburbs-and-taco-bell/2855508001/', 'asset-double-wide', False))
#11
#articleObjs.append(articleClass('https://www.candgnews.com/news/why-regular-baths-are-important-pet-health-94126', 'asset-double-wide', False))
#12
articleObjs.append(articleClass('https://www.mlive.com/news/2020/01/michigan-based-lipari-foods-recalls-sandwiches-over-listeria-contamination-concerns.html', 'entry-content', False))
#13
articleObjs.append(articleClass('https://www.mlive.com/news/flint/2019/10/conference-in-flint-discusses-how-water-contamination-affects-affordability.html', 'entry-content', False))
#14
articleObjs.append(articleClass('https://www.mlive.com/news/2019/10/michigan-apples-recalled-for-possible-listeria-contamination.html', 'entry-content', False))
#15
articleObjs.append(articleClass('https://www.mlive.com/news/2019/09/gold-medal-flour-recalled-over-possible-ecoli-contamination.html', 'entry-content', False))
#16
articleObjs.append(articleClass('https://www.mlive.com/news/2019/06/frozen-berries-sold-at-kroger-recalled-for-potential-hepatitis-contamination.html', 'entry-content', False))
#17
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2019/04/cost-pollution-raise-concern-at-meeting-on-proposed-grand-rapids-to-lakeshore-powerboat-link.html', 'entry-content', False))
#18
articleObjs.append(articleClass('https://www.mlive.com/news/grand-rapids/2012/06/pete_hoekstra_intelligence_lea.html', 'entry-content', False))
#19
articleObjs.append(articleClass('https://www.mlive.com/wolverines/2019/03/espn-womens-bracket-leak-spoils-surprise-for-michigan.html', 'entry-content', False))
#20
articleObjs.append(articleClass('https://www.candgnews.com/news/noise-pollution-health-issue-84629', 'article-body-text', False))
#21
articleObjs.append(articleClass('https://www.candgnews.com/news/be-part-of-the-pollution-solution--114274', 'article-body-text', False))
#22
articleObjs.append(articleClass('https://www.candgnews.com/news/when-lights-go-down-show-begins-100688', 'article-body-text', False))
#23
articleObjs.append(articleClass('https://www.candgnews.com/news/huntington-woods-begin-work-library-roof-fiscal-year-95801', 'article-body-text', False))
#24
articleObjs.append(articleClass('https://www.candgnews.com/news/void-found-on-15-mile-road-near-sinkhole-location-111982', 'article-body-text', False))
#25
articleObjs.append(articleClass('https://www.candgnews.com/news/truck-spill-causes-backups-on-telegraph-114461', 'article-body-text', False))
#26
articleObjs.append(articleClass('https://www.candgnews.com/news/man-dies-in-quadruple-stabbing-in-eastpointe-111458', 'article-body-text', False))
#27
articleObjs.append(articleClass('https://www.thesouthend.wayne.edu/article_074a3404-43c9-11ea-b554-e32171d0da0f.html', 'asset-content', False))
#28
articleObjs.append(articleClass('https://www.thenewsherald.com/opinion/impeachment-outcome-could-alter-our-form-of-government/article_2710c7ce-41d7-11ea-b318-af4fef4fd33d.html', 'asset-content', False))
#29
articleObjs.append(articleClass('https://www.candgnews.com/news/fired-financial-services-director-files-whistleblower-lawsuit-against-city-116732', 'article-body-text', False))
#30
articleObjs.append(articleClass('https://www.candgnews.com/news/athens-gradappears-in-broadway-tour-of-charlie-and-the-chocolate-factory-116731', 'article-body-text', False))
#31
articleObjs.append(articleClass('https://www.candgnews.com/news/jazz-singer-to-pay-tribute-to-tony-bennett-at-troy-library-116730', 'article-body-text', False))
#32
articleObjs.append(articleClass('https://www.candgnews.com/news/incinerator-failure-sparks-fire-at-industrial-equipment-supplier-in-troy-116729', 'article-body-text', False))
#33
articleObjs.append(articleClass('https://www.candgnews.com/news/remembering-super-sunday-116710', 'article-body-text', False))
#34
articleObjs.append(articleClass('https://www.candgnews.com/news/another-day-at-the-pawffice-116709', 'article-body-text', False))
#35
articleObjs.append(articleClass('https://www.candgnews.com/news/commission-moves-up-public-comments-at-meetings-116677', 'article-body-text', False))
#36
articleObjs.append(articleClass('https://www.candgnews.com/news/economists-wary-but-hopeful-for-michigan-in-2020-116676', 'article-body-text', False))
#37
articleObjs.append(articleClass('https://www.candgnews.com/news/scholarship-minigrant-opportunities-available-116658', 'article-body-text', False))
#38
articleObjs.append(articleClass('https://www.candgnews.com/news/beaumont-researchers-discover-key-biomarkers-for-predicting-autism-in-newborns-116619', 'article-body-text', False))
#39
articleObjs.append(articleClass('https://www.thenewsherald.com/news/state/thousands-without-power-after-tuesday-s-storms/article_ab263323-46d2-53b9-b998-899b307839fe.html', 'asset-content', False))
#40
articleObjs.append(articleClass('https://www.thenewsherald.com/news/items-found-on-allen-park-banquet-hall-roof-related-to/article_a8498c96-41ef-11ea-b603-2b5f625d0201.html', 'asset-content', False))
#41
articleObjs.append(articleClass('https://www.thenewsherald.com/downriver_life/tech-company-releases-list-of-most-commonly-used-passwords/article_b4b039af-2844-589c-8771-bc4e77c3db7f.html', 'asset-content', False))
#42
articleObjs.append(articleClass('https://www.thenewsherald.com/news/employees-spill-beans-on-wahlburgers-restaurant-moving-out-of-taylor/article_f62404f4-30f2-11ea-b447-cfba450ee089.html', 'asset-content', False))
#43
articleObjs.append(articleClass('https://www.thenewsherald.com/news/third-time-drunken-driving-suspect-arrested-in-wyandotte-after-swerving/article_d6125844-e919-11e9-95ad-47abb153db52.html', 'asset-content', False))
#44
articleObjs.append(articleClass('https://www.thenewsherald.com/news/police-investigating-who-robbed-grieving-family-after-husband-family-pets/article_e6c403ec-ed68-11e9-beec-7b59464dcf04.html', 'asset-content', False))
#45
articleObjs.append(articleClass('https://www.wxyz.com/news/region/oakland-county/oakland-county-deputies-search-hines-park-for-gun-used-in-armed-robberies', 'RichTextArticleBody-body', False))
#46
articleObjs.append(articleClass('https://www.wxyz.com/news/suspect-arrested-in-connection-to-armed-robberies-at-metro-detroit-fast-food-locations', 'RichTextArticleBody-body', False))
#47
articleObjs.append(articleClass('https://www.wxyz.com/news/farmington-hills-police-names-jeff-king-as-new-chief', 'RichTextArticleBody-body', False))
#48
articleObjs.append(articleClass('https://www.wxyz.com/getting-around-metro-detroit/michigan-senate-votes-to-require-study-of-highway-tolls', 'RichTextArticleBody-body', False))
#49
articleObjs.append(articleClass('https://www.clickondetroit.com/news/local/2019/12/19/police-respond-to-bloomfield-hills-high-school-after-apparent-false-alarm/', 'articleBody', False))
#50
articleObjs.append(articleClass('https://www.dailytribune.com/news/anti-impeachment-rally-planned-in-bloomfield-hills/article_20d0e42e-687f-5660-9051-582092cd858f.html', 'asset-content', False))

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
    














