import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

def convertScrapedtoSent(splitContent):
    tokenizedSent = []
    #tokenize
    NLPtxt = nlp(splitContent)
    for eachSent in NLPtxt.sents:
        tokenizedSent.append(eachSent.string.strip())
    return tokenizedSent

def paragraphToWords(splitContent):
    tokenizedWords = []
    POS = []
    NLPtxt = nlp(splitContent)
    for eachWord in NLPtxt:
        tokenizedWords.append(eachWord.text)
        POS.append(eachWord.tag_)
    return tokenizedWords, POS


def newsTextToCSV(text, CSVfile):
    #open CSV

#TODO: REMOVE COMMAS FROM THE GIVEN TEXT BEFORE INSERTING INTO CSV
    
    file = open(CSVfile, 'a+')
    tS = convertScrapedtoSent(text)
    sentNum = 1
    for sent in tS:
        tW, POS = paragraphToWords(sent)
        firstWord = True
        for i in range(len(tW)):
            CSVline = ""
            if(firstWord==True):
                CSVline = "Sentence "+str(sentNum)+","
                firstWord=False
            else:
                CSVline = "NaN,"
            if tW[i]==','or tW[i]=='\\':
                continue
            CSVline = CSVline+tW[i]+","+POS[i]+",O,\n"
            #write to file
            file.write(CSVline)
        
        sentNum = sentNum+1
    file.close()

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
wholeFile = ""
for sentence in CSVcontent:
    for wordLine in sentence:
        #print(wordLine)
        wholeFile=wholeFile+" "+wordLine[0]

#print(wholeFile)
newsTextToCSV(wholeFile, "CSVtext.csv")





