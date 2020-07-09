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

        # Appending tweets to the empty array tmp 
        for j in tweets: 
            tmp.append(j.full_text)

        # Printing tweets 
        print(tmp)
        y = str1.join(tmp) 
        get_tweets.x=len(y.split())
        # print(x)

# Driver code 
if __name__ == '__main__': 
    print("***************************************************************************")
    print("***************************************************************************")
    print("************************** Welcome to my program **************************")
    print("***************************************************************************")
    print("***************************************************************************")
    print("\n\n!!!'Import_tweets' is a python program which compares the last 50 tweets from two users.!!!")
    username1 = input("\nPlease enter 1st Twitter's user name (exclude'@') :")
    username2 = input("\nPlease enter 2nd Twitter's user name (exclude'@') :")
    get_tweets(username1)
    ela = get_tweets.x
    print(get_tweets.x)
    get_tweets(username2)
    pou = get_tweets.x
    print(get_tweets.x)

    if ela>pou:
        print(username1 +" used more words than " + username2)
    else:
        print(username2 + ' used more words than '+ username1)

     
    
    
    
    




  
  
    


