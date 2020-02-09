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
                #print(sent)
                sent = []
        if ",,," in line:
            temp = ""
        #else we know this won't be a comma so we can just use split
        else:
            #TODO: account for commas being used between #s (million) in sample corpus
            split = line.split(",")
            if '\\' in split[len(split)-4]:
                removeBS = split[len(split)-4].split('\\')
                #print(removeBS)
                if(removeBS[1]!=''):
                    tuple = (removeBS[1][0],removeBS[1][0],split[len(split)-2])
                    sent.append(tuple)
                    tuple = (removeBS[1][1:],split[len(split)-3],split[len(split)-2])
                    sent.append(tuple)
            else:
                tuple = (split[len(split)-4],split[len(split)-3],split[len(split)-2])
                sent.append(tuple)
            #put it in a tuple and append to sent
        
        line = csv.readline()
        cnt += 1
    csv.close()
    return t_s


CSVcontent = openAndParseCSV("CSVtags.csv")
# format of CSV content:
#[ [(word,POS,tag),...],...,[(word,POS,tag),...] ]
for sentence in CSVcontent:
    for wordLine in sentence:
        print(wordLine)






