import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

def CSVConvert():
    file = open("testing.txt",'r',encoding='cp437')
    newfile = open("testing.csv","w",encoding='cp437')
    line = file.readline()
    while(line=="\n"):
        line = file.readline() #skip any initial enters
    newfile.write("Sentence #,Word,POS,Tag\n")
    sentNum = 1
    firstLine = True
    while line:
        if("\n" != line and "-DOCSTART-" not in line and "," not in line):
            splits = line.split(" ")
            if(splits[0]=="" or len(splits)<2):
                line = file.readline()
                continue

            if(firstLine == True):
                if len(splits)>=4 and "\n" in line:
                    newfile.write("Sentence: "+str(sentNum)+","+splits[0]+","+splits[1]+","+splits[3]) #word
                elif len(splits)>=4 and "\n" not in line:
                    newfile.write("Sentence: "+str(sentNum)+","+splits[0]+","+splits[1]+","+splits[3]+"\n") #word
                else:
                    newfile.write("Sentence: "+str(sentNum)+","+splits[0]+","+splits[1]+",O\n") #word
                firstLine = False
            else:
                if len(splits)>=4:
                    newfile.write(","+splits[0]+","+splits[1]+","+splits[3]) #word
                elif len(splits)>=4 and "\n" not in line:
                    newfile.write(","+splits[0]+","+splits[1]+","+splits[3]+"\n") #word
                else:
                    newfile.write(","+splits[0]+","+splits[1]+",O\n") #word
        else:
            firstLine = True
            sentNum+=1
        line = file.readline()

    file.close()
    newfile.close()



CSVConvert()
