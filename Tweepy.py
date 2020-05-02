from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor

import credentials


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_user_timeline_tweets(self, num_tweet):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweet):
            tweets.append(tweet)
        return tweets
    
    def get_friend_list(self, num_friends):
        friend_list =[]
        for friend in Cursor(self.twitter_client.friends,id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
        
        


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
            print(data)
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
    
    twitter_client = TwitterClient('pycon')
    print(twitter_client.get_user_timeline_tweets(5))
    # tweeter_streamer = TweeterStreamer()
    # tweeter_streamer.stream_tweets(fetched_tweets_filename,mylist)
    
