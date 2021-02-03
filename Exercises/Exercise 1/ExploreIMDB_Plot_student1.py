import pandas as pd 
# more ugly df= pd.read_csv('IMDb movies.csv')
df= pd.read_csv('IMDb movies.csv',sep=',')

import matplotlib.pyplot as plt

dfToPlot=df[['title','year']].groupby('year')

plt.figure(figsize=(15,10))
dfToPlot.size().sort_values(ascending=False).head(10).plot.bar()
plt.xticks(rotation=50)
plt.xlabel('Year')
plt.ylabel('Total amount of movies')
plt.show()

#films per jaar
df1 = (
    df
    .groupby('year')
    .count()
)

#kortste films
df2 = (
    df
    .sort_values ('duration')
)

#de allerbeste films
df3 = (
    df
   .sort_values(['votes', 'avg_vote'], ascending=[False, True])
)
dfJC = df[df['actors'].str.contains("Jackie Chan")==True].sort_values(['reviews_from_users'])

dfFloris=(
    df
    .groupby(['year'])
    .agg({
        'duration':['mean']
        })
    .sort_values('year', ascending=False)
    .head(10)
)

(
df
.loc[:,['year','avg_vote', 'title','country']]
.loc[lambda df: df ['year']<= 2000]
.sort_values('avg_vote', ascending = False)
.head(20)
)

(
df[['year','avg_vote', 'title','country']]
.loc[lambda df: df ['year']<= 2000]
.sort_values('avg_vote', ascending = False)
.head(20)
)

