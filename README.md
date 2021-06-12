# About
The following project is used to scrape tweets using the Twitter API to run a sentiment analysis on tweets about Bitcoin. 
In this repository, the file titled Official Scraper and Necessary Functions are used to create a dataset. When 
completed, the full dataset will be posted to Kaggle.com.

### Questions to answer
Are bitcoin price and sentiment correlated?
How does geographic location affect sentiment?
Can sentiment predict price?

All of these questions will attempt to be answered as more data are collected.

# Visualization
Visualization is currently in process and can be viewed here:
https://tabsoft.co/3yQGNGT

A more indepth dashboard will be added after a few months worth of data is compiled.

# How are sentiments calculated?
Python and R are both utilized; however, more 'intense' lexicons are applied with R, mainly just due to user comfort.

### TextBlob
TextBlob is used to conduct the sentiment analysis in Python. Two scores are created, polarity (how positive or negative the string is) and subjectivity (literally how subjective the string is).
For the purpose of this project, polarity is the main focus.

### AFINN 
The AFINN lexicon was used to calculate sentiments (added 6/12) to further test accuracy of alternate lexicons.
This process is done using R, and can be seen in the "AFINNLexicon.R" file. Tweets were tokenized by single words, stopwords were removed, and the scores were assigned.
Scores per day were averaged and then compared. 

Alternate lexicons may be explored in later versions. In addition, bigrams and trigrams will be explored later on.

# Disclaimers
It's important to note that API keys are not included in the repository for privacy reasons.
I am proud to say that all code is original. With that being said, I am learning more everyday and I understand that the process I chose may not be the most efficient or effective.
In addition, take the number of commits with a grain of salt. I use github more of a cloud than its true purpose, so I tend to make a bunch of commits as a way to back up my work.
Thank you for reading!