library(ecospace)
setwd('C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/TimeStamped/')

# Formatting today's tweets
path <- "C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/TimeStamped/Tweets_"
date.today <- format(Sys.Date(), "%m_%d_%Y")
data.today <- read.csv(paste(path, date.today, ".csv", sep = ""))
data.today$Date <- as.Date(data.today$Date)
write.csv(data.today, paste(path, date.today, ".csv", sep = ""), row.names = FALSE)


all.tweets <- lapply(Sys.glob("Tweets*.csv"), read.csv)
all.tweets <- rbind_listdf(lists = all.tweets, seq.by = 100)
write.csv(all.tweets,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Scraped_Tweets.csv", row.names = FALSE)

