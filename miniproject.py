from pickletools import read_uint1
import botometer
import tweepy
import pandas as pd
import re
from google.cloud import language_v1
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/alandautov/Desktop/EC463-Mini-project/ec463-miniproject-363700-d23fada107c6.json"
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
username = input('Enter username: ')
no_of_tweets = 20


'''
botometer
'''

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@'+username)

print()
print("Botometer Result:")

print("Username: " + result["user"]["user_data"]["screen_name"])
print("Language: " + result["user"]["majority_lang"])

print()
print("Cap, English: " + str(result["cap"]["english"]))
print("Cap, Universal: " + str(result["cap"]["universal"]))

print()
print("Raw Scores, English, Astroturf: " + str(result["raw_scores"]["english"]["astroturf"]))
print("Raw Scores, English, Fake Follower: " + str(result["raw_scores"]["english"]["fake_follower"]))
print("Raw Scores, English, Financial: " + str(result["raw_scores"]["english"]["financial"]))
print("Raw Scores, English, Other: " + str(result["raw_scores"]["english"]["other"]))
print("Raw Scores, English, Overall: " + str(result["raw_scores"]["english"]["overall"]))
print("Raw Scores, English, Self Declared: " + str(result["raw_scores"]["english"]["self_declared"]))
print("Raw Scores, English, Spammer: " + str(result["raw_scores"]["english"]["spammer"]))

print()
print("Raw Scores, Universal, Astroturf: " + str(result["raw_scores"]["universal"]["astroturf"]))
print("Raw Scores, Universal, Fake Follower: " + str(result["raw_scores"]["universal"]["fake_follower"]))
print("Raw Scores, Universal, Financial: " + str(result["raw_scores"]["universal"]["financial"]))
print("Raw Scores, Universal, Other: " + str(result["raw_scores"]["universal"]["other"]))
print("Raw Scores, Universal, Overall: " + str(result["raw_scores"]["universal"]["overall"]))
print("Raw Scores, Universal, Self Declared: " + str(result["raw_scores"]["universal"]["self_declared"]))
print("Raw Scores, Universal, Spammer: " + str(result["raw_scores"]["universal"]["spammer"]))


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
    attributes_container = [[tweet.created_at, tweet.favorite_count, tweet.source, tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)

#getting last tweetis in single string
combined_tweets = ""
for tweet in tweets: 
    combined_tweets = combined_tweets + tweet.text + "\n"

combined_tweets = re.sub(r'http\S+', '\0', combined_tweets)
# print(combined_tweets)
# print(tweets_df)
'''
Google Cloud Natural Language AI
'''
# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
document = language_v1.Document(
    content=combined_tweets, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

combined_tweets = combined_tweets.replace("\n", "")
print("")
print("Text analyzed:")
print(combined_tweets)
# print("Text: {}".format(combined_tweets))
print("")
print("Sentiment(score, magnitude): {}, {}".format(sentiment.score, sentiment.magnitude))
print("")




