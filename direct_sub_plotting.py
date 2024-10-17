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

##### 6- Sub plotting #####
##### - let’s create a line and scatter plot in one row

# creating df with only years columns from 1980 - 2013
df_line = df_can[years]

# Applying sum to get total immigrants year-wise
total_immigrants = df_line.sum()

total_immigrants.index = total_immigrants.index.map(int)

fig, axs = plt.subplots(1, 2, sharey=True)

# Plotting in first axes - the left one
axs[0].plot(total_immigrants)
axs[0].set_title("Line plot on immigrants")

# Plotting in second axes - the right one
axs[1].scatter(total_immigrants.index, total_immigrants)
axs[1].set_title("Scatter plot on immigrants")

axs[0].set_ylabel("Number of Immigrants")

# Adding a Title for the Overall Figure
fig.suptitle("Subplotting Example", fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()


# Show the figure
plt.show()


##### - You can also implement the subplotting with add_subplot() as below:-

# Create a figure with Four axes - two rows, two columns
fig = plt.figure(figsize=(8, 4))

# Add the first subplot (top-left)
axs1 = fig.add_subplot(1, 2, 1)
# Plotting in first axes - the left one
axs1.plot(total_immigrants)
axs1.set_title("Line plot on immigrants")

# Add the second subplot (top-right)
axs2 = fig.add_subplot(1, 2, 2)
# Plotting in second axes - the right one
axs2.barh(
    total_immigrants.index, total_immigrants
)  # Notice the use of 'barh' for creating horizontal bar plot
axs2.set_title("Bar plot on immigrants")

# Adding a Title for the Overall Figure
fig.suptitle("Subplotting Example", fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()


# Show the figure
plt.show()

######## Create a figure with Four axes - two rows, two columns  ###########

fig = plt.figure(figsize=(10, 10))

# Add the first subplot (top-left)
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(total_immigrants)
ax1.set_title("Plot 1 - Line Plot")

# Add the second subplot (top-right)
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(total_immigrants.index, total_immigrants)
ax2.set_title("Plot 2 - Scatter plot")

# Add the third subplot (bottom-left)

df = df_can.groupby(["Country"])[years].sum()
df_dns = df.loc[["Denmark", "Norway", "Sweden"], years]
df_dns = df_dns.T

ax3 = fig.add_subplot(2, 2, 3)
ax3.hist(df_dns)
ax3.set_title("Plot3 - Histogram")
ax3.set_xlabel("Number of Immigrants")
ax3.set_ylabel("Number of Years")

# Add the fourth subplot (bottom-right)
ax4 = fig.add_subplot(2, 2, 4)
ax4.pie(
    total_immigrants[0:5],
    labels=years[0:5],
    colors=["gold", "blue", "lightgreen", "coral", "cyan"],
    autopct="%1.1f%%",
)
ax4.set_aspect("equal")
ax4.set_title("Plot 5 - Pie Chart")

# Adding a Title for the Overall Figure
fig.suptitle("Four Plots in a Figure Example", fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()


# Show the figure
plt.show()
