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
    positions = []
    tag = []
    POS = []
    ent = []
    NLPtxt = nlp(splitContent)
    for eachWord in NLPtxt:
        tokenizedWords.append(eachWord.text.upper())
        tag.append(eachWord.tag_)
        positions.append(eachWord.ent_iob_)
        ent.append(eachWord.ent_type_)
    return tokenizedWords, tag, positions, ent

def newsTextToTSV(text, TSVfile):
    #open CSV

#TODO: REMOVE COMMAS FROM THE GIVEN TEXT BEFORE INSERTING INTO CSV
    
    file = open(TSVfile, 'a+', encoding='cp437')
    file.write('-DOCSTART-')
    tS = convertScrapedtoSent(text)
    sentNum = 1
    for sent in tS:
        tW, tag, position, ent = paragraphToWords(sent)
        firstWord = True
        for i in range(len(tW)):
            TSVline = ""
            if(firstWord==True):
                TSVline = "\n"
                firstWord=False
            else:
                TSVline = ""
    
            if position[i]=='O':
                x = ""
            TSVline = TSVline+tW[i]+" "+tag[i]+" "+position[i]+" "+position[i]+" "+"\n"
            #write to file
            file.write(TSVline)
        
        sentNum = sentNum+1
    file.write('\n')
    file.close()


txtfile = open("sophia-200-article-bodies.txt", 'r', encoding='cp437', errors='ignore')
line = txtfile.readline()
while line:
    if "-DOCSTART-" not in line:
        newsTextToTSV(line, "sophia-200-articles-tsv.txt")
    line=txtfile.readline()












        
