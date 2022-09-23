import tweepy
import botometer
import pandas as pd
from google.cloud import language_v1

'''
basic variables
'''

consumer_key = 'iXZJ90ySLX27aa1q4axACMdVC'
consumer_secret = 'fartPliQt1rSSKak1k8IMh2bvkCK4DBxkXNVAmAYE3g2vvSobp'
access_token = "1571857911298629633-KIPIP5KC86oynuXmCsAP4QsraT0Z2v"
access_token_secret = "GmA6JVh2tmdsH42by3SUiuh1mfGU4JI2KJLok8qkzxwlJ"

rapidapi_key = "a0f0a80c61msh268ebbe71df7d3ap147eb8jsnc5b0bb6bbbcb"
botometer_api_url = 'http://botometer-pro.p.rapidapi.com'
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret
  }

# ask for an username
username = input('Enter username:')
no_of_tweets = 10


'''
botometer
'''

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@'+username)

print(result)


'''
tweepy
'''

#Pass in twitter API authenication key
auth = tweepy.OAuthHandler(consumer_key=consumer_key, 
                           consumer_secret=consumer_secret)

#Instantiate tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)

    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)

print(tweets_df)
'''
Google Cloud Natural Language AI
'''





