# Websearch-cli
## A forensic-oriented tool with Google cheatsheet
> before the use, install with `install.sh`
---
usage: google [-h] [-q QUERY [QUERY ...]] [-s STRICT [STRICT ...]]
              [-n NO_WORD [NO_WORD ...]] [--from-to FROMTO [FROMTO ...]]
              [-p {EUR,USD}] [-u USERNAME [USERNAME ...]]
              [-H HASHTAG [HASHTAG ...]] [-c CONVERT [CONVERT ...]]
              [-S SITE [SITE ...]] [-nS NO_SITE [NO_SITE ...]] [-C CACHE]
              [-f TYPE] [-d DEFINE] [-w WEATHER] [-m MAP] [-a AROUND]
              [-qt IN_TEXT [IN_TEXT ...]] [-qT IN_TITLE [IN_TITLE ...]]
              [-qu IN_URL [IN_URL ...]]

Search in google from CLI

options:
  -h, --help            show this help message and exit
  -q QUERY [QUERY ...]  Search query
  -s STRICT [STRICT ...], --strict STRICT [STRICT ...]
                        Set strict mode for words
  -n NO_WORD [NO_WORD ...], --no-word NO_WORD [NO_WORD ...]
                        Prohibite words
  --from-to FROMTO [FROMTO ...]
                        Define an interval
  -p {EUR,USD}, --price {EUR,USD}
                        Show price of product in USD or EUR
  -u USERNAME [USERNAME ...], --username USERNAME [USERNAME ...]
                        Search username
  -H HASHTAG [HASHTAG ...], --hashtag HASHTAG [HASHTAG ...]
                        Find almost one of the hashtag
  -c CONVERT [CONVERT ...], --convert CONVERT [CONVERT ...]
                        Convert a misure into another
  -S SITE [SITE ...], --in-site SITE [SITE ...]
                        Search in a site
  -nS NO_SITE [NO_SITE ...], --no-site NO_SITE [NO_SITE ...]
                        Don't search on that site
  -C CACHE, --cache CACHE
                        Search inside the website cache
  -f TYPE, --filetype TYPE
                        Specify the file type
  -d DEFINE, --define DEFINE
                        Define a word
  -w WEATHER, --weather WEATHER
                        Search for the weather in a specified city
  -m MAP, --map MAP     Search for a locality
  -a AROUND, --query-around AROUND
                        Set the around value for query
  -qt IN_TEXT [IN_TEXT ...], --in-text IN_TEXT [IN_TEXT ...]
                        Search a word or a phrase into sites text
  -qT IN_TITLE [IN_TITLE ...], --in-title IN_TITLE [IN_TITLE ...]
                        Search a word or a phrase into sites url
  -qu IN_URL [IN_URL ...], --in-url IN_URL [IN_URL ...]
                        Search a word or a phrase into sites url