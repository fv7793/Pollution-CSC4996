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
    NLPtxt = nlp(splitContent)
    for eachWord in NLPtxt:
        tokenizedWords.append(eachWord.text)
        print(eachWord)
    return tokenizedWords

def newsTextToCSV(text, CSVfile):
    #open CSV
    file = open(CSVfile, 'a+')
    tS = convertScrapedtoSent(text)
    sentNum = 1
    for sent in tS:
        tW = paragraphToWords(sent)
        firstWord = True
        for word in tW:
            CSVline = ""
            if(firstWord==True):
                CSVline = "Sentence "+str(sentNum)+","
                firstWord=False
            else:
                CSVline = "NaN,"
            CSVline = CSVline+word+",O,\n"
            print(CSVline)
            #write to file
            file.write(CSVline)
        
        sentNum = sentNum+1
    file.close()

#1
newsTextToCSV('Drinking water in three Macomb and St. Clair county communities tested positive for contamination, according to state environmental officials. The Michigan Department of Environmental Quality found perfluoroalkyl and polyfluoroalkyl substances, known as PFAS, in water in New Baltimore, Mount Clemens and Ira Township, MLive reported. The agency tested groundwater and treated drinking water in the area in January. The department issued letters March 2 alerting residents to the presence of the substances, which have been used in non-stick cookware, stain resistant fabrics and firefighting foams. The chemicals have been linked to cancer, thyroid disorders, elevated cholesterol and other diseases. Current contamination levels don\'t pose any significant danger, the department said. ”I want to assure the residents of the city that their water is safe to drink and that a boil water advisory has not been issued,” New Baltimore Mayor John Dupray said. ”I will be attending a meeting with the MDEQ early next week to discuss this issue in greater detail. We strive to provide the highest quality water possible and will continue to do so.” The contamination is believed to have originated in Lake St. Clair, though the exact source is unknown. Last year, Gov. Rick Snyder announced that the state is committed to spending more than $23 million to combat PFAS contamination. Plainfield Township, the Saginaw-Midland Corp., Huron Shores Regional Water Authority system in Tawas, Ann Arbor, Grayling and the village of Sparta have also detected PFAS in their water.', "CSVtest.csv")
#13
newsTextToCSV('A Department of Public Works crews equipment may be the source of an oily sheen found in the Plumbrook Drain Jan. 17. Macomb County workers took action that day after receiving a tip about oil spilling into the Plumbrook Drain, near 19 Mile Road, west of Ryan Road. Crews from the Macomb County Public Works Office reportedly spent the day taking steps to “contain and absorb” the substance by setting up booms, or floating barriers. They reportedly searched the area to find where the suspected oil had come from. A photo produced by the county shows a rainbow-streaked sheen upon the drain’s water. In a statement, Public Works Commissioner Candice Miller encouraged people to be “our eyes and ears” to rapidly combat pollution. “Protecting our waterways is our No. 1 priority. It is critical that we respond quickly so we are able to prevent pollutants from making their way into Lake St. Clair,” she said. The news of the incident did not reach some Sterling Heights officials right away. At around 4 p.m. that afternoon, Sterling Heights Fire Chief Chris Martin said he was unaware of the spill and planned to look into the incident. The city’s community relations director, Bridget Kozlowski, also hadn’t heard about the incident until contacted by the Sentry. Dan Heaton, public relations manager for the Macomb County Public Works Office, said his department typically works with the Fire Department on environmental matters like these, though he added that he “can’t speak directly to this incident.” City officials said in a press release dated later that day that they told the Macomb County Public Works Office that a Sterling Heights Department of Public Works crew had used heavy machinery in the area, which might have affected the drain. “The city of Sterling Heights is investigating whether the heavy machinery malfunctioned causing the discharge of hydraulic fluid and is fully cooperating with the MCPWO,” the statement reads.',"CSVtest.csv")
