library(ecospace)

setwd('C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/TimeStamped/')

# Formatting today's tweets
path <- "C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/TimeStamped/Tweets_"
date.today <- format(Sys.Date(), "%m_%d_%Y")
data.today <- read.csv(paste(path, date.today, ".csv", sep = ""), header =TRUE)

data.today$Date <- format(as.Date(data.today$Date, format = "%Y-%m-%d"), "%m/%d/%Y")
write.csv(data.today, paste(path, date.today, ".csv", sep = ""), row.names = FALSE)


all.tweets <- lapply(Sys.glob("Tweets*.csv"), read.csv)
all.tweets <- rbind_listdf(lists = all.tweets, seq.by = 100)
all.tweets$Date <- format(as.Date(all.tweets$Date, format = "%m/%d/%Y"))


write.csv(all.tweets,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Scraped_Tweets.csv", row.names = FALSE)
print("Complete!")
