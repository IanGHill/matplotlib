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

##### 4 - Histogram #####
##### - Let's find out the frequency distribution of the number (population)
# of new immigrants from the various countries to Canada in 2013?

df_country = df_can.groupby(["Country"])["2013"].sum().reset_index()

# Plot the bar
fig, ax = plt.subplots(figsize=(10, 4))
count = ax.hist(df_country["2013"])

# you can check the arrays in count with indexing count[0] for count, count[1] for bins

ax.set_title("New Immigrants in 2013")
ax.set_xlabel("Number of Immigrants")
ax.set_ylabel("Number of Countries")
ax.set_xticks(list(map(int, count[1])))
ax.legend(["Immigrants"])

# Display the plot
plt.show()


##### QUESTION - What is the immigration distribution for
# Denmark, Norway, and Sweden for years 1980 - 2013?

# let's quickly view the dataset
df = df_can.groupby(["Country"])[years].sum()
df_dns = df.loc[["Denmark", "Norway", "Sweden"], years]
df_dns = df_dns.T
# print(df_dns)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df_dns)
ax.set_title("Immigration from Denmark, Norway, and Sweden from 1980 - 2013")
ax.set_xlabel("Number of Immigrants")
ax.set_ylabel("Number of Years")
ax.legend(["Denmark", "Norway", "Sweden"])
# Display the plot
plt.show()

#### Question: What is the immigration distribution for China and India for years 2000 to 2013?

# let's quickly view the dataset
df = df_can.groupby(["Country"])[years].sum()
y = list(map(str, range(2000, 2014)))
df_ci = df.loc[["China", "India"], y]
df_ci = df_ci.T
print(df_ci)

fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df_ci)
ax.set_title("Immigration from China & India from 1980 - 2013")
ax.set_xlabel("Number of Immigrants")
ax.set_ylabel("Number of Years")
ax.legend(["China", "India"])
# Display the plot
plt.show()
