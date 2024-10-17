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

##### 5 - Pie Chart #####
##### - Let's create a pie chart representing the 'Total Immigrants' for the year 1980 to 1985

# creating df with only years columns from 1980 - 2013
df_line = df_can[years]

# Applying sum to get total immigrants year-wise
total_immigrants = df_line.sum()

fig, ax = plt.subplots()

# Pie on immigrants
ax.pie(
    total_immigrants[0:5],
    labels=years[0:5],
    colors=["gold", "blue", "lightgreen", "coral", "cyan"],
    autopct="%1.1f%%",
    explode=[0, 0, 0, 0, 0.1],
)  # using explode to highlight the lowest

ax.set_aspect("equal")  # Ensure pie is drawn as a circle

plt.title("Distribution of Immigrants from 1980 to 1985")
# plt.legend(years[0:5]), include legend, if you donot want to pass the labels
plt.show()
