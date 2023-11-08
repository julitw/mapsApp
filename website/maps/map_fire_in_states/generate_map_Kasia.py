import pandas as pd
import plotly
import json

import plotly.graph_objects as go

df = pd.read_csv('gdf_fires.csv')
with open("gz_2010_us_040_00_5m_1.json", 'r') as f:
    states = json.load(f)

def fires_in_states():
    # filtered_df = df[df['month'] == selected_month]
    # number_to_months = {6: 'June',
    #                     7: 'July',
    #                     8: 'August',
    #                     9: 'September',
    #                     10: 'October'}
    #
    # month_name = number_to_months.get(selected_month)
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

    return plotly.offline.plot(fig, filename='fires_in_states.html')


if __name__ == '__main__':
    fires_in_states()