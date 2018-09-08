# Smart City Data Analysis

This is the code to collect and analyse data from various social media sources for the Smart City project.

## Getting Started

See documentation/fileStructure.txt for directory/file details.

### Prerequisites

Add credential file for google translate
Add environment variables for twitter trawler

### Installing

1. Install python3
2. Git clone:

```
git clone https://github.com/AlexEltonPym/smartcity.git
```

3. Install any python dependancies you don't have

### Usage

## Running the data collectors

Navigate to relevant folder then run:

**Twitter** trawler:

```
python3 twitter.py
```

**News** trawler:

*note only brisbane times and syndey morning herald supported*

```
./autoRip.sh
python3 newsTidy.py
```

## Running the data analysers

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

```
python3 autoNewsAnalysis.py
```

**Sachin's Facebook** analyser:

```
python3 fbAnalysis.py
```

## Running the data visualisers

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

## Manually adding news articles

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

### Additonal information

## Authors

* **Alex Elton-Pym** - *Repository owner*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is the intellectual property of The Univeristy of Sydney. See their copywrite information for licensing.