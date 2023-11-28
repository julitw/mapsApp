import pandas as pd
import json
import plotly.graph_objects as go

def generate_map_Gabrysia(): 
    data = pd.read_csv('website\maps\dane_Gabrysia\gdf_diseases.csv')
    with open("website\maps\dane_Kasia\gz_2010_us_040_00_5m_1.json", 'r') as f:
        states = json.load(f)

    df = pd.DataFrame(data)

    fig = go.Figure(data=go.Choropleth(
            geojson=states,
            locations=df['State'],
            z=df['HeartDisease'],
            featureidkey="properties.NAME",
            colorscale='Viridis'
        ))
        

    fig.update_layout(
        title_text=f'Number of people suffering from heart disease',
        geo_scope='usa',
        )

    fig.update_geos(resolution=110, showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")

    graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph
