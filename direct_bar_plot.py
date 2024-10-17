import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
# years = np.arange(1980,2014)

##### 3 - Bar Plots #####
##### - Let's create a bar plot to visualize the top 5 countries that
# contribued the most immigrants to Canada from 1980 to 2013.

# Sorting the dataframe on 'Total' in descending order
df_can.sort_values(["Total"], ascending=False, axis=0, inplace=True)

# get the top 5 entries with head function
df_top5 = df_can.head()

# resetting the index back to original way
df_bar_5 = df_top5.reset_index()

# Creating alist of names of the top 5 countries
label = list(df_bar_5.Country)
label[2] = "UK"

fig, ax = plt.subplots(figsize=(10, 4))

ax.bar(label, df_bar_5["Total"], label=label)
ax.set_title("Immigration Trend of Top 5 Countries")
ax.set_ylabel("Number of Immigrants")
ax.set_xlabel("Years")

plt.show()
