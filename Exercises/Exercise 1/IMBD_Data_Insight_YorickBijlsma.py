'''
we have to answer the following questions:
    -how many rows are in the dataframe?
    -how many columns?
    -what is the mean duration of all movies?
    -how many movies with country='USA' are there?
    -what is the title with the most characters in it?

then plot a chart listing the number of movies per year
'''

import pandas as pd
import matplotlib.pyplot as plt
frame = pd.read_csv('IMDb movies.csv',sep=',')

#get all the necessary data
numRows = len(frame)
numColumns = len(frame.columns)
meanDuration = frame["duration"].mean()
usaMovies = frame["country"].value_counts()["USA"]
titleFrame = frame.reindex((-frame["title"].str.len()).argsort()).reset_index(drop=True)
longestMovieTitle=titleFrame.iloc[0]["title"]

#print it out for display
print("Number of rows: " + str(numRows))
print("Number of columns: " + str(numColumns))
print("Mean duration: " + str(meanDuration))
print("USA count: " + str(usaMovies))
print("Longest title: " + longestMovieTitle)

#we want to plot the years by amount of movies released that year
frame["year"].value_counts().plot(kind="bar")

#show the entire frame
plt.show()