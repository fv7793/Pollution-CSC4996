import spacy


initialRun = True
try:
    nerModel = spacy.load("NER-model")
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

##REWRITE <------------------------
#ctrl c
other_pipes = [pipe for pipe in nerModel.pipe_names if pipe != 'ner'] 
with nerModel.disable_pipes(*other_pipes):  # only train NER
    if initialRun==True:
        optimizer = nerModel.begin_training()
    else:
        optimizer = nerModel.resume_training()











        
