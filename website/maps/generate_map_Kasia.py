import plotly.express as px


def generate_map_Kasia():  # do modyfikacji przez ludzi od map
    data = [

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
