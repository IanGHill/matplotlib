import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
num_quarters = 4
num_categories = 4
num_subcategories = 3
num_samples = num_quarters * num_categories * num_subcategories * 50
# Generate sample sales data
np.random.seed(40)
# Creating sample data
dates = np.repeat(["Q1", "Q2", "Q3", "Q4"], 50 * num_categories * num_subcategories)
categories = np.tile(
    np.random.choice(
        ["Laptops", "Desktops", "Peripherals", "Software"], size=num_quarters * 50
    ),
    num_categories * num_subcategories,
)
subcategories = np.tile(
    np.random.choice(
        ["Accessories", "Components", "Software Suites"], size=num_quarters * 50
    ),
    num_categories * num_subcategories,
)
sales_values = np.random.randint(1000, 5000, size=num_samples)
# Create DataFrame
df = pd.DataFrame(
    {
        "Date": dates,
        "Category": categories,
        "Subcategory": subcategories,
        "Sales": sales_values,
    }
)

# Create pivot table
pivot_table = df.pivot_table(
    index="Date", columns=["Category", "Subcategory"], values="Sales", aggfunc=np.sum
)

# Plotting a pivot chart
pivot_table.plot(kind="bar", figsize=(14, 8))
plt.title("Sales Summary of IT Products by Category and Subcategory")
plt.xlabel("Quarters")
plt.ylabel("Total Sales")
plt.grid(False)
plt.legend(
    title=("Category", "Subcategory"), bbox_to_anchor=(1.05, 1), loc="upper left"
)
plt.tight_layout()
plt.show()
