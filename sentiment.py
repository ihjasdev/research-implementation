import pandas as pd
from textblob import TextBlob

# read in the dataframe
df = pd.read_csv("test6.csv")

# create a new column in the dataframe to store the sentiment
df["sentiment"] = ""

# iterate over the rows in the dataframe
for index, row in df.iterrows():
  # get the text from the row
  text = row["text"]
  
  # create a TextBlob object and get the sentiment
  text_blob = TextBlob(text)
  sentiment = text_blob.sentiment
  
  # store the sentiment in the dataframe
  df.at[index, "sentiment"] = sentiment

# print the updated dataframe
print(df)