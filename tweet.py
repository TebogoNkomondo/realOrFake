from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import json
import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json


import credentials


tokenizer = Tokenizer(num_words=3000)

labels = ['Fake', 'Real']

with open('dictionary.json', 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)


def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
    return wordIndices


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)

model.load_weights('model.h5')


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
         

class TwitterListener(StreamListener):  
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self, data):
        try:
            tweetText = json.loads(data)['text']
            testArr = convert_text_to_index_array(tweetText)
            input = tokenizer.sequences_to_matrix([testArr], mode='binary')
            
            pred = model.predict(input)
            
            print('\n',tweetText,'\n')
            
            print('****',labels[np.argmax(pred)], 'Tweet')
            
            # print("%s \n the %s sentiment; %f%% confidence" % (tweetText ,labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
            
            print(json.loads(data)['text'])
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
    fetched_tweets_filename = "text.txt"
    
    tweeter_streamer = TweeterStreamer()
    tweeter_streamer.stream_tweets(fetched_tweets_filename,mylist)
    
