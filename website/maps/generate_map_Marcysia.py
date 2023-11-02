import plotly.express as px


def generate_map_Marcysia():  # do modyfikacji przez ludzi od map
    data = [
        {'City': 'New York', 'Lat': 40.7128, 'Lon': -74.0060, 'Population': 8398748},
        {'City': 'Los Angeles', 'Lat': 34.0522, 'Lon': -118.2437, 'Population': 3990456},
        {'City': 'Chicago', 'Lat': 41.8781, 'Lon': -87.6298, 'Population': 2705994},
    ]
    fig = px.scatter_geo(data,
                         lat='Lat',  # szerokość geograficzna
                         lon='Lon',  # długość geograficzna
                         text='City',
                         size='Population',
                         projection='natural earth')

    fig.update_geos(resolution=110, showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")

    graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph
