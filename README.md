# About
The following project is used to scrape tweets using the Twitter API to run a sentiment analysis on a given query. 
In this repository, the file titled Official Scraper and Necessary Functions are used to create a dataset. When 
completed, the full dataset will be posted to Kaggle.com.

# Visualization
Visualization is currently in process and can be viewed here:
https://tabsoft.co/3yQGNGT

# How are sentiments calculated?
TextBlob is used to conduct the sentiment analysis in Python.

### AFINN 
The AFINN lexicon was used to calculate sentiments (added 6/12) to further test accuracy of alternate lexicons.
This process is done using R, and can be seen in the "AFINNLexicon.R" file. Tweets were tokenized by single words, stopwords were removed, and the scores were assigned.
Scores per day were averaged and then compared. 

Alternate lexicons may be explored in later versions. In addition, bigrams and trigrams will be explored later on.

# Disclaimers
It's important to note that API keys are not included in the repository for privacy reasons.
I am proud to say that all code is original. With that being said, I am learning more everyday and I understand that the process I chose may not be the most efficient or effective.

Thank you for reading!