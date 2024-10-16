import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)
print(df_can.head())

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

print("Matplotlib version: ", mpl.__version__)
print(plt.style.available)
mpl.style.use(["ggplot"])  # optional: for ggplot-like style

haiti = df_can.loc[
    "Haiti", years
]  # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

haiti.index = haiti.index.map(int)
# haiti.plot(kind="line")

# plt.title("Immigration from Haiti")
# plt.ylabel("Number of immigrants")
# plt.xlabel("Years")
# annotate the 2010 Earthquake.
# syntax: plt.text(x, y, label)
# plt.text(2000, 6000, "2010 Earthquake")
# plt.show()  # need this line to show the updates made to the figure

df_CI = df_can.loc[
    ["China", "India"], years
]  # passing in years 1980 - 2013 to exclude the 'total' column
print(df_CI)
df_CI = df_CI.transpose()
print(df_CI.head())

# df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
# df_CI.plot(kind='line')

# plt.title('Immigrants from China and India')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')

# plt.show()

# **Question:** Compare the trend of top 5 countries that contributed the most to immigration to Canada.
df_can.sort_values(by="Total", ascending=False, axis=0, inplace=True)
df_top5 = df_can.head(5)

df_top5 = df_top5[years].transpose()
df_top5.rename(
    columns={"United Kingdom of Great Britain and Northern Ireland": "UK"}, inplace=True
)
print(df_top5)
df_top5.index = df_top5.index.map(
    int
)  # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind="line", figsize=(14, 8))  # pass a tuple (x, y) size
plt.title("Immigration Trend of Top 5 Countries")
plt.ylabel("Number of Immigrants")
plt.xlabel("Years")
plt.show()
