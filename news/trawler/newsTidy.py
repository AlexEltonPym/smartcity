from bs4 import BeautifulSoup
import fileinput
import io

majorQueryNames = ['parramattaRoad', 'fiveDock', 'cronullaPark', 'yarrabilba']

queries = [
	['westconnex', 'parramatta road'], #parramatta road queries
	['five dock'], 	#five dock queries
	['cronulla park', 'logan'], #cronulla park queries
	['yarrabilba', 'cedargrove', 'treatment plant', 'springwood', 'logan'] #yarrabilba queries
]

majorSets = [set() for index in range(len(majorQueryNames))]

for line in fileinput.input(): #for each file
	fullPath = "articles/" + line[0:-1]
	ofile = open(fullPath) #remove \n from line and open file
	soup = BeautifulSoup(ofile, "lxml") #convert html file to a soup object
	paras = soup("p") #find all paragraphs

	articleList = []
	for pa in paras:
		articleList.append(pa.get_text())

	for (queryList, major) in zip(queries, majorSets):
		matching = [s for s in articleList if any(xs in s for xs in queryList)] #if any paragraphs match any current minor query
		if matching:
			major.update(articleList) #add all the paragraphs to the major set
			continue #continue incase the article matches any other major set 

for (name, mSet) in zip(majorQueryNames, majorSets):
	with open('articlesClean/'+name+'.txt', mode='w+', encoding='utf-8') as myfile:
		myfile.write('\n'.join(mSet))