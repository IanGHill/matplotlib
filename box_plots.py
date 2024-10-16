import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))

# Let's plot the box plot for the Japanese immigrants between 1980 - 2013.

# to get a dataframe, place extra square brackets around 'Japan'.
df_japan = df_can.loc[["Japan"], years].transpose()
print(df_japan.head())

df_japan.plot(kind="box", figsize=(8, 6))

plt.title("Box plot of Japanese Immigrants from 1980 - 2013")
plt.ylabel("Number of Immigrants")

plt.show()
# Use describe to get the actual numbers
print(df_japan.describe())

# Question: Compare the distribution of the number of new immigrants
# from India and China for the period 1980 - 2013.

df_CI = df_can.loc[["China", "India"], years].transpose()
print(df_CI.head())
df_CI.plot(kind="box", figsize=(8, 6))

plt.title("Box plot of Immigrants from China and India for years 1980 - 2013")
plt.ylabel("Number of Immigrants")

plt.show()

# horizontal box plots
df_CI.plot(kind="box", figsize=(10, 7), color="blue", vert=False)

plt.title("Box plots of Immigrants from China and India (1980 - 2013)")
plt.xlabel("Number of Immigrants")

plt.show()
# **Subplots**Often times we might want to plot multiple plots within the same figure.
# For example, we might want to perform a side by side comparison of the box plot with the
# line plot of China and India's immigration. To visualize multiple plots together,
# we can create a **`figure`** (overall canvas) and divide it into **`subplots`**, each containing a plot.
# With **subplots**, we usually work with the **artist layer** instead of the **scripting layer**.

fig = plt.figure()  # create figure

ax0 = fig.add_subplot(1, 2, 1)  # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(
    1, 2, 2
)  # add subplot 2 (1 row, 2 columns, second plot). See tip below**

# Subplot 1: Box plot
df_CI.plot(
    kind="box", color="blue", vert=False, figsize=(20, 6), ax=ax0
)  # add to subplot 1
ax0.set_title("Box Plots of Immigrants from China and India (1980 - 2013)")
ax0.set_xlabel("Number of Immigrants")
ax0.set_ylabel("Countries")

# Subplot 2: Line plot
df_CI.plot(kind="line", figsize=(20, 6), ax=ax1)  # add to subplot 2
ax1.set_title("Line Plots of Immigrants from China and India (1980 - 2013)")
ax1.set_ylabel("Number of Immigrants")
ax1.set_xlabel("Years")

plt.show()

# Create a box plot to visualize the distribution of the top 15 countries
# (based on total immigration) grouped by the decades 1980s, 1990s, and 2000s.

df_top15 = df_can.sort_values(["Total"], ascending=False, axis=0).head(15)
# create a list of all years in decades 80's, 90's, and 00's
years_80s = list(map(str, range(1980, 1990)))
years_90s = list(map(str, range(1990, 2000)))
years_00s = list(map(str, range(2000, 2010)))

# slice the original dataframe df_can to create a series for each decade
df_80s = df_top15.loc[:, years_80s].sum(axis=1)
df_90s = df_top15.loc[:, years_90s].sum(axis=1)
df_00s = df_top15.loc[:, years_00s].sum(axis=1)

# merge the three series into a new data frame
new_df = pd.DataFrame({"1980s": df_80s, "1990s": df_90s, "2000s": df_00s})

# display dataframe
print(new_df.head())
new_df.plot(kind="box", figsize=(10, 6))

plt.title("Immigration from top 15 countries for decades 80s, 90s and 2000s")

plt.show()

print(new_df.describe())
# Note how the box plot differs from the summary table created. The box plot scans the data
# and identifies the outliers. In order to be an outlier, the data value must be:

# larger than Q3 by at least 1.5 times the interquartile range (IQR), or,
# smaller than Q1 by at least 1.5 times the IQR.
# Let's look at decade 2000s as an example:

# Q1 (25%) = 36,101.5
# Q3 (75%) = 105,505.5
# IQR = Q3 - Q1 = 69,404
# Using the definition of outlier, any value that is greater than Q3 by 1.5 times IQR will be flagged as outlier.

# Outlier > 105,505.5 + (1.5 * 69,404)
# Outlier > 209,611.5

# let's check how many entries fall above the outlier threshold
new_df = new_df.reset_index()
print(new_df[new_df["2000s"] > 209611.5])

# China and India are both considered as outliers since their population for the decade exceeds 209,611.5.
#   Country  1980s   1990s   2000s
# 0   India  82154  180395  303591 <---
# 1   China  32003  161528  340385 <---
