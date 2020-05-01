from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials

mylist =['hazard','fire','ablaze','accident','aftershock','ambulance']

class StdOutListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        

 class TweeterStreamer():
      
     def stream_tweets(self, fetched_tweet_file, hash_tag_list):
        #handles twitter authentication and twitter streaming API
        listener = StdOutListener()
        auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
        
        stream = Stream(auth, listener)
        
        stream.filter(track=hash_tag_list)
         
        
        
if __name__ == "__main__":
    
