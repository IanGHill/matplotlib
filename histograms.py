import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

mpl.style.use(["ggplot"])  # optional: for ggplot-like style

# np.histogram returns 2 values
count, bin_edges = np.histogram(df_can["2013"])

print(count)  # frequency count
print(bin_edges)  # bin ranges, default = 10 bins

# 'bin_edges' is a list of bin intervals
# count, bin_edges = np.histogram(df_can["2013"])

# df_can["2013"].plot(kind="hist", figsize=(8, 5), xticks=bin_edges)

# plt.title(
#     "Histogram of Immigration from 195 countries in 2013"
# )  # add a title to the histogram
# plt.ylabel("Number of Countries")  # add y-label
# plt.xlabel("Number of Immigrants")  # add x-label

# plt.show()

# *Question*: What is the immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013?
print(df_can.loc[["Denmark", "Norway", "Sweden"], years])
# transpose dataframe
df_t = df_can.loc[["Denmark", "Norway", "Sweden"], years].transpose()
print(df_t.head())

# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)

# un-stacked histogram
df_t.plot(
    kind="hist",
    figsize=(10, 6),
    bins=15,
    alpha=0.6,
    xticks=bin_edges,
    color=["coral", "darkslateblue", "mediumseagreen"],
)

plt.title("Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013")
plt.ylabel("Number of Years")
plt.xlabel("Number of Immigrants")

plt.show()

# Stacked Histogram
count, bin_edges = np.histogram(df_t, 15)
xmin = (
    bin_edges[0] - 10
)  #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes
xmax = (
    bin_edges[-1] + 10
)  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

# stacked Histogram
df_t.plot(
    kind="hist",
    figsize=(10, 6),
    bins=15,
    xticks=bin_edges,
    color=["coral", "darkslateblue", "mediumseagreen"],
    stacked=True,
    xlim=(xmin, xmax),
)

plt.title("Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013")
plt.ylabel("Number of Years")
plt.xlabel("Number of Immigrants")

plt.show()
