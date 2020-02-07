
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

pollPats.append([{"LEMMA": {"IN": ["toxic","cleanup","hazmat"]}}])
pollPats.append([{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}}])
pollPats.append([{"LEMMA": {"IN": ["cause","source"]}},{"LEMMA": {"IN": ["unknown","pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}}])
pollPats.append([{"POS":"NOUN","OP":"?"},{"LEMMA": {"IN": ["superfund"]}},{"POS":"NOUN","OP":"?"}])
#pollPats.append([{"LEMMA": {"IN": ["official"]}},{"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued"]},"OP":"?"}]) #lemmatized words (said/discussed/etc.)

pollPats.append([{"POS": "NOUN"},{"LEMMA": {"IN": ["levels","contamination"]}}])
pollPats.append([{"POS": "NOUN"},{"LEMMA": {"IN": ["pollute", "contaminate", "dump", "pour","discard","spill", "leak", "taint", "bleed", "plume"]}}])
pollPats.append([{"LEMMA": {"IN": ["detected", "discovered", "found"]}},{"POS":"ADJ","OP":"*"},{"LEMMA": {"IN": ["substance", "chemical", "level"]}}, {"POS": "NOUN","OP":"?"}])
pollPats.append([{"POS":"ADJ"},{"LEMMA": {"IN": ["chemical"]}},{"POS":"NOUN","OP":"?"}])
pollPats.append([{"POS":"ADJ","OP":"?"},{"LEMMA": {"IN": ["chemical"]}},{"POS":"NOUN"}])
pollPats.append([{"POS": "NUM"},{"LEMMA": {"IN": ["gallon", "ppt", "ppb", "ton"]}}])

negP = Matcher(nlp.vocab)
negPats = []
#TO IDENTIFY NEGATIVES
#identifying lawsuit/sue
negPats.append([{"POS":"NOUN","OP":"?"},{"LEMMA": {"IN": ["legislation","lawsuit","sue","charge"]}},{"POS":"NOUN","OP":"?"}])
# op verb + automobile, car, vehicle, motor
negPats.append([{"POS":"VERB","OP":"?"},{"LEMMA": {"IN": ["noise","automobile","car","vehicle"]}}])
# op noun + automobile, car, vehicle, motor + op verb
negPats.append([{"POS":"NOUN","OP":"?"},{"LEMMA": {"IN": ["automobile","car","vehicle"]}},{"POS":"VERB","OP":"?"}])
# op verb + championship, game, tournament, competition
negPats.append([{"POS":"VERB","OP":"?"},{"LEMMA": {"IN": ["sport","basketball","championship","game","tournament","competition"]}}])
# op verb + fruit, meal, produce, meat + op adverb
negPats.append([{"POS":"VERB","OP":"?"},{"LEMMA": {"IN": ["recall","fruit","meal","meat"]}},{"POS":"ADV","OP":"?"}])
# op noun + fruit, meal, produce, meat + op adverb
negPats.append([{"POS":"NOUN","OP":"?"},{"LEMMA": {"IN": ["fruit","meal","meat"]}},{"POS":"ADV","OP":"?"}])
# op verb + application, password, technology + op verb
negPats.append([{"POS":"VERB","OP":"?"},{"LEMMA": {"IN": ["application","password","technology"]}},{"POS":"VERB","OP":"?"}])
# op verb + theater, performance, venue + op verb
negPats.append([{"POS":"VERB","OP":"?"},{"LEMMA": {"IN": ["theater","performance","venue"]}},{"POS":"VERB","OP":"?"}])
# op verb + theater, performance, venue + op noun
negPats.append([{"POS":"VERB","OP":"?"},{"LEMMA": {"IN": ["theater","performance","venue"]}},{"POS":"NOUN","OP":"?"}])

i=0
for pat in pollPats:
    pPt.add("pat"+str(i),None,pat)
    i=i+1

i=0
for pat in negPats:
    negP.add("neg"+str(i),None,pat)
    i=i+1


#article class
class articleClass:
    def __init__(self, title,  isEvent):
        self.title = title
        self.event = isEvent

    def getText(self):
        return self.title
    def isEvent(self):
        return self.event

def isArticleEvent(title):
    nER = nlp(title.getText())
    negInSent = negP(nER)
    matchesInSent = pPt(nER)
    if negInSent:
        return False
    if matchesInSent:
        return True
    return False


titles = []
titles.append(articleClass("Toxic chemicals found in New Baltimore, Mount Clemens, Ira Township drinking water",True))
titles.append(articleClass("Testing finds contaminated wells near Grand Rapids-area airport",True))
titles.append(articleClass("Synthetic coolant leaks from power cables in Michigan waters",True))
titles.append(articleClass("Concerns grow over tainted sewage sludge spread on Lapeer croplands",True))
titles.append(articleClass("Tlaib statement on Revere Copper site collapse into Detroit River",True))
titles.append(articleClass("Officials search for source of petroleum leak into relief drain, Clinton River",True))
titles.append(articleClass("38 million gallons of sewage, storm water spilled into Grand and Red Cedar rivers this month",True))
titles.append(articleClass("RACER Trust proposes fix for dioxane pollution in Lansing Township",True))
titles.append(articleClass("Contamination plume leaves manufacturing property in Kalamazoo Township",True))
titles.append(articleClass("Detroit schools to spend $3.8 million correcting water contamination issues",True))
titles.append(articleClass("Toxic pollution at Wolverine tannery is extensive, new report shows",True))
titles.append(articleClass("Coal ash from West Michigan power plant might be contaminating drinking water wells",True))
titles.append(articleClass("Officials investigate Plumbrook Drain oil report",True))
titles.append(articleClass("Royal Oak warns residents of 'action level' lead in water",True))
titles.append(articleClass("Mass City mercury spill contained",True))
titles.append(articleClass("Green ooze case worsens as PFAS shown in water at site",True))
titles.append(articleClass("Odd mercury spike found in Great Lakes fish",True))
titles.append(articleClass("Michigan says soybeans must be destroyed due to soil",True))
titles.append(articleClass("Toxic land: one family's story",True))
titles.append(articleClass("Cleanup of contaminated site is expected to cost millions",True))
titles.append(articleClass("Leak reported from wastewater pump station line in Harbor Springs",True))
titles.append(articleClass("Crews clean up fuel oil spill along Walloon Lake shore",True))
titles.append(articleClass("Michigan sues 3M, DuPont over 'forever' chemicals in water",True))
titles.append(articleClass("Pollution and southwest Detroit",True))
titles.append(articleClass("Sewer line break leaks 50 gallons in Augusta Township",True))
titles.append(articleClass("Hazmat crew called to nitrogen tank leak near Ford Airport, roads blocked",True))
titles.append(articleClass("Edgewood Elementary in Muskegon Heights evacuated due to gas leak in roadway",True))
titles.append(articleClass("City inspecting pipes under Kalamazoo after two sewage leaks into river",True))
titles.append(articleClass("Buick City site will close sewer that leaks PFAS into the Flint River",True))
titles.append(articleClass("Crews work to repair Lapeer sewer line gas leak",True))
titles.append(articleClass("Two treated at hospital after barrel leaks chemical, fumes spread",True))
titles.append(articleClass("Estimated 132,000 gallons of untreated sewage spill after pipe break near Muskegon",True))
titles.append(articleClass("No threat to public after leak at Palisades nuclear plant",True))
titles.append(articleClass("Chemical leak contained at Hemlock Semiconductor Operations",True))
titles.append(articleClass("Up to 755 gallons of crude oil spilled into Lake Michigan from BP refinery, Coast Guard says",True))
titles.append(articleClass("$110K fine levied for downtown Grand Rapids air pollution",True))
titles.append(articleClass("Superfund cleanup considered for Detroit 'green goo' site",True))
titles.append(articleClass("State continues air pollution probe at Grand Rapids medical sterilizer",True))
titles.append(articleClass("PFAS found at former Portage landfill, nearby private wells being tested",True))
titles.append(articleClass("Toxic stream of ‘mystery foam’ near Detroit was PFAS – but from where?",True))
titles.append(articleClass("PFAS found in Ann Arbor compost that’s used as fertilizer, park soil",True))
titles.append(articleClass("High lead levels found in 3 Everett High School water fountains",True))
titles.append(articleClass("'Pretty high' new PFAS contamination found at closed Buick City site in Flint",True))
titles.append(articleClass("Tannery waste dumped at landfill tied to municipal water pollution",True))
titles.append(articleClass("Fire agencies spend 12 hours containing spill after 100 gallons of fuel drain into lake",True))
titles.append(articleClass("Miller: St. Clair River spill shows need for real-time water monitoring",True))
titles.append(articleClass("Chemical Spill at Yoplait Evacuates Downtown ",True))
titles.append(articleClass("1,000 gallons of wastewater spill into Hersey River",True))
titles.append(articleClass("Mercury spill locks down school",True))
titles.append(articleClass("Leak spews oil into Kalamazoo River",True))



titles.append(articleClass("Royal Oak Manor works with city to ease senior parking problem",False))
titles.append(articleClass("Fatal crashes involving drivers who test positive for marijuana have doubled in states where recreational use is legal, report says",False))
titles.append(articleClass("FBI arrests 2 for string of Taco Bell armed robberies",False))
titles.append(articleClass("First case of person-to-person spread of coronavirus reported in US",False))
titles.append(articleClass("Troopers dressed as Star Wars stormtroopers take polar plunge for Special Olympics",False))
titles.append(articleClass("Detroit Tigers bring back shortstop Jordy Mercer on minor-league deal",False))
titles.append(articleClass("175 eateries cited for priority violations in December",False))
titles.append(articleClass("Motorist drives into concrete slab near 8 Mile in Southfield",False))
titles.append(articleClass("Perfect fit for Detroit Lions? Draft Tua Tagovailoa, sit him in 2020",False))
titles.append(articleClass("FBI: Fast food robber busted after terrorizing suburbs and Taco Bell",False))
titles.append(articleClass("Why regular baths are important for pet health",False))
titles.append(articleClass("Michigan-based Lipari Foods recalls sandwiches over Listeria contamination concerns",False))
titles.append(articleClass("Conference in Flint discusses how water contamination affects affordability",False))
titles.append(articleClass("Michigan apples recalled for possible listeria contamination",False))
titles.append(articleClass("Gold Medal flour recalled over possible E.coli contamination",False))
titles.append(articleClass("Frozen berries sold at Kroger recalled for potential Hepatitis contamination",False))
titles.append(articleClass("Cost, pollution raise concern at meeting on proposed Grand Rapids to lakeshore powerboat link",False))
titles.append(articleClass("Pete Hoekstra: Intelligence leak watchdog or serial secret sharer?",False))
titles.append(articleClass("ESPN women’s bracket leak spoils surprise for Michigan",False))
titles.append(articleClass("Noise pollution is a health issue",False))
titles.append(articleClass("Be part of the pollution solution",False))
titles.append(articleClass("When the lights go down, the show begins",False))
titles.append(articleClass("Huntington Woods to begin work on library roof this fiscal year",False))
titles.append(articleClass("'Void' found on 15 Mile Road near sinkhole location",False))
titles.append(articleClass("Truck spill causes backups on Telegraph",False))
titles.append(articleClass("Man dies in quadruple stabbing in Eastpointe",False))
titles.append(articleClass("MDOT wants Second Avenue bridge done by spring 2021",False))
titles.append(articleClass("Impeachment outcome could alter our form of government",False))
titles.append(articleClass("Fired financial services director files whistleblower lawsuit against city",False))
titles.append(articleClass("Athens grad appears in Broadway tour of 'Charlie and the Chocolate Factory'",False))
titles.append(articleClass("Jazz singer to pay tribute to Tony Bennett at Troy library",False))
titles.append(articleClass("Incinerator failure sparks fire at industrial equipment supplier in Troy",False))
titles.append(articleClass("Remembering 'Super' Sunday",False))
titles.append(articleClass("Another day at the 'paw-ffice'",False))
titles.append(articleClass("Commission moves up public comments at meetings",False))
titles.append(articleClass("Economists wary but hopeful for Michigan in 2020",False))
titles.append(articleClass("Scholarship, mini-grant opportunities available",False))
titles.append(articleClass("Beaumont researchers discover key biomarkers for predicting autism in newborns",False))
titles.append(articleClass("Thousands without power after Tuesday's storms",False))
titles.append(articleClass("Items found on Allen Park banquet hall roof related to break-in three months earlier",False))
titles.append(articleClass("Tech company releases list of most commonly used passwords",False))
titles.append(articleClass("Employees spill beans on Wahlburgers restaurant moving out of Taylor and into Woodhaven",False))
titles.append(articleClass("Third-time drunken driving suspect arrested in Wyandotte after swerving, falling off motorcycle",False))
titles.append(articleClass("Police investigating who robbed grieving family after husband, family pets die in Allen Park fire",False))
titles.append(articleClass("Deputies search Hines Park for gun used in armed robberies",False))
titles.append(articleClass("News Suspect arrested in connection to armed robberies at metro Detroit fast food locations ",False))
titles.append(articleClass("News Farmington Hills police names Jeff King as new chief ",False))
titles.append(articleClass("Michigan Senate votes to require study of highway tolls",False))
titles.append(articleClass("Police give all-clear after false alarm at Bloomfield Hills High School",False))
titles.append(articleClass("Anti-impeachment rally planned in Bloomfield Hills",False))



totalNum = len(titles)
numCorrect = 0
n=0
numTP = 0
numTN = 0
numFP = 0
numFN = 0
for title in titles:
    n=n+1
    result = isArticleEvent(title)
    print(""+str(n)+" " + str(result))
    if result==title.isEvent():
        numCorrect = numCorrect+1
        if result==True:
            numTP+=1
        else:
            numTN+=1
    else:
        if result==True:
            numFP+=1
        else:
            numFN+=1
    #determine T/F by function call of rules

#calculate accuracy
accuracy = numCorrect/totalNum
print("FINAL ACCURACY = "+str(accuracy))
print("TRUE pos = "+str(numTP/numCorrect))
print("TRUE neg = "+str(numTN/numCorrect))

print("FALSE pos = "+str(numFP/(totalNum-numCorrect)))
print("FALSE neg = "+str(numFN/(totalNum-numCorrect)))
#num of obj correctly found T/F / num total obj
#num false +, num false -, num true +, num true -








        

