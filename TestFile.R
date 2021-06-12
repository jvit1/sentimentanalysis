#Packages
library(readr)
library(tidyverse)
library(tidytext)
library(gridExtra)
library(grid)
library(igraph)
library(ggraph)
library(widyr)
library(SnowballC)

data <- read.csv("Scraped_Tweets.csv")

#Tokenizes and removes stopwords. 
review.words <- data %>%
  select(Text, BTC.Price, Date) %>%
  unnest_tokens(word, Text) %>%
  mutate(word = str_extract(word, "[0-9a-z']+")) %>%
  drop_na()

review.words$word <- sapply(review.words$word, removeNumbers)

review.words <- review.words %>%
  anti_join(stop_words)


#Summarizes by count.
review.words %>% group_by(word) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

# For now, we'll use the afinn lexicon becuase we want a quantitatve value. 
# We average out the scores by date. This will be what we can graph from.

afinn.sent <- get_sentiments("afinn")

sentiments <- review.words %>%
  inner_join(afinn.sent)

sentiments$Date <- as.Date(sentiments$Date)

final.table <- sentiments %>% select(BTC.Price, Date, value) %>%
  group_by(Date, BTC.Price) %>% summarize(score = mean(value))


