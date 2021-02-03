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

mostvotes = df.sort_values(['votes'], ascending=False)

print(mostvotes['title'].head(5))


avg_votes = (
    df
    .sort_values(['avg_vote'], ascending=True)
)

print(avg_votes[['title', 'avg_vote']].head(20))


df.count()

print(df.title.str.len().sort_values(ascending=False))

print(df['title'].str.len().sort_values(ascending=False))
# Note line 35 gives an error, dataframe instead of column
print(df[['title']].str.len().sort_values(ascending=False))

# wrong coding don disconnect x and y 
y_data = df.loc[:, ['avg_vote']].head(1000) 
x_data = df.loc[:, ['votes']].head(1000)

plt.title('Score in relation to votes') 
plt.xlabel('Votes') 
plt.ylabel('Average Vote') 
plt.scatter(x_data, y_data) 
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
plt.xscale('log') 
plt.show()

dfToPlot = df[['votes', 'avg_vote']].head(1000)

plt.title('Score in relation to votes') 
plt.xlabel('Votes') 
plt.ylabel('Average Vote') 
plt.scatter(dfToPlot['votes'], dfToPlot['avg_vote']) 
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
plt.xscale('log') 
plt.show()

