# Packages
library(readr)
library(tidyverse)
library(tidytext)
library(gridExtra)
library(grid)
library(igraph)
library(ggraph)
library(tm)
library(data.table)
print("Packages attached.")

data <- read.csv("C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Scraped_Tweets.csv", header = T)

# Tokenizes and removes stopwords. 
review.words <- data %>%
  unnest_tokens(word, Text) %>%
  mutate(word = str_extract(word, "[0-9a-z']+")) %>%
  drop_na()

review.words$word <- sapply(review.words$word, removeNumbers)

review.words <- review.words %>%
  anti_join(stop_words)


afinn.sent <- get_sentiments("afinn")

sentiments <- review.words %>%
  inner_join(afinn.sent)

#sentiments$Date <- format(as.Date(sentiments$Date, format = "%Y-%m-%d"), "%m/%d/%Y")

final.table <- sentiments %>% select(BTC.Price, Date, value) %>%
  group_by(Date, BTC.Price) %>% summarize(score = mean(value))

write.csv(sentiments,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Data/LexiconScores.csv", row.names = FALSE)
#################################

# Let's also get a csv of most common words (for graphic purposes).
word.totals <- review.words %>% group_by(word, Date) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

write.csv(word.totals,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Data/TotalWords.csv", row.names = FALSE)

# Bigrams: We'll use the same approach as before.


bigrams <- data %>%
  unnest_tokens(bigram, Text, token = "ngrams", n = 2) %>%
  mutate(bigram = str_extract(bigram, "[0-9a-z'\\s]+")) %>%
  drop_na()

bigrams <- bigrams %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  drop_na() %>%
  unite(bigram, word1, word2, sep = " ") 

## We are going to define some additional stop words to remove. 
##Because we are interested in seeing what else people are talking about, we will remove 'bitcoin'.
##Potential spam word combos will be removed also.

new_stop_words <- as.character(c("bitcoin", "btc", "cryptocurrency",
                                 "passive", "income", "kindly", 
                                 "instagram", "twitter", "facebook", "tiktok",
                                 "message", "pinterest"))


test <- bigrams %>%
  separate(bigram, c("word1", "word2"), sep= ' ') %>%
  filter(!word1 %in% new_stop_words) %>%
  filter(!word2 %in% new_stop_words) %>%
  unite(bigram, word1, word2, sep = " ")

bigram.count <- test %>%
  group_by(bigram, Date) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

write.csv(bigram.count,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Data/TotalBigrams.csv", row.names = FALSE)

print("Complete!")
