#Load relevant libraries
import warnings
warnings.filterwarnings("ignore")

import json
import keras
import pandas as pd
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
import numpy as np
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense, LSTM, SimpleRNN, Dropout, Activation, Embedding
from datetime import datetime
from tensorflow.keras.callbacks import EarlyStopping

import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

from keras.models import model_from_json

# Import libraries
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
import nltk 

# %matplotlib inline
pd.set_option('display.max_colwidth', 100)

import string
import re
import DataCleaning
#Load data from disc
data = pd.read_csv('../nlp-getting-started/train.csv')

modified_data = data.copy()
# Removing duplicates
modified_data = modified_data.drop_duplicates(subset=['text'])

modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.clean_text(x))
modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.tokenization(x.lower()))
modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.remove_stopwords(x))
modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.listToString(x))
modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.remove_emoji(x))
modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.rename(x))
modified_data['text'] = modified_data['text'].apply(lambda x: DataCleaning.sentenceStemmer(x))

# New dataframe with of missing location features
df_new = modified_data.copy()
bool_series = pd.isnull(df_new["location"])
df1 = df_new[bool_series]

df_new.dropna(subset=['location'], inplace=True)
usa = df1[:497]
new_york = df1[498:994]
united_states = df1[995:1490]
london = df1[1491:1986]
canada = df1[1987:2482]

# filling missing values with top 5 most used locations
usa['location'].fillna('usa', inplace=True)
new_york['location'].fillna('new york', inplace=True)
united_states['location'].fillna('united states', inplace=True)
london['location'].fillna('london', inplace=True)
canada['location'].fillna('canada', inplace=True)

# Merging the dataframes
df2 = usa.append(new_york)
df3 = df2.append(united_states)
df4 = df3.append(london)
df5 = df4.append(canada)
final_df = df_new.append(df5)

final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.clean_text(x))
final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.tokenization(x.lower()))
final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.remove_stopwords(x))
final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.listToString(x))
final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.remove_emoji(x))
final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.rename(x))
final_df['location'] = final_df['location'].apply(lambda x: DataCleaning.sentenceStemmer(x))

df = final_df.copy()

sentences = df['text'].values
y = df['target'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, 
                                                                    y, test_size=0.2, random_state=42, shuffle=True)
                                                                    
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
X_train

from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=100000)
tokenizer.fit_on_texts(sentences_train)

X_train = tokenizer.texts_to_sequences(sentences_train)
X_test = tokenizer.texts_to_sequences(sentences_test)

vocab_size = len(tokenizer.word_index) + 1  # Adding 1 because of reserved 0 index

from keras.preprocessing.sequence import pad_sequences

max_len = max([len(s.split()) for s in sentences])

X_train = pad_sequences(X_train, padding='post', maxlen=max_len)
X_test = pad_sequences(X_test, padding='post', maxlen=max_len)

X_train = pad_sequences(X_train, maxlen=max_len, padding='post')
X_test =pad_sequences(X_test, maxlen=max_len, padding='post')

from keras.layers import Dense,Dropout,Embedding,LSTM,SpatialDropout1D, Bidirectional

from keras import layers

embedding_dim = 100
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(SpatialDropout1D(0.25))
model.add(Bidirectional(LSTM(128,return_sequences=True)))
model.add(Bidirectional(LSTM(64,return_sequences=False)))
model.add(Dense(32, activation='relu', kernel_initializer='he_normal'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X_train, y_train,
                    epochs=50,
                    verbose=1,
                    validation_data=(X_test, y_test),
                    batch_size=10,
                   callbacks=[EarlyStopping(monitor='val_loss', mode='min', verbose=1)])

keras_embed_model = model.to_json()
with open('../NN_Models/embed_model.json', 'w') as json_file:
    json_file.write(keras_embed_model)

model.save_weights('../NN_Models/embed_Model.h5')

print('saved model!')                                                                    
