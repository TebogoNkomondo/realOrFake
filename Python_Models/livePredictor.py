import json
import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
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

import json
from keras.models import model_from_json

# Import libraries
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
import nltk 
# nltk.download()
import string
import re
# %matplotlib inline

pd.set_option('display.max_colwidth', 100)

import string
import re
from keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer 

# we're still going to use a Tokenizer here, but we don't need to fit it
tokenizer = Tokenizer(num_words=10000)
# for human-friendly printing
labels = ['fake', 'real']

# read in our saved dictionary
with open('./Dictionary_Models/glove_models_dictionary.json', 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)
    
def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
#     words = pad_sequences(words, padding='post', maxlen=23)
#     print(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
    return wordIndices

json_file = open('./NN_Models/Glove_BLSTM_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)

model.load_weights('./NN_Models/Glove_BLSTM_model.h5')

tweetText = 'there is a fire at melville mountain'

tweetText = convert_text_to_index_array(tweetText)

input = pad_sequences([tweetText], padding='post', maxlen=100)
    
pred = model.predict_generator(input)

def rounding(results):
    '''Results needs to be rounded to 0 or 1 for fake or real, respectively'''
    if results < 0.5:
        return 0
    else:
        return 1
    
predictions_final = [rounding(x) for x in pred]

predictions_final

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor


import sys  
sys.path.insert(0, './Python_Models/')
import credentials
# from DataCleaning import clean_text, tokenization, remove_stopwords, listToString, lementization

#punctutation removal
def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Tockenization
def tokenization(text):
    text = re.split('\W+', text)
    return text

# stopword removal 
stopword = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text


# return to string
def listToString(s):     
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 

# Lematizing the words
lemmatizer = WordNetLemmatizer()

def lementization(text):
    text = lemmatizer.lemmatize(text)
    return text


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET) 
        return auth       
    
    
class TweeterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
      
    def stream_tweets(self, fetched_tweet_file, hash_tag_list):
        #handles twitter authentication and twitter streaming API
        listener = TwitterListener(fetched_tweet_file) 
        auth = self.twitter_authenticator.authenticate_twitter_app()       
        stream = Stream(auth, listener)
        
        stream.filter(track=hash_tag_list)


def DataCleaningFunction(text):
    text = clean_text(text)
    text = tokenization(text.lower())
    text = remove_stopwords(text)
    text = listToString(text)
    text = lementization(text.lower())
    return text


def rounding(results):
    '''Results needs to be rounded to 0 or 1 for fake or real, respectively'''
    if results < 0.5:
        return 0
    else:
        return 1
    
    
class TwitterListener(StreamListener):  
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self, data):
        try:
            tweetText = json.loads(data)['text']
            myvar = tweetText
            tweetText = DataCleaningFunction(tweetText)
            testArr = convert_text_to_index_array(tweetText)
            input = pad_sequences([testArr], padding='post', maxlen=100)
            
            pred = model.predict_generator(input)

            predictions_final = [rounding(x) for x in pred]
            
            print('\n',myvar)
            
            print('********************************',labels[predictions_final[0]], 'Tweet ********************************'  )
            
            # print("%s \n the %s sentiment; %f%% confidence" % (tweetText ,labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
      
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True
    
    def on_error(self, status):
        if status == 420:
            return False
        print(status)
        
        
if __name__ == "__main__":
    mylist =['hazard','fire','ablaze','accident','aftershock','ambulance']   
    fetched_tweets_filename = "./nlp-getting-started/feteched_tweets_text.txt"
    
    tweeter_streamer = TweeterStreamer()
    tweeter_streamer.stream_tweets(fetched_tweets_filename,mylist)
             
