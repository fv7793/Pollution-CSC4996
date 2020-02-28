def cleanOutputFile():
    badfile = open("record.txt", "r", errors="ignore")
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
            
            
        

    



cleanOutputFile()
#evalAccuracy()
