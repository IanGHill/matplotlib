import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv(
    "airline_data.csv",
    encoding="ISO-8859-1",
    dtype={
        "Div1Airport": str,
        "Div1TailNum": str,
        "Div2Airport": str,
        "Div2TailNum": str,
    },
)

data = data.sample(n=500, random_state=42)

print("Data downloaded and read into a dataframe!")

# 1/ Scatter Plot -
# Let us use a scatter plot to represent departure time changes with respect to airport distance

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data["Distance"], y=data["DepTime"], mode="markers", marker=dict(color="red")
    )
)
fig.update_layout(
    title="Distance vs Departure Time", xaxis_title="Distance", yaxis_title="DepTime"
)
fig.show()

# 2/ Line PLot
# Let us now use a line plot to extract average monthly arrival delay time and see how it changes over the year.

# Group the data by Month and compute average over arrival delay time.
line_data = data.groupby("Month")["ArrDelay"].mean().reset_index()
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=line_data["Month"],
        y=line_data["ArrDelay"],
        mode="lines",
        marker=dict(color="green"),
    )
)
fig.update_layout(
    title="Month vs Average Flight Delay Time",
    xaxis_title="Month",
    yaxis_title="ArrDelay",
)
fig.show()

# 3/ Bar Chart
# Let us use a bar chart to extract number of flights from a specific airline that goes to a destination

# Group the data by destination state and reporting airline. Compute total number of flights in each combination
bar_data = data.groupby("DestState")["Flights"].sum().reset_index()

fig = px.bar(
    bar_data,
    x="DestState",
    y="Flights",
    title="Total number of flights to the destination state split by reporting airline",
)
fig.show()

# 4/ Histogram
# Let us represent the distribution of arrival delay using a histogram

# Set missing values to 0
data["ArrDelay"] = data["ArrDelay"].fillna(0)
fig = px.histogram(
    data,
    x="ArrDelay",
    title="Total number of flights to the destination state split by reporting air",
)
fig.show()

# 5/ Bubble Chart
# Lets use a bubble plot to represent number of flights as per reporting airline

# Group the data by reporting airline and get number of flights
bub_data = data.groupby("Reporting_Airline")["Flights"].sum().reset_index()

fig = px.scatter(
    bub_data,
    x="Reporting_Airline",
    y="Flights",
    size="Flights",
    hover_name="Reporting_Airline",
    title="Reporting Airline vs Number of Flights",
    size_max=60,
)
fig.show()

# 6/ Pie Chart
# Let us represent the proportion of Flights by Distance Group (Flights indicated by numbers)
fig = px.pie(
    data,
    values="Flights",
    names="DistanceGroup",
    title="Flight propotion by Distance Group",
)
fig.show()

# 7 / Sunburst Chart
# Let us represent the hierarchical view in othe order of month and destination state
# holding value of number of flights

fig = px.sunburst(
    data,
    path=["Month", "DestStateName"],
    values="Flights",
    title="Flight Distribution Hierarchy",
)
fig.show()
