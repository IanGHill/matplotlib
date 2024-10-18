import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use("ggplot")  # optional: for ggplot-like style

# Import Primary Modules:
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
from PIL import Image  # converting images into arrays

# import seaborn
import seaborn as sns

# check for latest version of Matplotlib and seaborn
print("Matplotlib version: ", mpl.__version__)  # >= 2.0.0
print("Seaborn version: ", sns.__version__)

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# 1 - Count Plot - A count plot can be thought of as a histogram across a categorical, instead of quantitative, variable.

df_can1 = df_can.replace("Latin America and the Caribbean", "L-America")
df_can1 = df_can1.replace("Northern America", "N-America")

plt.figure(figsize=(15, 10))
sns.countplot(x="Continent", data=df_can1)
plt.show()

# 2 - Barplot - This plot will perform the Groupby on a categorical varaible and plot aggregated values, with confidence intervals.
plt.figure(figsize=(15, 10))
sns.barplot(x="Continent", y="Total", data=df_can1)
plt.show()

# 3 -  Regression Plot

# Use seaborn to create a scatter plot with a regression line to visualize the total immigration from Denmark,
# Sweden, and Norway to Canada from 1980 to 2013.
years = list(map(str, range(1980, 2014)))
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

# define figure size
plt.figure(figsize=(15, 10))

# define background style and font size
sns.set(font_scale=1.5)
sns.set_style("whitegrid")

# generate plot and add title and axes labels
ax = sns.regplot(
    x="year",
    y="total",
    data=df_total,
    color="green",
    marker="+",
    scatter_kws={"s": 200},
)
ax.set(xlabel="Year", ylabel="Total Immigration")
ax.set_title(
    "Total Immigration from Denmark, Sweden, and Norway to Canada from 1980 - 2013"
)
plt.show()
