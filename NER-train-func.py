import spacy
import random
from spacy.util import minibatch, compounding
import nlp-spacy

#TODO ----->>>> IMPORT THE CRAWLER FILE


def trainModel(nerM, trainingD, o, l={}):
    random.shuffle(trainingD)
    bRes = minibatch(trainingD, compounding(1., 10., 1.001)) #TODO CHANGE THESE VALUES
        #compounding -> start, end, multiply current value by this until it reaches the end
    for b in bRes:
        for t, a in trainingD:
            nerM.update([t], [a], o, .2, l=losses)
    print(l)

    #return nerM -- only needed if the update is considered a local change to the model and is not given to the global model
#______________________________________________________

def runModelonSent(tS, nModel):
    results = []
    for sent in tS:
        resultNER = nModel(sent)
        print(sent)
        sentNER = []
        for NER in resultNER.ents:
            #print(NER.text, NER.label_)
            sentNER.append(NER)
        results.append(sentNER)
    return results
#returns a 2Dim array, each sent is 1 dim, each of those has an array of each NER and the label
#______________________________________________________________

#INITIALIZATION
initialRun = True
#take training data from the external file
td = []
try:
    nerModel = spacy.load("NER-model-test")
    initialRun=False
except:
    nerModel = spacy.blank("en")  # create blank Language class
    initialRun=True

ENT1 = "SUBLOC"
ENT2 = "BODWAT"
ENT3 = "CHEM"
ENT4 = "TITLE"
ENT5 = "UNIT"

newLabels = []
newLabels.append(ENT1)
newLabels.append(ENT2)
newLabels.append(ENT3)
newLabels.append(ENT4)
newLabels.append(ENT5)


#START THE TESTING SETUP________________________________________
found = False
if not nerModel.pipe_names:
    for pipe in nerModel.pipe_names:
        if(pipe=='ner'):
            NERpipe = nerModel.get_pipe("ner")
            found = True
            break
if(found==False):
    NERpipe = nerModel.create_pipe('ner')
    print("Created NER pipe")
    nerModel.add_pipe(NERpipe, last=True) 

for new in newLabels:
    NERpipe.add_label(new)

for p in nerModel.pipe_names:
    if p!='ner':
        nerModel.disable_pipes(p)

if initialRun==True:
    opt = nerModel.begin_training()
else:
    opt = nerModel.resume_training()
#END TRAINING SETUP _____________________________________________



##CHANGE THIS FILE:
    #GET SCRAPED OBJECT FROM SAULAR'S .py SCRIPT
    #EXTRACT THE TEXT, hand it to the tokenizing function
#get scraped object ______________________________________________
crawler = FreepCrawler("pollution", "contamination")
crawler.crawlURLs()
crawler.scrapeURLs()

#_________________________________________________________________
#RIGHT NOW WE RETRAIN FOR EVERY ARTICLE
#TODO ---->>>> TEST WITH ONLY TRAINING ONCE FOR ALL ARTICLES
nerResults = []
for article in crawler.getScrapedArticles():
    #call tokenizing function from nlp-spacy.py
    tokenizedSent = nlp-spacy.convertScrapedtoSent(article)
    for i in range(0, 25):
        trainModel(nerModel,td,opt)
    ##TODO: determine if the update stays in the model without an assignment?
    #if we do an assign, does it overwrite previous updates to the model??
    #pass by reference??
    nerResults = runModelonSent(tokenizedSent, nerModel)
    for sent in nerResults:
        for NER in sent:
            print(NER.text, NER.label_)
    
        


#nerModel.to_disk("NER-model-test")


