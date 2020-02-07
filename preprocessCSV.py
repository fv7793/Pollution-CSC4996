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
            CSVline = CSVline+tW[i]+","+POS[i]+",O,\n"
            #write to file
            file.write(CSVline)
        
        sentNum = sentNum+1
    file.close()

newsTextToCSV('A Department of Public Works crews equipment may be the source of an oily sheen found in the Plumbrook Drain Jan. 17. Macomb County workers took action that day after receiving a tip about oil spilling into the Plumbrook Drain, near 19 Mile Road, west of Ryan Road. Crews from the Macomb County Public Works Office reportedly spent the day taking steps to “contain and absorb” the substance by setting up booms, or floating barriers. They reportedly searched the area to find where the suspected oil had come from. A photo produced by the county shows a rainbow-streaked sheen upon the drain’s water. In a statement, Public Works Commissioner Candice Miller encouraged people to be “our eyes and ears” to rapidly combat pollution. “Protecting our waterways is our No. 1 priority. It is critical that we respond quickly so we are able to prevent pollutants from making their way into Lake St. Clair,” she said. The news of the incident did not reach some Sterling Heights officials right away. At around 4 p.m. that afternoon, Sterling Heights Fire Chief Chris Martin said he was unaware of the spill and planned to look into the incident. The city’s community relations director, Bridget Kozlowski, also hadn’t heard about the incident until contacted by the Sentry. Dan Heaton, public relations manager for the Macomb County Public Works Office, said his department typically works with the Fire Department on environmental matters like these, though he added that he “can’t speak directly to this incident.” City officials said in a press release dated later that day that they told the Macomb County Public Works Office that a Sterling Heights Department of Public Works crew had used heavy machinery in the area, which might have affected the drain. “The city of Sterling Heights is investigating whether the heavy machinery malfunctioned causing the discharge of hydraulic fluid and is fully cooperating with the MCPWO,” the statement reads.',"CSVtest.csv")
