import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

mpl.style.use(["ggplot"])  # optional: for ggplot-like style

df_can.sort_values(["Total"], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head()

# transpose the dataframe
df_top5 = df_top5[years].transpose()
df_top5.rename(
    columns={"United Kingdom of Great Britain and Northern Ireland": "UK"}, inplace=True
)

print(df_top5.head())

# Area plots are stacked by default. And to produce a stacked area plot,
# each column must be either all positive or all negative values
# (any `NaN`, i.e. not a number, values will default to 0). To produce
# an unstacked plot, set parameter `stacked` to value `False`.

# let's change the index values of df_top5 to type integer for plotting
df_top5.index = df_top5.index.map(int)
# df_top5.plot(kind="area", stacked=False, figsize=(20, 10))  # pass a tuple (x, y) size

# plt.title("Immigration Trend of Top 5 Countries")
# plt.ylabel("Number of Immigrants")
# plt.xlabel("Years")

# plt.show()

# The unstacked plot has a default transparency (alpha value) at 0.5. We can modify this value by passing
# in the `alpha` parameter.
df_top5.plot(
    kind="area",
    alpha=0.25,  # 0 - 1, default value alpha = 0.5
    stacked=False,
    figsize=(20, 10),
)

plt.title("Immigration Trend of Top 5 Countries")
plt.ylabel("Number of Immigrants")
plt.xlabel("Years")

plt.show()
