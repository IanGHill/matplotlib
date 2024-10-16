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

# Vertical bar chart

# Question: Compare the number of Icelandic immigrants (country = 'Iceland')
# to Canada from year 1980 to 2013.

df_iceland = df_can.loc["Iceland", years]
print(df_iceland.head())

df_iceland.plot(kind="bar", figsize=(10, 6), rot=90)

plt.xlabel("Year")
plt.ylabel("Number of Immigrants")
plt.title("Icelandic Immigrants to Canada from 1980 to 2013")

# Annotate arrow
plt.annotate(
    "",  # s: str. will leave it blank for no text
    xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
    xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
    xycoords="data",  # will use the coordinate system of the object being annotated
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="blue", lw=2),
)

# Annotate Text
plt.annotate(
    "2008 - 2011 Financial Crisis",  # text to display
    xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
    rotation=72.5,  # based on trial and error to match the arrow
    va="bottom",  # want the text to be vertically 'bottom' aligned
    ha="left",  # want the text to be horizontally 'left' algned.
)

plt.show()

# Create a horizontal bar plot showing the *total* number of immigrants
# to Canada from the top 15 countries, for the period 1980 - 2013. Label each country with the total immigrant count.

df_can.sort_values(by="Total", ascending=True, inplace=True)

df_can.rename(
    index={"United Kingdom of Great Britain and Northern Ireland": "UK"}, inplace=True
)
df_top15 = df_can["Total"].tail(15)
# print(df_top15)

df_top15.plot(kind="barh", figsize=(12, 12))

plt.xlabel("Number of Immigrants")
plt.ylabel("Country")
plt.title(
    "Total number of immigrants to Canada from the top 15 countries, for the period 1980 - 2013"
)

# annotate value labels to each country
for index, value in enumerate(df_top15):
    label = format(int(value), ",")  # format int with commas

    # place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
    plt.annotate(label, xy=(value - 50000, index - 0.10), color="white")

plt.show()
