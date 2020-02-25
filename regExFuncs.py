import re

#function to take a sentence and return the date in it - multiple formats attempt 1

dates = "04-04-2004; 04/04/04; 4/04/04; 4/4/05; April 04, 2004; March 24, 2004; April. 24, 2004; April 24 2004; 24 Mar 2004; 24 March 2004; 4 June. 2004; 24 August, 2010; Mar 22nd, 2006; Jul 21st, 2007; Mar 24th, 2004; Jan 2009; Dec 2009; Oct 2014; 6/2004; 12/2004; 2018; 2019"

#multiple formats
regEx = r'(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)?(?:\d{2,4})'

result = re.findall(regEx, dates)
print(result)





    
