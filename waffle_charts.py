import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use("ggplot")  # optional: for ggplot-like style

# Import Primary Modules:
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library

from pywaffle import Waffle


# check for latest version of Matplotlib and seaborn
print("Matplotlib version: ", mpl.__version__)  # >= 2.0.0

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)

# Let's revisit the case study on Denmark, Norway & Sweden
# let's create a new dataframe for these three countries
df_dsn = df_can.loc[["Denmark", "Norway", "Sweden"], :]

# let's take a look at our dataframe
print(df_dsn)


# Step 1. The first step into creating a waffle chart is determing
# the proportion of each category with respect to the total.

# compute the proportion of each category with respect to the total
total_values = df_dsn["Total"].sum()
category_proportions = df_dsn["Total"] / total_values

# print out proportions
print(pd.DataFrame({"Category Proportion": category_proportions}))

# Set up the Waffle chart figure

fig = plt.figure(
    FigureClass=Waffle,
    rows=20,
    columns=30,  # pass the number of rows and columns for the waffle
    values=df_dsn["Total"],  # pass the data to be used for display
    cmap_name="tab20",  # color scheme
    legend={
        "labels": [f"{k} ({v})" for k, v in zip(df_dsn.index.values, df_dsn.Total)],
        "loc": "lower left",
        "bbox_to_anchor": (0, -0.1),
        "ncol": 3,
    },
    # notice the use of list comprehension for creating labels
    # from index and total of the dataset
)

# Display the waffle chart
plt.show()

# Now repeat for China and India
df_CI = df_can.loc[["China", "India"], :]

# let's take a look at our dataframe
print(df_CI)

# compute the proportion of each category with respect to the total
total_values_CI = df_CI["Total"].sum()
category_proportions_CI = df_dsn["Total"] / total_values

# print out proportions
print(pd.DataFrame({"Category Proportion": category_proportions_CI}))

# Set up the Waffle chart figure

fig = plt.figure(
    FigureClass=Waffle,
    rows=20,
    columns=30,  # pass the number of rows and columns for the waffle
    values=df_CI["Total"],  # pass the data to be used for display
    cmap_name="tab20",  # color scheme
    legend={
        "labels": [f"{k} ({v})" for k, v in zip(df_CI.index.values, df_CI.Total)],
        "loc": "lower left",
        "bbox_to_anchor": (0, -0.1),
        "ncol": 3,
    },
    # notice the use of list comprehension for creating labels
    # from index and total of the dataset
)

# Display the waffle chart
plt.show()
