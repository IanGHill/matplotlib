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

##### 1 - Line Plots #####
##### - Let's created a line plot to visualize the immigrants (to Canada) trend during 1980 to 2013.

# creating df with only years columns from 1980 - 2013
df_line = df_can[years]

# Applying sum to get total immigrants year-wise
total_immigrants = df_line.sum()
print(total_immigrants)
# Create figure and axes
fig, ax = plt.subplots()

# Changing the index type to integer
total_immigrants.index = total_immigrants.index.map(int)

# Plot the line
ax.plot(
    total_immigrants,
    marker="s",  # Including markers in squares shapes
    markersize=5,  # Setting the size of the marker
    color="green",  # Changing the color of the line
    linestyle="dotted",
)  # Changing the line style to a Dotted line

# Setting up the Title
ax.set_title("Immigrants between 1980 to 2013")

# Setting up the Labels
ax.set_xlabel("Years")
ax.set_ylabel("Total Immigrants")

# limits on x-axis
plt.xlim(1975, 2015)  # or ax.set_xlim()

# Enabling Grid
plt.grid(True)  # or ax.grid()

# Legend
plt.legend(["Immigrants"])  # or ax.legend()

# Display the plot
plt.show()

#### QUESTION - Plot a line graph of immigration from Haiti

# Creating data for plotting
df_can.reset_index(inplace=True)
haiti = df_can[df_can["Country"] == "Haiti"]

# creating haiti with only years columns from 1980 - 2013
# and transposing to get the result as a series
haiti = haiti[years].T

# converting the index to type integer
haiti.index = haiti.index.map(int)

# Plotting the line plot on the data
fig, ax = plt.subplots()

ax.plot(haiti)

# Setting up the Title
ax.set_title("Immigrants from Haiti between 1980 to 2013")

# Setting up the Labels
ax.set_xlabel("Years")
ax.set_ylabel("Number of Immigrants")

# Enabling Grid and ticks
# plt.grid(True)  #or ax.grid()
# ax.set_xticks(list(range(n, m, s)))

# Legend
plt.legend(["Immigrants"])  # or ax.legend()

ax.annotate("2010 Earthquake", xy=(2000, 6000))
plt.show()
