import pandas as pd
import plotly.express as px

# Replace with your actual dataset or data source
data = {
    "Category": ["Category 1", "Category 1", "Category 2", "Category 2", "Category 3"],
    "Subcategory": [
        "Subcategory 1A",
        "Subcategory 1B",
        "Subcategory 2A",
        "Subcategory 2B",
        "Subcategory 3A",
    ],
    "Value": [10, 20, 30, 40, 50],
}
df = pd.DataFrame(data)

fig = px.treemap(
    df,
    path=["Category", "Subcategory"],  # Define hierarchical structure
    values="Value",  # Size of each rectangle
    title="Treemap Example",
)  # Title of the treemap

fig.show()
