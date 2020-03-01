import pandas as pd
import numpy as np

data = pd.read_csv("csv-file.csv", encoding="latin1")
test = pd.read_csv("testing.csv", encoding='latin1')

data = data.fillna(method="ffill")
test = test.fillna(method="ffill")
data.tail(10)
test.tail(10)
print(data)
words = list(set(data["Word"].values))
testwords = list(set(test["Word"].values))
words.append("ENDPAD")
testwords.append("ENDPAD")
n_words = len(words);
tn_words = len(testwords)
print(tn_words)
tags = list(set(data["Tag"].values))
testtags = list(set(test["Tag"].values))
n_tags = len(tags);
tn_tags = len(testtags)
print(testwords)
print(testtags)

class SentenceGetter(object):
    
    def __init__(self, data):
        self.n_sent = 1
        self.data = data
        self.empty = False
        agg_func = lambda s: [(w, p, t) for w, p, t in zip(s["Word"].values.tolist(),
                                                           s["POS"].values.tolist(),
                                                           s["Tag"].values.tolist())]
        self.grouped = self.data.groupby("Sentence #").apply(agg_func)
        self.sentences = [s for s in self.grouped]
    
    def get_next(self):
        try:
            s = self.grouped["Sentence: {}".format(self.n_sent)]
            self.n_sent += 1
            return s
        except:
            return None


getter = SentenceGetter(data)
sent = getter.get_next()



sentences = getter.sentences

testGet = SentenceGetter(test)
testsents = testGet.sentences
print(len(sentences))
import matplotlib.pyplot as plt
plt.style.use("ggplot")
plt.hist([len(s) for s in sentences], bins=50)
plt.show()


max_len = 50
word2idx = {w: i for i, w in enumerate(words)}
tag2idx = {t: i for i, t in enumerate(tags)}

word2idxtest = {w: i for i, w in enumerate(testwords)}
tag2idxtest = {t: i for i, t in enumerate(testtags)}



from keras.preprocessing.sequence import pad_sequences
X = [[word2idx[w[0]] for w in s] for s in sentences]
X = pad_sequences(maxlen=max_len, sequences=X, padding="post", value=n_words - 1)

y = [[tag2idx[w[2]] for w in s] for s in sentences]
y = pad_sequences(maxlen=max_len, sequences=y, padding="post", value=tag2idx["O"])

tx = [[word2idxtest[w[0]] for w in s] for s in testsents]
tx = pad_sequences(maxlen=max_len, sequences=tx, padding="post", value=tn_words - 1)

ty = [[tag2idxtest[w[2]] for w in s] for s in testsents]
ty = pad_sequences(maxlen=max_len, sequences=ty, padding="post", value=tag2idxtest["O"])



from keras.utils import to_categorical

y = [to_categorical(i, num_classes=n_tags) for i in y]
ty = [to_categorical(i, num_classes=n_tags) for i in ty]
from sklearn.model_selection import train_test_split

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.1)

Xtst, Xbl, ytst, ybl = train_test_split(tx, ty, test_size=0.999)


from keras.models import Model, Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional

input = Input(shape=(max_len,))
model = Embedding(input_dim=n_words, output_dim=50, input_length=max_len)(input)
model = Dropout(0.1)(model)
model = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(model)
out = TimeDistributed(Dense(n_tags, activation="softmax"))(model)  # softmax output layer
model = Model(input, out)
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
history = model.fit(X_tr, np.array(y_tr), batch_size=32, epochs=5, validation_split=0.1, verbose=1)



##hist = pd.DataFrame(history.history)
##plt.figure(figsize=(12,12))
##plt.plot(hist["acc"])
##plt.plot(hist["val_acc"])
##plt.show()

newfile = open("recordtest.txt", "w",errors="ignore")
numPred = 0
for i in range(1, len(Xbl)-1, 100):
    numPred+=1
    p = model.predict(np.array([Xbl[i]]))
    p = np.argmax(p, axis=-1)
    #print("{:15} ({:5}): {}".format("Sentence: #","Word", "True", "Pred"))
    newfile.write("Sentence " + str(i)+"\n")
    for w, pred in zip(Xbl[i], p[0]):
        newfile.write("{:15}: {}".format(testwords[w], testtags[pred])+"\n")

newfile.close()









