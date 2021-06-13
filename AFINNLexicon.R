# Packages
library(readr)
library(tidyverse)
library(tidytext)
library(gridExtra)
library(grid)
library(igraph)
library(ggraph)
library(widyr)
library(SnowballC)
library(readr)

link = 'https://raw.githubusercontent.com/jvit1/sentimentanalysis/main/Scraped_Tweets.csv'
data <- read_csv(url(link))


# Tokenizes and removes stopwords. 
review.words <- data %>%
  select(Text, `BTC Price`, Date) %>%
  unnest_tokens(word, Text) %>%
  mutate(word = str_extract(word, "[0-9a-z']+")) %>%
  drop_na()

review.words$word <- sapply(review.words$word, removeNumbers)

review.words <- review.words %>%
  anti_join(stop_words)


# Summarizes by count.
review.words %>% group_by(word) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

# For now, we'll use the AFINN lexicon because we want a quantitative value. 
# We average out the scores by date. This will be what we can graph from.

afinn.sent <- get_sentiments("afinn")

sentiments <- review.words %>%
  inner_join(afinn.sent)

sentiments$Date <- as.Date(sentiments$Date)

final.table <- sentiments %>% select(`BTC Price`, Date, value) %>%
  group_by(Date, `BTC Price`) %>% summarize(score = mean(value))


write.csv(final.table,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Data/AFINNLexicon.csv", row.names = FALSE)

# Let's also get a csv of most common words (for graphic purposes).
word.totals <- review.words %>% group_by(word) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

write.csv(word.totals,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Data/wordtotals.csv", row.names = FALSE)

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

###############################################################################
new_stop_words <- tibble(word.stem = c("bitcoin", "btc", ""))

test <- bigrams %>%
  separate(bigram, c("word1", "word2"), sep= ' ') %>%
  filter(!word1 %in% new_stop_words) %>%
  filter(!word2 %in% new_stop_words) %>%
  unite(bigram, word1, word2, sep = " ")
###################### Bigram word removal is not working #####################
################### FIX THIS ASAP #######################

bigram.count <- bigrams %>%
  group_by(bigram) %>%
  summarize(count = n()) %>%
  arrange(desc(count))


bigram.count %>%
  top_n(15, count) %>%
  mutate(bigram = reorder(bigram, count)) %>%
  ggplot(aes(x = bigram, y = count)) + 
  geom_col() + 
  coord_flip()
