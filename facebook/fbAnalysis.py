#This program analyses the fb_logan_city.txt file sachin prepared.
import io
import json
import nltk
import os
import csv

import textmining
import numpy as np
from textblob import TextBlob

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

from google.cloud import translate
import six

#must include your google translate credentials
translate_client = translate.Client.from_service_account_json('../creds.json')

#translates text to any target language
def translate_text(target, text):
	#check text is a fine format for translation api
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
	#translate api call
    result = translate_client.translate(
        text, target_language=target)
    return result

posts = [] #array of text posts
with open("fb_logan_city.txt", "r") as dataFile:

	#fancy string manipulation to extract text data
	for line in dataFile:
		first = line.split("u'message': u")
		second = first[1].split(", u'id':")
		fbPost = second[0]
		fbPost = fbPost[1:-1]
		posts.append(fbPost)

outputJson = {}

#initialise text processing
stopwords = set(stopwords.words('english'))
whitelist = [''] #currently not provided
blacklist = ['https'] #currently not provided

dirname = os.path.dirname(__file__)

#prepare output json with "query" set to fb
outputJson["fb"] = []

#initialise tdm generator
tdm = textmining.TermDocumentMatrix()

matrix = []
docs = []

j = 0
for post in posts:
	#translate to english
	translation = translate_text("en", post)
	translated = TextBlob(translation['translatedText'])

	#clean words: remove stops, query words, white/blacklist and undefined words
	words = translated.words
	cleanedWords = []
	for word in words:
		lower = word.lower()
		if (not lower in stopwords and len(word.define()) != 0 and not lower in blacklist) or lower in whitelist:
			cleanedWords.append(lower)

	if len(cleanedWords) > 0: #if we understood at least 1 word
		analysis = TextBlob(' '.join(cleanedWords))

		tempElement = {
			"text": post,
			"cleanedWords": cleanedWords,
			"originalLanguage": translation['detectedSourceLanguage'],
			"translatedText": translated.string,
			"polarity": analysis.sentiment.polarity,
			"subjectivity": analysis.sentiment.subjectivity,
		}
		
		doc = ' '.join(cleanedWords)
		if not doc in docs:
			docs.append(doc)
			tdm.add_doc(doc) #fill tdm

			outputJson["fb"].append(tempElement)
		j = j + 1


#generate tdm
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

	filename = os.path.join(dirname, 'tdm/fb-docbyword.csv')
	with open(filename, 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		for row in printable:
			wr.writerow(row)

filename = os.path.join(dirname, 'processedFBData.json')
with open(filename, 'w') as outfile:
	json.dump(outputJson, outfile)

