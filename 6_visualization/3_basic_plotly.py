# Import necessary libraries for Plotly
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Set the default renderer to 'browser'
pio.renderers.default = 'browser'

# Data to be plotted
df = px.data.iris()

# Create a 3D scatter plot for the Iris dataset
fig = px.scatter_3d(df, 
                    x='sepal_width', 
                    y='sepal_length', 
                    z='petal_width', 
                    color='species')
fig.show()

# Creating random data for demonstration purposes
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Create a basic scatter plot
plot = go.Figure(data=[go.Scatter(
    x=random_x, 
    y=random_y, 
    mode='markers'
)])

# Add a dropdown menu to switch between scatter plot and bar chart
plot.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ],
            direction="down",
        ),
    ]
)

plot.show()

# Load tips dataset from Plotly Express
df = px.data.tips()

# Extract total_bill and day columns for plotting
x = df['total_bill']
y = df['day']

# Create a scatter plot with a range slider and selector
plot = go.Figure(data=[go.Scatter(
    x=x, 
    y=y, 
    mode='markers'
)])

# Update layout to include a range slider and a selector button
plot.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(
                    count=2,
                    step="day",
                    stepmode="backward",
                    label="Last 2 days"
                ),
            ]
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)

plot.show()


import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Generate some sample exchange rate data
np.random.seed(0)
date_range = pd.date_range(start='2021-01-01', end='2022-01-01', freq='D')
exchange_rates = np.random.normal(loc=1.2, scale=0.05, size=len(date_range))

# Create a DataFrame
df = pd.DataFrame({'Date': date_range, 'Exchange Rate': exchange_rates})

# Create a Plotly figure
fig = go.Figure()

# Add the trace for exchange rates
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Exchange Rate'],
    mode='lines',
    name='Exchange Rate'
))

# Add a slider to control the date range
steps = []
for i in range(len(df)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(df)},
              {"title": "Exchange Rate History: " + str(df['Date'][i].date())}],
        label=str(df['Date'][i].date())
    )
    step["args"][0]["visible"][i] = True  # Toggle visibility
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Date: ", "visible": True, "xanchor": 'center'},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    title="Exchange Rate History with Slider",
    xaxis_title="Date",
    yaxis_title="Exchange Rate",
    showlegend=False
)

# Show the figure
fig.show()


