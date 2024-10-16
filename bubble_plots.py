import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))

# A bubble plot is a variation of the scatter plot that displays three dimensions of data (x, y, z).
# The data points are replaced with bubbles, and the size of the bubble is determined by the third variable z,
# also known as the weight. In maplotlib, we can pass in an array or scalar to the parameter s to plot(),
# that contains the weight of each point.

# Let's start by analyzing the effect of Argentina's great depression.
# Argentina suffered a great depression from 1998 to 2002, which caused widespread unemployment,
# riots, the fall of the government, and a default on the country's foreign debt. In terms of income,
# over 50% of Argentines were poor, and seven out of ten Argentine children were poor at the depth of
# the crisis in 2002.
# Let's analyze the effect of this crisis, and compare Argentina's immigration to that of it's neighbour Brazil.
# Let's do that using a bubble plot of immigration from Brazil and Argentina for the years 1980 - 2013.
# We will set the weights for the bubble as the normalized value of the population for each year.

# transposed dataframe
df_can_t = df_can[years].transpose()

# cast the Years (the index) to type int
df_can_t.index = map(int, df_can_t.index)

# let's label the index. This will automatically be the column name when we reset the index
df_can_t.index.name = "Year"

# reset index to bring the Year in as a column
df_can_t.reset_index(inplace=True)

# view the changes
print(df_can_t.head())

# normalize Brazil data
norm_brazil = (df_can_t["Brazil"] - df_can_t["Brazil"].min()) / (
    df_can_t["Brazil"].max() - df_can_t["Brazil"].min()
)

# normalize Argentina data
norm_argentina = (df_can_t["Argentina"] - df_can_t["Argentina"].min()) / (
    df_can_t["Argentina"].max() - df_can_t["Argentina"].min()
)
# Brazil
ax0 = df_can_t.plot(
    kind="scatter",
    x="Year",
    y="Brazil",
    figsize=(14, 8),
    alpha=0.5,  # transparency
    color="green",
    s=norm_brazil * 2000 + 10,  # pass in weights
    xlim=(1975, 2015),
)

# Argentina
ax1 = df_can_t.plot(
    kind="scatter",
    x="Year",
    y="Argentina",
    alpha=0.5,
    color="blue",
    s=norm_argentina * 2000 + 10,
    ax=ax0,
)

ax0.set_ylabel("Number of Immigrants")
ax0.set_title("Immigration from Brazil and Argentina from 1980 to 2013")
ax0.legend(["Brazil", "Argentina"], loc="upper left", fontsize="x-large")
plt.show()

# Repeat for China & India
# normalized Chinese data
norm_china = (df_can_t["China"] - df_can_t["China"].min()) / (
    df_can_t["China"].max() - df_can_t["China"].min()
)
# normalized Indian data
norm_india = (df_can_t["India"] - df_can_t["India"].min()) / (
    df_can_t["India"].max() - df_can_t["India"].min()
)

# China
ax0 = df_can_t.plot(
    kind="scatter",
    x="Year",
    y="China",
    figsize=(14, 8),
    alpha=0.5,  # transparency
    color="green",
    s=norm_china * 2000 + 10,  # pass in weights
    xlim=(1975, 2015),
)

# India
ax1 = df_can_t.plot(
    kind="scatter",
    x="Year",
    y="India",
    alpha=0.5,
    color="blue",
    s=norm_india * 2000 + 10,
    ax=ax0,
)

ax0.set_ylabel("Number of Immigrants")
ax0.set_title("Immigration from China and India from 1980 - 2013")
ax0.legend(["China", "India"], loc="upper left", fontsize="x-large")
plt.show()
