import spacy
import random
from spacy.util import minibatch, compounding


def trainModel(nerM, trainingD, o, l={}):
    random.shuffle(trainingD)
    bRes = minibatch(trainingD, compounding(1., 10., 1.001)) #TODO CHANGE THESE VALUES
        #compounding -> start, end, multiply current value by this until it reaches the end
    for b in bRes:
        for t, a in trainingD:
            nerM.update([t], [a], o, .2, l=losses)
    print(l)

    #return nerM -- only needed if the update is considered a local change to the model and is not given to the global model




#take training data from the external file
td = []

initialRun = True
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

##for _, annotations in TRAIN_DATA:
##    for ent in annotations.get('entities'):
##        ner.add_label(ent[2])
    
#the above code is doing the same thing as below
for new in newLabels:
    NERpipe.add_label(new)

#nonNERpipes = []
for p in nerModel.pipe_names:
    if p!='ner':
        nerModel.disable_pipes(p)
        #nonNERpipes.append(p)
#DONE ABOVE
#with nerModel.disable_pipes(*nonNERpipes):  # only train NER
if initialRun==True:
    opt = nerModel.begin_training()
else:
    opt = nerModel.resume_training()


for i in range(0, 25):
    trainModel(nerModel,td,opt)
    ##TODO: determine if the update stays in the model without an assignment?
    #if we do an assign, does it overwrite previous updates to the model??
    #pass by reference??
        


#nerModel.to_disk("NER-model-test")

for sent in tokenizedSent:
    resultNER = nerModel(sent)
    print(sent)
    for NER in resultNER.ents:
        print(ent.text, ent.label_)
