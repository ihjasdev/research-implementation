import pandas as pd

#create DataFrame
df = pd.DataFrame({'team' : ['Mavs$', 'Nets', 'Kings!!', 'Spurs%', '&Heat&'],
                   'points' : [12, 15, 22, 29, 24]})

#view DataFrame
print(df)
#remove special characters from team column
df['team'] = df['team'].str.replace('\W', '', regex=True)

#view updated DataFrame
print(df)