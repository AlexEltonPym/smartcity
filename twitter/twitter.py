import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import io
import json
import os
import datetime

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
		
	for tweet in Tweets:
		if i == 0 and tweet != {}: #dont include queries with no results
			tweetJson[query] = []
		i = i + 1

		alreadyIn = False
		for alreadyInserted in tweetJson[query]:
			if alreadyInserted['text'] == tweet.full_text:
				alreadyIn = True
				alreadyInserted['duplicantCount'] += 1
		if not alreadyIn:
			tempTweet = {
				"text": tweet.full_text, #store the tweet text and any other tweet data
				"location": tweet.user.location,
				"duplicantCount": 0
			}

			if tweet.coordinates:
				tempTweet['coordinates'] = tweet.coordinates
			tweetJson[query].append(tempTweet)
		else:
			print("Duplicant tweet detected, not including.")

	print("Finished query \'" + query + "\'")
	print("Numnber of tweets found: " + str(len(tweetJson[query])))

with open('data/twitter_'+str(datetime.datetime.now())+'.json', 'w') as outfile:
	json.dump(tweetJson, outfile)