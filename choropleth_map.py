import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import folium
from folium import plugins, Choropleth

df_can = pd.read_csv("canada.csv")
print(df_can.head())
# create a plain world map
world_map = folium.Map(location=[0, 0], zoom_start=2)
# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
folium.Choropleth(
    geo_data="world_countries.json",
    data=df_can,
    columns=["Country", "Total"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Immigration to Canada",
    reset=True,
).add_to(world_map)

# display map
world_map.show_in_browser()
