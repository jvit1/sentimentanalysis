def spam_filter(df):
    df = tweets_df[~tweets_df[2].str.contains("RT")]
    df = df[~(df[4] <= 100)]  # Making sure total followers is greater than 100
    df = df[~(df[11] <= 100)]  # Making sure total account likes is greater than 100
    df = df[(df[10] == False)]  # Making sure there is a real profile pic
    return df