tags = ["B-PERCENT", "I-PERCENT", "B-EVENT", "I-EVENT", "B-PRODUCT","I-PRODUCT","B-ORG", "I-ORG","B-LAW", "I-LAW","B-NORP", "I-NORP", "B-ORDINAL", "I-ORDINAL","B-WORK_OF_ART", "I-WORK_OF_ART","B-LOC", "I-LOC","B-DATE", "I-DATE","B-GPE", "I-GPE","B-CARDINAL", "I-CARDINAL","B-PERSON", "I-PERSON","B-FAC", "I-FAC","B-TIME", "I-TIME","B-MONEY", "I-MONEY"]

def removeTags():
    file = open("./data/test.txt",'r',encoding='utf-8')
    newfile = open("./data/newtest.txt","w",encoding='utf-8')
    line = file.readline()
    while line:
        written = False
        for tag in tags:
            if tag in line:
                newfile.write(line.replace(tag, "O"))
                written = True
        if written == False:
            newfile.write(line)
        line = file.readline()

    file.close()
    newfile.close()

def removeSpaces():
    file = open("./test.txt",encoding='utf-8')
    newfile = open("./test2.txt","w",encoding='utf-8')
    line = file.readline()
    while line:
        if line=='\n':
            newfile.write(line)
        elif line[len(line)-1]=='\n':
            if line[len(line)-2]==' ':
                line = line[:len(line)-2]+'\n'
            newfile.write(line)
        line = file.readline()

    file.close()
    newfile.close()



def removeIB():
    file = open("./data/valid.txt",encoding='utf-8')
    newfile = open("./data/valid2.txt","w",encoding='utf-8')
    line = file.readline()
    while line:
        if line=='\n':
            newfile.write(line)
        elif line[len(line)-1]=='\n':
            if line[len(line)-2]=='I' or line[len(line)-2]=='B':
                line = line[:len(line)-2]+'O\n'
            newfile.write(line)
        line = file.readline()

    file.close()
    newfile.close()



def wordsOnly():
    file = open("./test.txt",encoding='utf-8')
    newfile = open("./test2.txt","w",encoding='utf-8')
    line = file.readline()
    while line:
        if line=='\n':
            newfile.write(line)
        else:
            s = line.split(' ')
            newfile.write(s[0]+"\n")
        line = file.readline()

    file.close()
    newfile.close()








wordsOnly()
#removeIB()
#removeSpaces()
#removeTags()
