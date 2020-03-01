def cleanOutputFile():
    badfile = open("recordtest.txt", "r", errors="ignore")
    goodfile = open("goodeval.txt", "w", errors = "ignore")

    line = badfile.readline()
    while(line):
        if(line=="\n" or "," in line):
            line = badfile.readline()
            continue
        else:
            goodfile.write(line)
            line = badfile.readline()
    badfile.close()
    goodfile.close()

def matchingTags(sentNum, fullSent):
    origCSV = open("csv-file.csv", "r", errors="ignore")
    line = origCSV.readline()
    numCorr = 0
    numTotal = 0
    while(line):
        if(str(sentNum) in line):
            i = 0
            noCommas = line.split(',')
            tag = noCommas[3]
            if(len(fullSent)!=0 and fullSent[i]==tag):
                numCorr +=1
                numTotal+=1
                i+=1
            else:
                numTotal+=1
                i+=1
            line = origCSV.readline()
            while(line[0]==','):
                line = origCSV.readline()
                noCommas = line.split(',')
                tag = noCommas[3]
                if(len(fullSent)!=0 and fullSent[i]==tag):
                    numCorr +=1
                    numTotal+=1
                    i+=1
                else:
                    numTotal+=1
                    i+=1
            
            return numCorr, numTotal
        else:
            line = origCSV.readline()
        
        


    #return number correct, number total (not including O)

def evalAccuracy():
    goodfile = open("goodeval.txt", "r", errors = "ignore")


    line = goodfile.readline()
    numCorrect = 0
    numTotal = 0
    while(line):
        splits = ""
        num = 1
        if(line!=""):
            splits = line.split(" ")
        if("Sentence" in line):
            res = line.split(" ")
            num = int(res[1])
            line = goodfile.readline()
            tags = []
            while("Sentence" not in line):
                noCol = line.split(":")
                noSp = noCol[1].split(" ")
                
                if noSp:
                    print(noSp[1][:-1])
                    tags.append(noSp[1][:-1])
                line = goodfile.readline()
            print("FINISHED SENTENCE "+str(num))
            #print(tags)
            numCorr, numTot = matchingTags(num, tags)
            numCorrect+=numCorr
            numTotal+=numTot
            
        else:
            line = goodfile.readline()

    print("ACCURACY: "+str(numCorrect/numTotal))
            
def removeBadTags():
    test = open("testing.txt", "r", errors = "ignore")
    test2 = open('test2.txt', 'w', errors='ignore')
    line = test.readline()
    while(line):
        if(line!='\n' and 'DOC' not in line and "B-" not in line and "I-" not in line):
            splits = line.split(" ")
            if '' in splits:
                splits.remove('')
            temp = splits[0]
            for s in splits[1:]:
                temp+=' '
                temp+=s
            line = temp

            if line[0]==' ':
                while line[0]==' ':
                    line = line[1:]
            line = line[:-3]+"O\n"
            test2.write(line)
        elif line=='\n':
            test2.write(line)
        elif line[len(line)-1]=='\n':
            if line[len(line)-2]==' ':
                line = line[:len(line)-2]+'\n'
            test2.write(line)
        line = test.readline()
    test.close()
    test2.close()

def eval2Files():
    tCSV = open("testing.csv", "r", errors="ignore")
    goodfile = open("goodeval.txt", "w", errors = "ignore")

    orig = tCSV.readline()
    pred = goodfile.readline()
    numTotal = 0
    numCorrect = 0
    while orig and pred:
        if "Sentence" in orig and "Sentence" in pred:
            orig = tCSV.readline()
            pred = goodfile.readline()
        else:
            origsplit = orig.split(',')
            predsplit = pred.split(' ')
            if(origsplit[3]!='O'):
                numTotal+=1
                if(predsplit[3]==origsplit[3]):
                    numCorrect+=1
        
        orig = tCSV.readline()
        pred = goodfile.readline()
    


#removeBadTags()
cleanOutputFile()
#evalAccuracy()
#eval2Files()






