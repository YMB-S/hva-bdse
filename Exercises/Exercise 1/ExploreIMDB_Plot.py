import pandas as pd 
# more ugly df= pd.read_csv('IMDb movies.csv')
df= pd.read_csv('IMDb movies.csv',sep=',')

df.head(5)

import matplotlib.pyplot as plt
import plotly.express as px



df[['duration']].mean()


# alleen USA
dfUSA=(
    df
    .loc[lambda df: df['country'] == 'USA']
)
dfUSA.head()

# lengte van film titels
print(df.title.str.len().sort_values(ascending=False))

print(df['title'].str.len().sort_values(ascending=False))

df['title'].loc[47063]

# Note Next line  gives an error, dataframe instead of column
print(df[['title']].str.len().sort_values(ascending=False))

new=df.groupby(['duration'], as_index=False).mean()
new.info()

plt.plot(new.duration,new.avg_vote)

fig = px.line(new, x='duration', y='avg_vote')
fig.show()

df.head(10)

dfnew=df

dfnew=df[['year','title']].groupby('year').count()

dfToPlot=dfnew.sort_values('title', ascending=False).head(10)


plt.figure(figsize=(15,10))
dfToPlot.plot.bar()
plt.xticks(rotation=50)
plt.xlabel('Year')
plt.ylabel('Total amount of movies')
plt.show()


fig = px.bar(dfToPlot
              ,x='year'
              ,y='title'
              ,labels={'nummer of movies'}
              ,title='Overview')

fig.show()

fig = px.bar(dfToPlot
              ,x=dfToPlot.index
              ,y='title'
              ,labels={'nummer of movies'}
              ,title='Overview'
              ,width=350
              ,height=300)
fig.update_layout(
              xaxis_showticklabels=True
              ,xaxis_type='category'
              ,xaxis_tickangle=-45
              ,font_family="Courier New"
              ,font_size=5)

fig.show()
