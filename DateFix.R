#Opening and reformatting tweets from today
path <- "C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/TimeStamped/Tweets_"
date.today <- format(Sys.Date(), "%m_%d_%Y")
data.today <- read.csv(paste(path, date.today, ".csv", sep = ""))
data.today$Date <- as.Date(data.today$Date)

#Adding to combined csv
total <- read.csv("C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Scraped_Tweets.csv", header = T)
total$Date <- as.Date(total$Date, "%m/%d/%Y")
colnames(total)[colnames(total) == "Unnamed..0"] <- "X"

scraped.tweets <- rbind(total, data.today)
write.csv(scraped.tweets,"C:/Users/student/Documents/UVA/Portfolio Projects/Sentiment Analysis/sentimentanalysis/Scraped_Tweets.csv", row.names = FALSE)