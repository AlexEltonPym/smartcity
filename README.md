# Smart City Data Analysis

This is the code to collect and analyse data from various social media sources for the Smart City project.

## Getting Started

See documentation/fileStructure.txt for directory/file details.

### Prerequisites

1. Add credential file for google translate

2. Add environment variables for twitter trawler

### Installing

1. Install python3
2. Git clone:

```
git clone https://github.com/AlexEltonPym/smartcity.git
```

3. Install any python dependancies you don't have

## Usage

### Running the data collectors

Navigate to relevant folder then run:

**Twitter** trawler:

```
python3 twitter.py
```

**News** trawler:

*note only brisbane times and syndey morning herald supported*
*note this script will automatically backup the last run*
*note this script will automatically run the data anlysis*

```
./autoRip.sh
```

### Running the data analysers

*all analysers that translate text require google api credentials*

Navigate to relevant folder then run:

**Twitter** analyser:

*make sure you set the relevant twitter data file to analyse*

*requires twitter api credentials*

```
python3 twitterAnalysis.py
```

**Sachin's Twitter** analyser:

```
python3 twitterAnalysis.py
```

**Manual News** analyser:

```
python3 newsAnalysis.py
```

**Trawler News** analyser:

*note this is automatically run during autorun.sh*

```
python3 autoNewsAnalysis.py
```

**Sachin's Facebook** analyser:

```
python3 fbAnalysis.py
```

### Running the data visualisers

*make sure you setup which data, clusters and colours you want to use*

Navigate to top of file structure then run a local server:

```
python3 -m http.server 8080
```

Navigate, in your browser, to:

```
http://localhost:8080/visualisations/sentimentScatter.html

or

http://localhost:8080/visualisations/sentimentScatterWithTopic.html
```
## Updating data andd queries

### Manually adding news articles

Add articles to end of news.txt with following format:

```
TITLE: Article title here

SOURCE: Newspaper name here

URL: www.articleURL.com/here

First paragraph

Second paragraph

Third paragraph

COMMENTS:

First user comment (optional)

Second user comment (optional)

Third user comment (optional)

TITLE: Next article...
```

### Adding urls for news trawling

*note only brisbane times and sydney morning herald are supported*

Add urls to end of urls.txt:

```
https://www.smh.com.au/politics/nsw
https://www.smh.com.au/national/nsw
https://www.smh.com.au/politics/queensland
https://www.smh.com.au/national/queensland
https://www.brisbanetimes.com.au/politics/queensland
https://www.brisbanetimes.com.au/national/queensland
https://www.brisbanetimes.com.au/politics/nsw
https://www.brisbanetimes.com.au/national/nsw

```

*This will search any articles will links from those pages which are subdomains of those urls*

### Adding queries for news trawling

Add queries to newsTidy.py:

```
queries = [
	['westconnex', 'parramatta road'], #parramatta road queries
	['five dock'], 	#five dock queries
	['cronulla park', 'logan'], #cronulla park queries
	['yarrabilba', 'cedargrove', 'treatment plant', 'springwood', 'logan'] #yarrabilba queries
]
```

*Any articles with text that matches a query will be kept and added to the major topic (parramatta road, five dock, cronulla park and yarrabilba)*

### Adding queries for twitter trawling

Add queries to queries file, one query per line.

```
parramatta road
five dock
yarrabilba
cronulla park
```

### Additonal information

## Authors

* **Alex Elton-Pym** - *Repository owner*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is the intellectual property of The Univeristy of Sydney. See their copywrite information for licensing.