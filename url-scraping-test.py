import requests #library that communicates requests from scraper to the web page
from bs4 import BeautifulSoup

page = requests.get('https://www.usnpl.com/search/state?state=MI')
bs = BeautifulSoup(page.text, 'html.parser') #instantiate object with these parameters
#other parsers exist other than this one

allLinksHolder = bs.find(class_='table table-sm') #just the table
justLinks = allLinksHolder.find_all('a') #all anchor tags within that table

allItalicLinkChildren = allLinksHolder.find_all('i')


#THIS LOOP SUCCESSFULLY FINDS AND PRINTS ONLY THE NAMES
allNewsNamesHolder = allLinksHolder.find_all('td')
for row in allNewsNamesHolder:
    if row.get('class') is not None and row.get('class')[0] == 'w-50':
        nameA = row.find_all('a')
        for name in nameA:
            n = name.contents[0]
            print(n)


#failed attemptes to do what the above loop does
##    if name.contents[0]=='<a href="newspapers?q=4893">Tecumseh Herald</a>':
##        print(name.contents[0])
##        #if name.get('class')[0]=='w-50':
##        #    print(name.contents[0])

        
##firstClassMatch = bs.find(class_='w-50')
##allNewsNamesHolder = allLinksHolder.find_all('td')
##for nameC in allNewsNamesHolder:
##    if nameC.contents[0] is not None:
##    #if they have the same class as firstClassMatch
##        print(nameC.contents[0])

##justNames = allNewsNamesHolder.find_all('a')

##for name in justNames:
##    n = name.contents[0]
##    print(n)


#THIS LOOP SUCCESSFULLY ONLY MINES THE LINKS TO THE NEWS WEBSITES
for italicChild in allItalicLinkChildren:
    z=italicChild.get('class')
    for link in justLinks:
        x=link.contents[0]
        if x is italicChild and italicChild.get('class')[1] == 'fa-link':
            y = link.get('href')
            print(y)
    
    #ALL OF THESE WERE AN ATTEMPT AT SAYING:
    #if the child item of the 'a' tag (link.contents[0])
        #has the class 'fas fa-link', show it, else don't
    #the problem is that link.contents[0] is recognized as a bs4 Tag object
        #BUT only until you try to access its attributes, then it becomes a navigblestring object
        #unsure how that happens but it does so had to give up on that idea for now
    
    
    #if(link.contents[0]!=NoneType)
        #testsoup = BeautifulSoup(link.contents[0], 'html.parser')
    
    #x=link.contents[0]
    #z=x['class'] #<--- this is how the documentations says to access the class of it
    #print(z)

    #if(x['class']=='fas fa-link')
        #print the link href, else don't
    
    
