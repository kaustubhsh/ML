# !/usr/bin/python3
import tweepy

consumer_key = "blEoppnaZTlEFGemt3hBa8abH"
consumer_secret ="6HRYJ0kc244D7T1j9HU0smBVpJLZRlTtETWXYdFiKSKyZyNvOO"
access_key = "792211276244000768-rXrBFfIFD9cNvAm6ZDK2TmOVf5JaZuh"
access_secret = "gPjVeWfmV43QzUnl3RcY7V0uKdP2NK16jBW9y7GS2Cgfs"

def get_tweets(username): 
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=50
        tweets = api.user_timeline(screen_name=username) 
        
        # Empty Array 
        tmp=[]  
                
        # create array of tweet information: username,     
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv:
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 
  

#        for items in search:
 #           print("\n")
  #          print(items.text)
# Driver code 
if __name__ == '__main__': 
  #data = input('Enter twitter handle')
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    
    choice=input('Enter \n 1. twitter handle \n 2. search \t:  ')
    if choice=='1':
        get_tweets(input('Enter Twitter handle : '))
    elif choice=='2':
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_key, access_secret) 
        api = tweepy.API(auth)
#        search=tweepy.Cursor(api.search,input('Enter Your Search : '),lang="en").items(5)
        search=tweepy.Cursor(api.search,lang="en").items(5)
        for items in search:
              print(items.name)
              print("\n")
