import snscrape.modules.twitter as sntwitter
import pandas as pd
import openpyxl
import xlsxwriter


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

print(df)
print("-------------Converting into xlsx file----------")
df.to_excel(r'C:\Users\icom\Desktop\newfile.xlsx', index=False)