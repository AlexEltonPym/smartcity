import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import io
import json

import os





consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

queries = ['parramatta road', 'five dock', 'yarrabilba', 'cronulla park']

tweetJson = {}

for query in queries:
	Tweets = tweepy.Cursor(api.search, q=query, tweet_mode='extended', include_entities='True').items(1000)
	i = 0
	j = 0
		
	for tweet in Tweets:
		if i == 0 and tweet != {}: #dont include queries with no results
			tweetJson[query] = []
		i = i + 1
		tempTweet = {
			"text": tweet.full_text, #store the tweet text and any other tweet data
			"location": tweet.user.location,
		}
		#print(tempTweet["location"])

		if tweet.coordinates:
			tempTweet['coordinates'] = tweet.coordinates
			j=j+1
			
		
		tweetJson[query].append(tempTweet)
	
	print("Finished: \'" + query + "\'")
	print("num found: " + str(i))
	print("with coordinates: " + str(j))

with open('twitter.json', 'w') as outfile:
	json.dump(tweetJson, outfile)