#twitter data extractor

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import io
import json
import os
import datetime
import fileinput


#environment variables for Somwrita's twitter application
#do not push environment variables to the git
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

queries = []

#process stdin query list
for line in fileinput.input():
    queries.append(line[:-1]) #remove \n

print("Searching these queries:")
print(queries)

tweetJson = {}

for query in queries:
	#searches past 7 days, max items found rarely reaches 300 so this will get all
	Tweets = tweepy.Cursor(api.search, q=query, tweet_mode='extended', include_entities='True').items(1000)
	i = 0
		
	for tweet in Tweets:
		if i == 0 and tweet != {}: #dont include queries with no results
			tweetJson[query] = []
		i = i + 1

		#caluclate if the tweet already has been inserted
		#typically finds perfect retweets or bot posts
		alreadyIn = False
		for alreadyInserted in tweetJson[query]:
			if alreadyInserted['text'] == tweet.full_text:
				alreadyIn = True
				alreadyInserted['duplicantCount'] += 1 #if it was found then count that
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

#save with a datetime, this program should be run once a week once the system is deployed
with open('data/twitter_'+str(datetime.datetime.now())+'.json', 'w') as outfile:
	json.dump(tweetJson, outfile)