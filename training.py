t_s = []
f = open("CSVtest.csv","r")
line = f.readline()
cnt = 1

sent = []
while line:
    firstWord = False
   #print("Line {}: {}".format(cnt, line.strip()))
    if(line[0]=="S"): #start of a new sentence
        if len(sent)!=0:
            t_s.append(sent)
            print(sent)
            sent = []

    #test for ,,, FIRST (if it doesn't find it, use the general case)
    if ",,," in line:
        split = line.split(",")
        tuple = (",",split[3],split[4])
        sent.append(tuple)
    #else we know this won't be a comma so we can just use split
    else:
        split = line.split(",")
        tuple = (split[1],split[2],split[3])
        sent.append(tuple)
    #put it in a tuple and append to sent
        
    line = f.readline()
    cnt += 1
f.close()



#if the line has sentence # in the column, start a new sentence list
#make a tuple for each line, put it in the current sentence object

#t_s is a list of sentences
#each sentence should be
#[
#(word,tag),
#(word,tag), ...
#]


#parse the CSV into t_s

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]



X_train = [sent2features(s) for s in t_s]
y_train = [sent2labels(s) for s in t_s]

X_test = [sent2features(s) for s in t_s]
y_test = [sent2labels(s) for s in t_s]

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_train, y_train)

labels = list(crf.classes_)
y_pred = crf.predict(X_test)
metrics.flat_f1_score(y_test, y_pred,
                      average='weighted', labels=labels)
