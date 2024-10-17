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

##### 2 - Scatter Plots #####
##### - Let's create a Scatter plot to visualize the immigrants (to Canada) trend during 1980 to 2013.

# creating df with only years columns from 1980 - 2013
df_line = df_can[years]

# Applying sum to get total immigrants year-wise
total_immigrants = df_line.sum()

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 4))

total_immigrants.index = total_immigrants.index.map(int)

# Customizing Scatter Plot
ax.scatter(
    total_immigrants.index,
    total_immigrants,
    marker="o",  # setting up the markers
    s=20,  # setting up the size of the markers
    color="darkblue",
)  # the color for the marker

# add title
plt.title("Immigrants between 1980 to 2013")
# add labels
plt.xlabel("Years")
plt.ylabel("Total Immigrants")
# including grid
plt.grid(True)

# Legend at upper center of the figure
ax.legend(["Immigrants"], loc="upper center")

# Display the plot
plt.show()
