##def baseline_model():
##    model = Sequential()
##    model.add(Dense(8, input_dim=4, activation='relu'))
##    model.add(Dense(3, activation='softmax'))
##    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
##    return model
##
##model = baseline_model();
##model.fit(X,dummy_y,epochs=250,verbose=1)
##y_pred = model.predict_classes(X)



import keras
import numpy as np
import pandas as pd
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
#read in training data
from keras.callbacks import EarlyStopping
#set early stopping monitor so the model stops training when it won't improve anymore
early_stopping_monitor = EarlyStopping(patience=3)
train_df_2 = pd.read_csv('./small-csv.csv', encoding='latin1')

temp = []
temp2 = []
temp3=[]
for t in train_df_2.Words:
    temp.append(t)
for t in train_df_2.POS:
    temp2.append(t)
for t in train_df_2.Tag:
    temp3.append(t)

Dict = {'Words':temp,'POS':temp2, 'Tag':temp3}
df = pd.DataFrame(Dict)
#print (df)
#print(df.dtypes)
df['Words'] = pd.to_numeric(df['Words'], errors='coerce')
df['Tag'] = pd.to_numeric(df['Tag'], errors='coerce')
df = df.replace(np.nan, 0, regex=True)
##    try:
##        x = float(t)
##    except:
##        print(t)

#view data structure
print(train_df_2.head())

#create a dataframe with all training data except the target column
train_X_2 = df#.drop(columns=['Tag'])

#check that the target variable has been removed
print(train_X_2.head())

#one-hot encode target column
train_y_2 = df#.drop(columns=['POS'])#to_categorical(train_df_2.Tag) #is or is not a chem
##from sklearn.preprocessing import OneHotEncoder
##ohe = OneHotEncoder()
##train_2 = train_df_2
##train_2 = ohe.fit_transform(train_y_2).toarray()

#vcheck that target column has been converted
print(train_y_2[0:5])

#create model
model_2 = Sequential()

#get number of columns in training data
n_cols_2 = train_X_2.shape[1]

#add layers to model
model_2.add(Dense(250, activation='relu', input_shape=(n_cols_2,)))
model_2.add(Dense(250, activation='relu'))
model_2.add(Dense(250, activation='relu'))
model_2.add(Dense(2, activation='softmax'))

#compile model using accuracy to measure model performance
model_2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train model
model_2.fit(train_X_2, train_y_2, epochs=150, validation_split=0.2, callbacks=[early_stopping_monitor])


