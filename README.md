# Smart City Data Analysis

This is the code to collect and analyse data from various social media sources for the Smart City project.

## Getting Started

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

*Note: only brisbane times and syndey morning herald supported*

*Note: this script will automatically backup the last run*

*Note: this script will automatically run the data anlysis*

```
./autoRip.sh
```

### Running the data analysers

*All analysers that translate text require google api credentials*

Navigate to relevant folder then run:

**Twitter** analyser:

*Make sure you set the relevant twitter data file to analyse*

*Requires twitter api credentials*

```
python3 twitterAnalysis.py
```

**Sachin's Twitter** analyser:

```
python3 sTwitterAnalysis.py
```

**Manual News** analyser:

```
python3 newsAnalysis.py
```

**Trawler News** analyser:

*Note this is automatically run during autorun.sh*

```
python3 autoNewsAnalysis.py
```

**Sachin's Facebook** analyser:

```
python3 fbAnalysis.py
```

### Running the data visualisers

*Make sure you setup which data, clusters and colours you want to use*

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
## Updating data and queries

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

*Note: only brisbane times and sydney morning herald are supported*

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

## File structure
```
├── council\ survey\ data
│   └── Cronulla\ Park\ Master\ Plan\ Consultation\ Deidentifie.._.xlsx #not enough data so unused
├── creds.json #google translate credentials, do not publicise
├── facebook
│   ├── facebook\ denial.png #visual proof of denial for permissions
│   ├── fbAnalysis.py #analyses sachin's facebook data -> processedFBData.json and fb-docbyword.csv
│   ├── fb_logan_city.txt #sachin's facebook raw txt file
│   ├── ourApp
│   │   ├── FB\ Submission\ Video.mov #screengrab video used for second facebook submission
│   │   └── index.html #facebook login implementation for permission approval
│   ├── processedFBData.json #json collection of analysed facebook data
│   └── tdm
│       └── fb-docbyword.csv #tdm for sachin's facebook data
├── news
│   ├── manual
│   │   ├── news.txt #manually collected news file
│   │   ├── newsAnalysis.py #manually collected news analyser
│   │   ├── processedNews.json #json collection of analysed manual news data
│   │   └── tdm
│   │       └── news-docbyword.csv #tdm for manually collected news
│   └── trawler
│       ├── articles
│       │   ├─- #contains various downloaded html articles
│       ├── articlesClean #paragraphs extracted from articles matching queries
│       │   ├── cronullaPark.txt 
│       │   ├── fiveDock.txt
│       │   ├── parramattaRoad.txt
│       │   └── yarrabilba.txt
│       ├── autoNewsAnalysis.py #analyses cleaned articles
│       ├── autorip.sh #automatically downloads, cleans and analyses articles
│       ├── newsTidy.py #cleans downloaded articles
│       ├── processedAutoNews.json #json collection of analysed autoripped news
│       ├── tdm #contains tdms for any successful queries
│       └── urls.txt #list of urls to scrape for articles
├── sTwitter
│   ├── data #sachin's raw twitter data
│   │   ├── dock.txt
│   │   ├── logan.txt
│   │   ├── parra.txt
│   │   ├── spring.txt
│   │   └── yara.txt
│   ├── processedSTwitterData.json #json colelction of sachin's twitter data
│   ├── sTwitterAnalysis.py #processes then analyses sachin's raw data
│   └── tdm #tdms for each of sachin's topics
│       ├── sTwitter-dock-docbyword.csv
│       ├── sTwitter-logan-docbyword.csv
│       ├── sTwitter-parra-docbyword.csv
│       └── sTwitter-yara-docbyword.csv
├── twitter
│   ├── processedTwitterData.json #json collection of fresh twitter data
│   ├── tdm #tdms for each query
│   │   ├── cronulla\ park-docbyword.csv
│   │   ├── five\ dock-docbyword.csv
│   │   ├── parramatta\ road-docbyword.csv
│   │   └── yarrabilba-docbyword.csv
│   ├── data #captured twitter data
│   ├── twitter.py #twitter data collector
│   └── twitterAnalysis.py #analyses raw twitter data
└── visualisations
    ├── sentimentScatter.html #plots documents by sentiment and subjectivity
    ├── sentimentScatterWithTopic.html #plots documents by sentiment and subjectivity with topic colouring
```

## Avenues explored

### Facebook

We have applied for public page content access twice. Both times have been rejected:

```
"Your screencast doesn't show how the use of this permission directly improves the user experience in your app. Unfortunately, we also weren't able to determine this from testing your app manually.
All permissions data must be visibly used within your app. We do not accept permission requests for data that you may decide to use later."
```

In summary, because we don't show the data being used in the dashboard, Facebook will not approve collecting data yet.

*We can revisit this once the dashboard is operational. We may need to show a full user interaction and may still be rejected due to recent tightening on Facebooks permission approval.*

Admins of Facebook pages can also download an archive of their page which can be processed for analysis if needed. It is my understanding that this archive does not include user comments.

### Instagram

Instagram, now owned by Facebook, has merged their API with the Facebook Graph API. Therefore the same permission issues apply. We also don't have the ability to analyse images which is the primary data on Instagram. Further, Instagram is typically used for personal use, rather than public opinion like how Twitter is used.

*We can revisit this once the dashboard is operational. We may need to show a full user interaction and may still be rejected due to recent tightening on Facebooks permission approval.*


### Twitter

Sachin has collected 7 years of data for some queries. We believe these queries are:
```
Five Dock
Logan
Parramatta Road
Springwood
Yarrabiliba
```

We also have an automatic pipeline for capturing the past 7 days of data for any given queries. These weekly collections are stored along with their capture timestamp.

We will also do a full historical search using the Premium Twitter API as a once off step.

### Council survey data

Council survey data is too limited to be meaningful at this point. The pipeline can be easily adapted if more of this data becomes available.

### News

Both manually downloaded articles and automatically trawlled articles are available.

Articles from the supported websites can be automatically downloaded, searched for relevant queries and then analysed.

We can also download the content of an article manually for analysis.

Because there are few user comments on these articles the magority of processed data are the paragraphs of the article body.

## Additonal information

### Authors

* **Alex Elton-Pym** - *Repository owner*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

### License

This project is the intellectual property of The Univeristy of Sydney. See their copywrite information for licensing.