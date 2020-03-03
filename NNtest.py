#Dependencies
import numpy as np
import pandas as pd
#dataset import
dataset = pd.read_csv('./small-csv.csv', encoding='latin1') #You need to change #directory accordingly
dataset.head(10) #Return 10 rows of data

#Changing pandas dataframe to numpy array
#Changing pandas dataframe to numpy array
#X = dataset.iloc[:,:20].values
#y = dataset.iloc[:,20:21].values
X = dataset.iloc[:,:2].values
y = dataset.iloc[:,2:3].values

#print(X)
#print(y)

allWords=[]
for row in X:
    allWords.append(row[0])
allSet = set(allWords)
sortedSet = sorted(allSet)

wordFloatPairs = []
i = 0
for word in sortedSet:
    wordFloatPairs.append((float(i), word))
    i+=1
#print(wordFloatPairs)

#make a set of all words
#alphebatize them
#make a list of tuples where each word is paired with their order in the list
#every time that word appears, replace it with the key
for row in X:
    for wordPair in wordFloatPairs:
        if row[0]==wordPair[1]:
           row[0]=wordPair[0]
           break

    
allPOS=[]
for row in X:
    allPOS.append(row[1])
allPOSSet = set(allPOS)
sortedPOSSet = sorted(allPOSSet)

posFloatPairs = []
i = 0
for pos in sortedPOSSet:
    posFloatPairs.append((float(i), pos))
    i+=1
#do the same for tags
for row in X:
    for posPair in posFloatPairs:
        if row[1]==posPair[1]:
           row[1]=posPair[0]
           break

#POS AND WORDS ARE FLOATS BEYOND THIS POINT_____________________


#Normalizing the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
y = ohe.fit_transform(y).toarray()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1)

#Dependencies
import keras
from keras.models import Sequential
from keras.layers import Dense
# Neural network
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train,validation_data = (X_test,y_test), epochs=20, batch_size=64)



y_pred = model.predict(X_test)
#Converting predictions to label
pred = list()
for i in range(len(y_pred)):
    pred.append(np.argmax(y_pred[i]))
print(pred)
#Converting one hot encoded test label to label
test = list()
for i in range(len(y_test)):
    test.append(np.argmax(y_test[i]))
print(test)


from sklearn.metrics import accuracy_score
a = accuracy_score(pred,test)
print('Accuracy is:', a*100)


