import os

from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.graph_objs as go
from django.conf import settings

# path_to_data = os.path(settings.MEDIA_ROOT, path)
# path_to_data = "board/static/board/data/"
paper_bg_color = 'rgba(0,0,0,0)'
bg_color = 'rgba(0,0,0,0)'
text_color = '#ffffff'

from django_plotly_dash import DjangoDash
df10 = pd.read_json(settings.STATICFILES_DIRS[0] + '/board/data/map.json')
app = DjangoDash('map')

# df10 = pd.read_json('Z:/Work_Projects_Dir/DashBoard_V0.3 — копия/dash_board/static/board/data/map.json') # settings.STATICFILES_DIRS[0] + '/board/data/weeked.json'
# app = Dash(__name__)


df10.sort_values(by='sorting_date', inplace=True)
df10.reset_index(drop=True, inplace=True)
# categoryarray_to_push = df10['created'].unique()



def color_picker(str, os):
    if str == 'МТС':
        return 'red'
    if str == 'Теле2':
        return 'black'
    if str == 'Мегафон':
        if os == 'IOS':
            return 'darkgreen'
        elif os == 'Android':
            return 'chartreuse'
    if str == 'Билайн':
        return 'orange'
    if str == 'МГТС':
        return 'darkblue'
    if str == 'Ростелеком(мобильный)':
        return 'darkviolet'
    if str == 'Trytek':
        return '#c4c404'
    if str == 'Win mobile':
        return 'darkviolet'
    if str == 'Волна мобайл':
        return 'darkblue'
    if str == 'Инетком':
        return '#07ab5e'
    if str == 'Крафт-С':
        return '#783d02'
    if str == 'Севтелеком':
        return 'pink'
    if str == 'Севтелекомсвязь':
        return '#b80786'
    if str == 'Ростелеком':
        return 'violet'

text_style = {'font-size': '28px', 'padding-left': '5px', 'text-align': 'center', 'font-family': 'Montserrat, sans-serif', 'color': 'white'}
def map_my():
    fig = go.Figure()
    fig.add_trace(go.Scattermapbox(lat=df10['longitude'],
                            lon=df10['latitude'],
                            text=(df10['street']),
                            marker=go.scattermapbox.Marker(size=10, color='Black', opacity=0.5)
                            ))
    fig.add_trace(go.Scattermapbox(lat=df10['longitude'],
                            lon=df10['latitude'],
                            text=(df10['street']),
                            marker=go.scattermapbox.Marker(size=6, color='#ADD8E6', opacity=0.5)
                            ))
    # fig.add_trace(go.Scattermapbox(lat=df10['longitude'],
    #                         lon=df10['latitude'],
    #                         text=(df10['street']),
    #                         marker=go.scattermapbox.Marker(size=10, symbol='mobile-phone', opacity=0.5)
    #                         ))
    map_center = go.layout.mapbox.Center(lat=df10['longitude'].values[1], lon=df10['latitude'].values[1])
    fig.update_layout(mapbox_style="open-street-map", mapbox=dict(center=map_center, zoom = 6.8), showlegend=False, paper_bgcolor=paper_bg_color, plot_bgcolor=bg_color, margin=dict(l=20, r=20, t=20, b=20)) #
    return fig


app.layout = html.Div([
    html.Div(
            # style={'font-size':'35px', 'padding-left':'5px', 'color':'#000000', 'text-align':'center'},
        children=[
            # html.Div('Карта: ', style=text_style),
            dcc.Graph(figure=map_my(),
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'Улица': 'г.Москва, ул. Муравская, 34'}]},
            style={'margin-left': 'auto', 'margin-right': 'auto'}
            )
        ], style={'padding': 10, 'width': '97vh', 'height': '100%', }), #, style={'padding': 10, 'flex': 1}, 'height': '75vh'

        html.Div(
            # style={'font-size':'35px', 'padding-left':'5px', 'color':'#000000', 'text-align':'center'},
            children=[
                html.Div('Средняя работоспособность VPN-сервисов в выбранной точке тестирования: ', style=text_style),
                dcc.Graph(id = 'x-time-series', style={'margin': '15px'})
            ], style={'padding': 10, 'width': '100vh'}) # , style={'padding': 10, 'flex': 1}, 'height': '75vh'
        ], style={'display': 'grid', 'overflow':'hidden', 'border-bottom':'10px;', 'border-color':'#f0f0f0'})#style={'backgroundColor':'#ffffff', 'display': 'flex', 'flex-direction': 'row'}




def create_time_series(dff):
    # print(dff)
    dff.sort_values(by='sorting_date', inplace=True)
    categoryarray_to_push = dff['created'].unique()
    fig = go.Figure()
    for i in dff['operator_names'].unique():
        for j in dff['os_names'].unique():
            # print(dff[dff['operator_names'] == i])
            fig.add_trace(go.Scatter(
                        x=dff[(dff['operator_names'] == i) & (dff['os_names'] == j)]['created'], 
                        y=dff[(dff['operator_names'] == i) & (dff['os_names'] == j)]['mean_all'], 
                        mode='lines+markers',
                        marker=dict(color=color_picker(i, j), size=8),
                        line=dict(color=color_picker(i, j), width=3, shape='spline', smoothing = 0),
                        name=i + ' ' + j,
                        textfont=dict(
                        family="Montserrat, sans-serif",
                        size=10,
                        color=text_color)
                        ))
    fig.update_layout(hovermode="y unified", paper_bgcolor=paper_bg_color, plot_bgcolor=bg_color, font=dict(family="Montserrat, sans-serif", size=10, color=text_color), height=500, xaxis_showgrid=True, yaxis_showgrid=True, margin=dict(l=20, r=20, t=20, b=20), showlegend=True,
                      hoverlabel=dict(
                          font=dict(
                              color='black',
                              family="Montserrat, sans-serif"
                          )
                      )) #, xaxis_showgrid=False, yaxis_showgrid=False
    fig.update_xaxes(categoryorder='array', categoryarray = categoryarray_to_push, tickangle = -50)
    fig.update_xaxes(showline=True, linewidth=2, linecolor='#77aad9', gridcolor='#77aad9')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='#77aad9', gridcolor='#77aad9')
    fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#77aad9')
    fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#77aad9')
    fig.update_yaxes(range=[-10, 110])
    return fig

@app.callback(
    Output('x-time-series', 'figure'),
    Input('crossfilter-indicator-scatter', 'hoverData'))
def update_y_timeseries(hoverData):
    # print(hoverData)
    if len(hoverData['points'][0]) == 1:
        country_name = hoverData['points'][0]['Улица']
    else:
        country_name = hoverData['points'][0]['text']
    dff = df10[df10['street'] == country_name]
    return create_time_series(dff)


# if __name__ == '__main__':
#     # make_map_file()
#     app.run_server(debug=True)


