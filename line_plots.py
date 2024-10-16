import pandas as pd

df_can = pd.read_excel(
    "canada.xlsx",
    sheet_name="Canada by Citizenship",
    skiprows=range(20),
    skipfooter=2,
)

print("Data read into a pandas dataframe!")
