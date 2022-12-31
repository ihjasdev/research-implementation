import snscrape.modules.twitter as sntwitter
import pandas as pd
import openpyxl
import xlsxwriter
import re


query ="(from:elonmusk) until:2021-07-20 since:2021-01-17"
tweets=[]
limit =100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets)== limit:
     break
    else:
        tweets.append([tweet.user.username,tweet.content])

df=pd.DataFrame(tweets, columns=['User','Tweet'])
#remove special charecters

df['Tweet'] = df['Tweet'].str.replace('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', regex=True)

df['Tweet'] = df['Tweet'].str.replace('\W', ' ', regex=True)
print(df)
print("-------------Converting into xlsx file----------")
df.to_csv(r'test6.csv', index=False)




