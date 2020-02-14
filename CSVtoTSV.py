
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

def CSVConvert():
    file = open("AustinCSVtest.csv",'r',encoding='cp437')
    newfile = open("austin-tsv.txt","w",encoding='cp437')
    line = file.readline()
    sent = []
    POS = []
    tags = []
    position = []
    while line:
        if("Sentence" in line):
            #fill POS with the pos of each
            fullSent = ""
            for word in sent:
                fullSent = fullSent+" "+word
            #print(fullSent)
            NLPtxt = nlp(fullSent)
            for eachWord in NLPtxt:
                POS.append(eachWord.tag_)
            #write current sentence to file with POS and tags (send 3 lists)
            for i in range(len(sent)):
                print(""+sent[i].upper()+" "+POS[i]+" "+position[i]+" "+tags[i]+"\n")
                newfile.write(""+sent[i].upper()+" "+POS[i]+" "+position[i]+" "+tags[i]+"\n")
            print("\n")
            newfile.write("\n")
            sent = []
            POS = []
            tags = []
            position = []
        
        commaOut = line.split(',')
        sent.append(commaOut[1])
        tags.append(commaOut[-2])
        if(commaOut[-2]!=''):
            position.append(commaOut[-2][0])
        else:
            position.append('O')
        line = file.readline()

    file.close()
    newfile.close()



CSVConvert()
