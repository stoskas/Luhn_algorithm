import tweepy 
  
# Exo valei ta dika mou credentials apo to api tou tweeter
consumer_key = "oUNpdHhYxlZ4zgP512hQmbeQv" 
consumer_secret = "D4hpg7NknxXHKqkGrUk9EWhP2CvaXugk6hHH5fIs1KtT3ZbMkF"
access_key = "2244306962-ORcN9ROKsdRAEyjOsduCjzvMtTf24HT7IGSWtWE"
access_secret = "vvs2MIDTXEQ1k9UWAGBNFg1eh4qw59hk1Ij7WUX7lB9eD"
  
# Function to extract tweets 
def get_tweets(userID): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
        
        tweets = api.user_timeline(screen_name= userID, count=50, include_rts = False, tweet_mode = 'extended')
        # Empty Array 
        tmp=[]  
        str1 = " " 
        
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        # tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j.full_text)

        # Printing the tweets 
        print(tmp)
        y = str1.join(tmp) 
        x=len(y.split())
        print(x)

# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("Spiliopoulos_A")  

   
