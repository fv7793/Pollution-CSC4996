

def openAndParseCSV(CSVfile):
    csv = open(CSVfile,"r")
    line = csv.readline()
    cnt = 1

    t_s = []
    sent = []
    while line:
        firstWord = False
       #print("Line {}: {}".format(cnt, line.strip()))
        if(line[0]=="S"): #start of a new sentence
            if len(sent)!=0:
                t_s.append(sent)
                print(sent)
                sent = []
        split = line.split(",")
        tuple = (split[len(split)-4],split[len(split)-3], split[len(split)-2])
        sent.append(tuple)
        #put it in a tuple and append to sent
        
        line = csv.readline()
        cnt += 1
    csv.close()
    return t_s

CSVcontent = openAndParseCSV("CSVtest.csv")
# format of CSV content:
#[ [(word,POS,tag),...],...,[(word,POS,tag),...] ]
