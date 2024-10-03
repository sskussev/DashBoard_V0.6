import io
import json

import pandas as pd
import plotly.figure_factory as ff
from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
from django_plotly_dash import DjangoDash
from django.conf import settings
app = DjangoDash('without_vpn_mts')
# app = Dash(__name__) # для проверки отдельно, не раскоменчивать

# dff = pd.read_json(settings.STATICFILES_DIRS[0] + '/board/data/bar_2.json')
with io.open(settings.STATICFILES_DIRS[0] + '/board/data/bar_3_mts.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

colors_mts = {
    'Facebook App': 'rgb(66, 123, 237)',
    'Facebook Web': 'rgb(138, 168, 227)',
    'Instagram App': 'rgb(199, 20, 193)',
    'Instagram Web': 'rgb(232, 160, 230)',
}

fig = ff.create_gantt(data, colors=colors_mts, index_col='Task', show_colorbar=True,
                      group_tasks=True, showgrid_x=True, showgrid_y=True)

fig.layout.xaxis.update({
    'type': 'category',
    'tickvals': [data[i]['Start'] for i in range(len(data))],
    'ticktext': [data[i]['Start'] for i in range(len(data))],
    'tickangle': -50,
    'categoryorder': 'category ascending',

})

fig.update_xaxes(linecolor='#77aad9',
                 gridcolor='#77aad9')
fig.update_yaxes(linecolor='#77aad9',
                 gridcolor='#77aad9')
fig.layout.update(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)
fig.update_layout(
    font_family="Montserrat, sans-serif",
    # font_color="#cccccc",
    font_color='#ffffff'

)

fig.layout.title = None
fig.update_yaxes(automargin=True)
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
app.layout = html.Div([
   dcc.Graph(figure=fig)
],)

# для проверки отдельно, не раскоменчивать
# if __name__ == '__main__':
#     app.run_server(debug=True, port='16600')
