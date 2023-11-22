import pandas as pd
import plotly
import json

import plotly.graph_objects as go

df = pd.read_csv('gdf_fires.csv')
with open("gz_2010_us_040_00_5m_1.json", 'r') as f:
    states = json.load(f)

def fires_in_states():
    state_fires = df.groupby('state')['number of fires'].sum().reset_index()
    df_test = pd.DataFrame(state_fires)

    fig = go.Figure(data=go.Choropleth(
        locations=df_test['state'],
        z=df_test['number of fires'],
        locationmode='USA-states',
        colorscale='Reds',
    ))

    fig.update_layout(
        title_text=f'Number of fires per state', # in {month_name}',
        geo_scope='usa',
    )

    fig.update_geos(resolution=110, showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")

    graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph