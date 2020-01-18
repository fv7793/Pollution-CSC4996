#INSTRUCTIONS:
#pip install nltk
#python
#(>>>)import nltk
#(>>>)nltk.download()
#download all packages
#(>>>)exit()
#install beautifulsoup4
#install matplotlib
#install html5lib





import urllib.request
import nltk
response =  urllib.request.urlopen('https://spacy.io/usage/processing-pipelines')
html = response.read()
print(html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

tokens = [t for t in text.split()]
print(tokens)

from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
