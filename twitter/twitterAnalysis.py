import io
import json
import nltk
import os
import csv
import time

import textmining
import numpy as np
from textblob import TextBlob

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


from google.cloud import translate
import six

translate_client = translate.Client.from_service_account_json('../creds.json')


def translate_text(target, text):

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    result = translate_client.translate(
        text, target_language=target)

    return result



with open("twitter.json", "r") as dataFile:
	jsonData = json.load(dataFile)

outputJson = {}

stopwords = set(stopwords.words('english'))
whitelist = ['']
blacklist = ['https']


dirname = os.path.dirname(__file__)

for query in jsonData:
	queryWords = TextBlob(query).words
	outputJson[query] = []

	tdm = textmining.TermDocumentMatrix()
	matrix = []
	docs = []

	j = 0

	for tweet in jsonData[query]:

		translation = translate_text("en", tweet['text'])
		translated = TextBlob(translation['translatedText'])

		#clean words: remove stops, query words and white/blacklist
		words = translated.words
		cleanedWords = []
		for word in words:
			lower = word.lower()
			if (not lower in stopwords and len(word.define()) != 0 and not lower in blacklist and not lower in queryWords) or lower in whitelist:
				cleanedWords.append(lower)

		if len(cleanedWords) > 0: #if we understood at least 1 word
			analysis = TextBlob(' '.join(cleanedWords))

			tempElement = {
				"text": tweet['text'],
				"location": tweet['location'],
				"originalLanguage": translation['detectedSourceLanguage'],
				"translatedText": translated.string,
				"polarity": analysis.sentiment.polarity,
				"subjectivity": analysis.sentiment.subjectivity,
				"cleanedWords": cleanedWords,
			}
			
			doc = ' '.join(cleanedWords)
			if not doc in docs:
				docs.append(doc)
				tdm.add_doc(doc) #fill tdm

				outputJson[query].append(tempElement)
			j = j + 1


	i = 0
	for row in tdm.rows(cutoff=1): #cutoff controls the number of times docs a words must be in to count
		if i == 0: 
			wordsFull = list(row) #save the names of the words
		else:
			matrix.append(np.array(row)) #add each row of the tdm, (as nparray) to a list
		i = i + 1

	if len(matrix) > 0: #check for empty search queries
		npMatrix = np.array(matrix) #create a nparray of nparrays
		npMatrix = np.transpose(npMatrix)
	
		printable = [['Document/Word']]
		printable[0].extend(docs) #add docs across top


		j = 0
		for word in wordsFull:
			line = []
			line.append(word)
			line.extend(npMatrix[j].tolist())
			printable.append(line)
			j = j + 1

		#File saving

		filename = os.path.join(dirname, 'tdm/' + query + '-docbyword.csv')
		with open(filename, 'w') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			for row in printable:
				wr.writerow(row)

filename = os.path.join(dirname, 'processedTwitterData.json')
with open(filename, 'w') as outfile:
	json.dump(outputJson, outfile)

