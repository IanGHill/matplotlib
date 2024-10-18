import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import folium
from folium import plugins

# define the world map
world_map = folium.Map()

# display world map
# world_map.show_in_browser()

# Centred on Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
# world_map.show_in_browser()

# create a Cartodb dark_matter map of the world centered around Canada
world_map = folium.Map(
    location=[56.130, -106.35], zoom_start=4, tiles="Cartodb dark_matter"
)
# world_map.show_in_browser()

# create a Cartodb positron map of the world centered around Canada
world_map = folium.Map(
    location=[56.130, -106.35], zoom_start=4, tiles="Cartodb positron"
)
# world_map.show_in_browser()

# Sanfrancisco crime stats
df_incidents = pd.read_csv("incidents.csv")
print(df_incidents.head())

# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
# sanfran_map.show_in_browser()

# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.vector_layers.CircleMarker(
        [lat, lng],
        radius=5,  # define how big you want the circle markers to be
        color="yellow",
        fill=True,
        popup=label,
        fill_color="blue",
        fill_opacity=0.6,
    ).add_to(sanfran_map)

# show map
# sanfran_map.show_in_browser()

# Alternatively we can use clustering to aid in homing in on different areas:


# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for (
    lat,
    lng,
    label,
) in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
sanfran_map.show_in_browser()
