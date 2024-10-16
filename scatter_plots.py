import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))

# Using a `scatter plot`, let's visualize the trend of total
# immigration to Canada (all countries combined) for the years 1980 - 2013.

# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))
print(df_tot)
# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ["year", "total"]

# view the final dataframe
print(df_tot.head())

# plot the data:
df_tot.plot(kind="scatter", x="year", y="total", figsize=(10, 6), color="darkblue")

plt.title("Total Immigration to Canada from 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of Immigrants")

plt.show()

# Lets plot a line of best fit and try to predict for 2015

x = df_tot["year"]  # year on x-axis
y = df_tot["total"]  # total on y-axis
fit = np.polyfit(x, y, deg=1)

df_tot.plot(kind="scatter", x="year", y="total", figsize=(10, 6), color="darkblue")

plt.title("Total Immigration to Canada from 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of Immigrants")

# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color="red")  # recall that x is the Years
plt.annotate("y={0:.0f} x + {1:.0f}".format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# print out the line of best fit
"No. Immigrants = {0:.0f} * Year + {1:.0f}".format(fit[0], fit[1])

#
# Question: Create a scatter plot of the total immigration from Denmark,
#  Norway, and Sweden to Canada from 1980 to 2013?

# create df_countries dataframe
df_countries = df_can.loc[["Denmark", "Norway", "Sweden"], years].transpose()

# create df_total by summing across three countries for each year
df_total = pd.DataFrame(df_countries.sum(axis=1))

# reset index in place
df_total.reset_index(inplace=True)

# rename columns
df_total.columns = ["year", "total"]

# change column year from string to int to create scatter plot
df_total["year"] = df_total["year"].astype(int)

# show resulting dataframe
print(df_total.head())

# generate scatter plot
df_total.plot(kind="scatter", x="year", y="total", figsize=(10, 6), color="darkblue")

# add title and label to axes
plt.title("Immigration from Denmark, Norway, and Sweden to Canada from 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of Immigrants")

# show plot
plt.show()
