import pandas as pd
import psycopg2
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_daq as daq
import plotly.graph_objs as go
import pandas as pd
import random

import warnings
warnings.filterwarnings('ignore')


host = "192.168.1.173"
port = "5432"

userName = "postgres"
pas = "changeme"
BDName = "postgres"

def connectToBD():
    conn = psycopg2.connect(dbname=BDName, host=host, user=userName, password=pas, port=port)
    return(conn)


def getData(sqlRequest, conn):
    with conn:
        return pd.read_sql_query(sqlRequest, conn)


def vpnCount(data):
    for i in range(data.shape[0]):
        if data['vpn_android'].iloc[i] == 'Отсутствует':
            data['vpn_android'].iloc[i] = data['vpn_ios'].iloc[i]
    return data





# print('SELECT vpn_ios, vpn_android FROM asndata WHERE asnnumber IN {}'.format('(AS6939)'))
# data = getData("SELECT * FROM asndata", connectToBD())
# data = vpnCount(data)['vpn_android'].unique()
# print(data[data['type'] == 'Ручное']['asnnumber'].unique())
# print(data['blocked'].unique())
# "select  asnnumber, os_names, week_period, week_sorting_date, vpn_android, vpn_ios, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData GROUP BY asnnumber, os_names, week_period, week_sorting_date, vpn_android, vpn_ios"
# sql = "select * from asnData"
# sql = "SELECT * FROM   generate_series('2020-02-01'::DATE, '2020-04-05'::DATE, '1 week'::interval)"

# with conn:
#     sql = "select  asnnumber, os_names, week_period, week_sorting_date, vpn_android, vpn_ios, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData GROUP BY asnnumber, os_names, week_period, week_sorting_date, vpn_android, vpn_ios"
#     # sql = "select * from asnData"
#     # sql = "SELECT * FROM   generate_series('2020-02-01'::DATE, '2020-04-05'::DATE, '1 week'::interval)"
#     dat1 = pd.read_sql_query(sql, conn)
# print(dat1)
def getK():
    conn = connectToBD()
    k = pd.to_datetime(getData('SELECT created FROM asndata', conn)['created']).sort_values().unique()
    conn.close()
    # k = k.to_list()
    return k

# def getAsn():
#     conn = connectToBD()
#     asnList = getData('SELECT asnnumber FROM asndata', conn)['asnnumber'].unique()
#     conn.close()
#     # asnList = asnList.to_list()
#     return asnList

# def getOs():1976
#     conn = connectToBD()
#     osList = getData('SELECT os_names FROM asndata', conn)['os_names'].unique()
#     conn.close()
#     # asnList = asnList.to_list()
#     return osList

# print(asnList)
k = getK()
# asnList = getAsn()
# osList = getOs()
# ['AS197695' 'AS16345' 'AS8359' 'AS12958' 'AS25159' 'AS25513' 'AS12389'
#  'AS42610' 'AS47759' 'AS9009' 'AS14061' 'AS31208' 'AS13213' 'AS132203'
#  'AS13335' 'AS42437' 'AS63023' 'AS57169' 'AS212238' 'AS6939' 'AS12876'
#  'AS56630' 'AS21100' 'AS213230' 'AS204957' 'AS205544']


sql = """select  asnnumber, os_names, week_period, week_sorting_date, vpn_android, vpn_ios, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app\
         from asnData
         WHERE
         GROUP BY asnnumber, os_names, week_period, week_sorting_date, vpn_android, vpn_ios"
"""

paper_bg_color = 'rgba(0,0,0,0)'
bg_color = 'rgba(0,0,0,0)'
text_color = '#ffffff'
mts_counter = 0
tele2_counter = 0
megafon_counter = 0
beeline_counter = 0
mgts_counter = 0
rostelecom_mobile_counter = 0
rostelecom_counter = 0

text_style = {'font-size': '28px', 'padding-left': '5px', 'text-align': 'center', 'font-family': 'Montserrat, sans-serif', 'color': 'white'}

calendarStyle = {'width': '100%', 'text-align': 'center', 'font-family': 'Montserrat, sans-serif'}

dropdown_style = {'font-size': '20px', 'padding-left': '5px', 'padding-right': '5px', 'text-align': 'center', 'font-family': 'Montserrat, sans-serif', 'color': '#adcce9', 'margin-bottom': '10px'}
dropdown_inside_style = {'background-color':'white', 'color': 'black', 'text-align': 'left', 'font-family': 'Montserrat, sans-serif', 'border-radius': '5px'}
dropdown_as_is_style = {'flex-basis': 'auto', 'background-color':bg_color, 'margin-bottom': '15px'} # , 'width': '24vw'

RadioItemsStyle = {'text-align': 'center'}

style_all_filters = {'background-color':bg_color, 'display': 'flex', 'flex-direction': 'column', 'border-color': '#1f2630', 'font-family': 'Montserrat, sans-serif', 'color': 'white', 'margin-top': '2px'} # ,'width': '99vw'

app = Dash(__name__)



app.layout = html.Div([
    html.Div(
        children=[
            html.Div('Фильтры: ', style=text_style), #
            html.Div([
                html.Div(
                    children=[
                        html.Div('Тип сервиса: ', style=dropdown_style),
                        dcc.RadioItems(options=[
                                                    {'label':'Все', 'value':'*'}, 
                                                    {'label':'Заблокированные', 'value':'True'},
                                                    {'label':'Не заблокированные', 'value':'False'}
                                                ], 
                                       value='*', id='Type', style=RadioItemsStyle, inline=True)
                    ], style=dropdown_as_is_style),
                
                html.Div(
                    children=[
                        html.Div('Тип тестирования: ', style=dropdown_style),
                        dcc.RadioItems(options=[
                                                    {'label':'Все', 'value':'*'}, 
                                                    {'label':'Ручное', 'value':'Ручное'},
                                                    {'label':'Автоматическое', 'value':'Автоматическое'}
                                                ], 
                                       value='*', id='Testing_type', style=RadioItemsStyle, inline=True)
                    ], style=dropdown_as_is_style),

                html.Div(
                    children=[
                        html.Div('ASN: ', style=dropdown_style),
                        dcc.Dropdown(multi=False, id='ASN', clearable=False, style=dropdown_inside_style),#asnList, asnList[0], 
                    ], style=dropdown_as_is_style),

                html.Div(
                    children=[
                        html.Div('Операционная система: ', style=dropdown_style),
                        dcc.Dropdown( multi=False, id='OS', clearable=False, style=dropdown_inside_style),#osList, osList[0],
                    ], style=dropdown_as_is_style),

                html.Div(
                    children=[
                        html.Div('Название сервиса: ', style=dropdown_style),
                        dcc.Dropdown(multi=False, id='VPN', searchable=True, clearable=False, optionHeight=50, style=dropdown_inside_style), # vp, vp[0],
                    ], style=dropdown_as_is_style),

                

                html.Div(
                    children=[
                        html.Div('Оператор: ', style=dropdown_style),
                        dcc.Dropdown(multi=True, id='Oper', clearable=False, style=dropdown_inside_style),
                    ], style=dropdown_as_is_style),
                html.Div(
                    children=[
                       
                        html.Div('Период тестирования: ', style=dropdown_style),
                        dcc.DatePickerRange(
                            month_format='DD-MM-YYYY-Q',
                            display_format='DD-MM-YYYY',
                            id='datePicker',
                            min_date_allowed=k[0],
                            max_date_allowed=k[len(k)-1],
                            initial_visible_month=k[len(k)-1],
                            start_date=k[0],
                            end_date=k[len(k)-1], 
                            style=calendarStyle
                        )
                    ], style=dropdown_as_is_style
                    ),
                # html.Div(
                #     children=[
                #         html.Div('Отобразить по типам сервисов: ', style=dropdown_style),
                #         daq.ToggleSwitch(
                #             label='Отобразить по типам сервисов',
                #             labelPosition='bottom'),
                #     ]
                # )
            ], style=style_all_filters)
    ], style={'padding': 10,   'width': '29vh'}),
    html.Div(
        children=[
            html.Div('Результаты тестирования: ', style=text_style),
            dcc.Graph(id = 'x-time-series'),
            html.Div(id='b-time-series'),
            html.Div('Таблица тестированиЙ: ', style=text_style),
            html.Div(id='z-time-series'),
        ], style={'padding': 10, 'width': '169vh'}) 
], style={'display': 'flex', 'flex-direction': 'row', 'border-bottom': '10px', 'border-color': '#1f2630'}  )#


def rand_color():
    col = ['#'+''.join([random.choice('123456789ABCDEF') for i in range(6)])]
    return col


def color_picker(str, arr):
    if str == 'МТС':
        if arr[0] == 0:
            arr[0] = arr[0] + 1
            # print(arr[0])
            return ['red', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Теле2':
        if arr[1] == 0:
            # print(arr[1])
            arr[1] = arr[1] + 1
            return ['black', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Мегафон':
        if arr[2] == 0:
            # print(arr[2])
            arr[2] = arr[2] + 1
            return ['green', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Билайн':
        if arr[3] == 0:
            # print(arr[3])
            arr[3] = arr[3] + 1
            return ['orange', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'МГТС':
        if arr[4] == 0:
            # print(arr[4])
            arr[4] = arr[4] + 1
            return ['darkblue', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Ростелеком(мобильный)':
        if arr[5] == 0:
            # print(arr[5])
            arr[5] = arr[5] + 1
            return ['darkviolet', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Ростелеком':
        if arr[6] == 0:
            # print(arr[6])
            arr[6] = arr[6] + 1
            return ['violet', arr]
        else:
            return [rand_color()[0], arr]


def createGraph(data, VPN, dataM):
    data.sort_values(by='week_sorting_date', inplace=True)
    categoryarray_to_push = data['week_period'].unique()
    fig = go.Figure()
    arr = [
        mts_counter,
        tele2_counter,
        megafon_counter,
        beeline_counter ,
        mgts_counter,
        rostelecom_mobile_counter ,
        rostelecom_counter,
    ]
    # for v in VPN:
    #     curV = data[(data['vpn_android'] == v) | (data['vpn_ios'] == v)]
    make_mean = False
    for a in data['asnnumber'].unique():
        curVA = data[data['asnnumber'] == a]
        for o in curVA['os_names'].unique():
            curVAO = curVA[curVA['os_names'] == o]
            for oper in curVAO['operator_names'].unique():
                if len(curVAO['operator_names'].unique()) > 1:
                    make_mean = True
                cur = curVAO[curVAO['operator_names'] == oper]
                for typ in cur['type'].unique():
                    curT = cur[cur['type'] == typ]
                    if len(cur['type'].unique()) > 1:
                        make_mean = True
                    for blocked in curT['blocked'].unique():
                        curTB = curT[curT['blocked'] == blocked]
                        if len(curT['blocked'].unique()) > 1:
                            make_mean = True
                        if blocked:
                            blockedSTR = 'Блокируется'
                        else:
                            blockedSTR = 'Не блокируется'
                        col = color_picker(oper, arr)
                        # print(arr)
                        # print(oper)
                        arr = col[1]
                        fig.add_trace(go.Scatter(
                                    x=curTB['week_period'], 
                                    y=curTB['mean_all'], 
                                    mode='lines+markers',
                                    marker=dict(color=col[0], size=8),
                                    line=dict(color=col[0], width=3, shape='spline', smoothing = 0),
                                    name = "{} - <br>{} - <br>{} - <br>{} - <br>{} - <br>{}".format(VPN, o, oper, a, typ, blockedSTR),
                                    # name=VPN+' - '+ '<br>'+o+' - '+ '<br>'+oper+'-' + '<br>' + a, # +c+' - '+ '<br>'
                                    textfont=dict(
                                    family="Montserrat, sans-serif",
                                    size=16,
                                    color=text_color)
                                    ))
    if make_mean:
        fig.add_trace(
            go.Scatter(
                x=dataM['week_period'], 
                y=dataM['mean_all'], 
                mode='lines+markers',
                marker=dict(color='#707070', size=11),
                line=dict(color='#595959', width=5, shape='spline', dash = 'longdash', smoothing = 0),
                name= 'Среднее',
                textfont=dict(
                family="Montserrat, sans-serif",
                size=16,
                color=text_color)
                )
            )
    fig.update_layout(hovermode="y unified", paper_bgcolor=paper_bg_color, plot_bgcolor=bg_color, font=dict(family="Montserrat, sans-serif", size=12, color=text_color), height=750)
    fig.update_xaxes(categoryorder='array', categoryarray= categoryarray_to_push, tickangle = -50)
    fig.update_xaxes(showline=True, linewidth=2, linecolor='#77aad9', gridcolor='#77aad9')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='#77aad9', gridcolor='#77aad9')
    fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#77aad9')
    fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#77aad9')
    fig.update_yaxes(range=[-10, 110])
    return fig










# def getDataForGraph(OS, VPN, ASN, Oper, Period_begin, Period_end):
#     sqlB = "SELECT asnnumber, os_names, operator_names, week_period, week_sorting_date, vpn_android, vpn_ios, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData WHERE "
#     sqlE = " GROUP BY asnnumber, os_names, operator_names, week_period, week_sorting_date, vpn_android, vpn_ios"
     
#     if len(VPN) == 1: 
#         sqlVpn = "(vpn_android = '{}' OR vpn_ios = '{}') AND ".format(VPN[0], VPN[0])
#     else:
#         sqlVpn = "(vpn_android IN {} OR vpn_ios IN {}) AND ".format(tuple(VPN), tuple(VPN))
#     if len(ASN) == 1:
#         sqlAsn = "asnnumber = '{}' AND ".format(ASN[0])
#     else:
#         sqlAsn = "asnnumber IN {} AND ".format(tuple(ASN))
#     if len(OS) == 1:
#         sqlos = "os_names = '{}' AND ".format(OS[0])
#     else:
#         sqlos = "os_names IN {} AND ".format(tuple(OS))
#     if len(Oper) == 1:
#         sqlopr = "operator_names = '{}' AND ".format(Oper[0])
#     else:
#         sqlopr = "operator_names IN {} AND ".format(tuple(Oper))
#     sqlDate = "created >= '{}' AND created <= '{}'".format(Period_begin[0], Period_end[0])
#     conn = connectToBD()
#     sql = sqlB + sqlVpn + sqlAsn + sqlos + sqlopr + sqlDate + sqlE #  + sqlos + sqlAsn + sqlopr + sqlDate 
#     sqlBM = "SELECT week_period, week_sorting_date, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData WHERE "
#     sqlEM = " GROUP BY week_period, week_sorting_date"
#     sqlM = sqlBM + sqlVpn + sqlAsn + sqlos + sqlopr + sqlDate + sqlEM #  + sqlos + sqlAsn + sqlopr + sqlDate 
#     print(sqlM)
#     data = getData(sql, conn)
#     conn.close()
#     return createGraph(data, VPN)





@app.callback(
    Output('x-time-series', 'figure'),
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
    Input('ASN', 'value'),
    Input('OS', 'value'),
    Input('VPN', 'value'),
    Input('Oper', 'value'),
    Input('datePicker', 'start_date'),
    Input('datePicker', 'end_date'),    
    )
def updateGraph(Type, Testing_type, ASN, OS, VPN, Oper, Period_begin, Period_end): 
    if len(Oper) == 1:
        Oper = Oper[0]
    sqlB = "SELECT type, blocked, asnnumber, os_names, operator_names, week_period, week_sorting_date, vpn_android, vpn_ios, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData WHERE "
    sqlE = " GROUP BY type, blocked, asnnumber, os_names, operator_names, week_period, week_sorting_date, vpn_android, vpn_ios"
    if Type == '*':
         sqlType = ""
    else:
         sqlType = "type = '{}' AND ".format(Type)
    if Testing_type == '*':
         sqlTestingType = ""
    else:
         sqlTestingType = "blocked = '{}' AND ".format(Testing_type)
    sqlVpn = "(vpn_android = '{}' OR vpn_ios = '{}') AND ".format(VPN, VPN)
    sqlAsn = "asnnumber = '{}' AND ".format(ASN)
    if OS == 'Все':
        sqlOS = ''
    else:
        sqlOS = "os_names = '{}' AND ".format(OS)
    
    if isinstance(Oper, list):
        sqlopr = "operator_names IN {} AND ".format(tuple(Oper))
    else:
        sqlopr = "operator_names = '{}' AND ".format(Oper)
    sqlDate = "created >= '{}' AND created <= '{}'".format(Period_begin, Period_end)
    conn = connectToBD()
        
    sql = sqlB + sqlType + sqlTestingType + sqlVpn + sqlAsn + sqlOS + sqlopr + sqlDate + sqlE #  + sqlos + sqlAsn + sqlopr + sqlDate 
    
    sqlBM = "SELECT week_period, week_sorting_date, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData WHERE "
    sqlEM = " GROUP BY week_period, week_sorting_date"
     

    sqlM = sqlBM + sqlType + sqlTestingType + sqlVpn + sqlAsn + sqlOS + sqlopr + sqlDate + sqlEM #  + sqlos + sqlAsn + sqlopr + sqlDate 

    
    dataM = getData(sqlM, conn)
    dataM.sort_values(by='week_sorting_date',inplace=True)
    dataM.reset_index(drop=True, inplace=True)
    
    
    data = getData(sql, conn)
    conn.close()
    # print(sqlM)
    # print(dataM)
    return createGraph(data, VPN, dataM)







def create_table(data):
    # data_for_scatter = data
    table_data = pd.DataFrame()
    for typ in data['type'].unique():
        dataT = data[data['type'] == typ]
        for blocked in dataT['blocked'].unique():
            dataTB = dataT[dataT['blocked'] == blocked]
            for OS in dataTB['os_names'].unique():
                dataTBO = dataTB[dataTB['os_names'] == OS]
                if dataTBO.shape[0] != 0:
                    cur_dataCopy = dataTBO.copy(deep=True)
                    cur_dataCopy['operator_names'] = 'Среднее'
                    # print(cur_dataCopy)
                    cur_data = pd.concat([dataTBO, cur_dataCopy])
                    columns = []
                    testCounts = cur_data.shape[0]
                    # print(cur_data.columns)
                    for i in cur_data.columns:
                        if i in ['os_names', 'operator_names', 'type', 'blocked', 'vpn_android', 'vpn_ios']: columns.append(i)
                    cur_data = cur_data.groupby(columns).agg({'mean_web': ['mean'], 'mean_app': ['mean'], 'mean_all': ['mean']}). reset_index()
                    columns.append('mean_web')
                    columns.append('mean_app')
                    columns.append('mean_all')
                    cur_data.columns = columns
                    print(cur_data)
                    cur_data['mean_web'] = cur_data['mean_web'].round(2)
                    cur_data['mean_app'] = cur_data['mean_app'].round(2)
                    cur_data['mean_all'] = cur_data['mean_all'].round(2)
                    cur_data['Количество тестов'] = testCounts
                    cur_data_mean_web = cur_data[['operator_names','mean_web']].T.reset_index(drop=True)
                    cur_data_mean_app = cur_data[['operator_names','mean_app']].T.reset_index(drop=True)
                    cur_data_mean_all = cur_data[['operator_names','mean_all']].T.reset_index(drop=True)
                    
                    cur_data_mean_all.columns = cur_data_mean_all.iloc[0]
                    cur_data_mean_all = cur_data_mean_all.iloc[[1]]
                    cur_data_mean_all.reset_index(drop=True, inplace = True)
                    cur_data_mean_app.columns = cur_data_mean_app.iloc[0]
                    cur_data_mean_app = cur_data_mean_app.iloc[[1]]
                    cur_data_mean_app.reset_index(drop=True, inplace = True)
                    cur_data_mean_web.columns = cur_data_mean_web.iloc[0]
                    cur_data_mean_web = cur_data_mean_web.iloc[[1]]
                    cur_data_mean_web.reset_index(drop=True, inplace = True)

                    new_line_mean_all = cur_data.iloc[[0]].copy(deep=True)
                    new_line_mean_all.drop(['operator_names', 'mean_all', 'mean_web', 'mean_app'], axis=1, inplace=True)
                    new_line_mean_all.reset_index(drop=True, inplace = True)
                    new_line_mean_web = new_line_mean_all.copy(deep = True)
                    new_line_mean_app = new_line_mean_all.copy(deep = True)
                    new_line_mean_all['app_type'] = 'mean_all'
                    new_line_mean_web['app_type'] = 'mean_web'
                    new_line_mean_app['app_type'] = 'mean_app'
                    new_line_mean_all = pd.concat([new_line_mean_all, cur_data_mean_all], axis=1)
                    new_line_mean_app = pd.concat([new_line_mean_app, cur_data_mean_app], axis=1)
                    new_line_mean_web = pd.concat([new_line_mean_web, cur_data_mean_web], axis=1)
                    print(new_line_mean_all)
                    print(new_line_mean_app)
                    print(new_line_mean_web)
                    print(table_data)
                    if table_data.empty:
                        table_data = pd.concat([new_line_mean_web, new_line_mean_app, new_line_mean_all])
                    else:
                        table_data = pd.concat([table_data, new_line_mean_web, new_line_mean_app, new_line_mean_all])
                    table_data.reset_index(drop=True, inplace=True)
    cols = table_data.columns.tolist()
    cols_new = []
    for i in cols:
        if i != 'Среднее':
            cols_new.append(i)
    cols_new.append('Среднее')
    table_data = table_data[cols_new]
    return table_data
                
                
                
    
    
    # for os_name in data_for_scatter['os_names'].unique():
    #     for vpn_number in range(len(VPN_new)):
    #         # print(VPN_new[vpn_number])
    #         cur_data = data_for_scatter[((data_for_scatter['vpn_ios'] == VPN_new[vpn_number]) | 
    #                                     (data_for_scatter['vpn_android'] == VPN_new[vpn_number])) & 
    #                                     (data_for_scatter['os_names'] == os_name)]
    #         # print(cur_data)
    #         if cur_data.shape[0] != 0:
    #             # print(cur_data)
    #             cur_dataCopy = cur_data.copy(deep=True)
    #             cur_dataCopy['operator_names'] = 'Среднее'
    #             # print(cur_dataCopy)
    #             cur_data = pd.concat([cur_data, cur_dataCopy])
    #             columns = []
    #             testCounts = cur_data.shape[0]
    #             # print(cur_data.columns)
    #             for i in cur_data.columns:
    #                 if i in ['os_names', 'operator_names', 'vpn_android', 'operator_names', 'vpn_ios']: columns.append(i)
    #             cur_data = cur_data.groupby(columns).agg({'mean_web': ['mean'], 'mean_app': ['mean'], 'mean_all': ['mean']}). reset_index()

    #             columns.append('mean_web')
    #             columns.append('mean_app')
    #             columns.append('mean_all')
    #             cur_data.columns = columns
    #             cur_data['mean_web'] = cur_data['mean_web'].round(2)
    #             cur_data['mean_app'] = cur_data['mean_app'].round(2)
    #             cur_data['mean_all'] = cur_data['mean_all'].round(2)
    #             cur_data['Количество тестирований'] = testCounts
    #             # print(cur_data)
    #             cur_data_mean_web = cur_data[['operator_names','mean_web']].T.reset_index(drop=True)
    #             cur_data_mean_app = cur_data[['operator_names','mean_app']].T.reset_index(drop=True)
    #             cur_data_mean_all = cur_data[['operator_names','mean_all']].T.reset_index(drop=True)
                
    #             cur_data_mean_all.columns = cur_data_mean_all.iloc[0]
    #             cur_data_mean_all = cur_data_mean_all.iloc[[1]]
    #             cur_data_mean_all.reset_index(drop=True, inplace = True)
    #             cur_data_mean_app.columns = cur_data_mean_app.iloc[0]
    #             cur_data_mean_app = cur_data_mean_app.iloc[[1]]
    #             cur_data_mean_app.reset_index(drop=True, inplace = True)
    #             cur_data_mean_web.columns = cur_data_mean_web.iloc[0]
    #             cur_data_mean_web = cur_data_mean_web.iloc[[1]]
    #             cur_data_mean_web.reset_index(drop=True, inplace = True)

    #             new_line_mean_all = cur_data.iloc[[0]].copy(deep=True)
    #             new_line_mean_all.drop(['operator_names', 'mean_all', 'mean_web', 'mean_app'], axis=1, inplace=True)
    #             new_line_mean_all.reset_index(drop=True, inplace = True)
    #             new_line_mean_web = new_line_mean_all.copy(deep = True)
    #             new_line_mean_app = new_line_mean_all.copy(deep = True)
    #             new_line_mean_all['type'] = 'mean_all'
    #             new_line_mean_web['type'] = 'mean_web'
    #             new_line_mean_app['type'] = 'mean_app'
    #             new_line_mean_all = pd.concat([new_line_mean_all, cur_data_mean_all], axis=1)
    #             new_line_mean_app = pd.concat([new_line_mean_app, cur_data_mean_app], axis=1)
    #             new_line_mean_web = pd.concat([new_line_mean_web, cur_data_mean_web], axis=1)
    #             if table_data.empty:
    #                 table_data = pd.concat([new_line_mean_web, new_line_mean_app, new_line_mean_all])
    #             else:
    #                 table_data = pd.concat([table_data, new_line_mean_web, new_line_mean_app, new_line_mean_all])
    # # print(table_data)
    # # table_data.sort_values(by='sorting_date', inplace=True)
    # table_data.reset_index(drop=True, inplace=True)
    # cols = table_data.columns.tolist()
    # cols_new = []
    # for i in cols:
    #     if i != 'Среднее':
    #         cols_new.append(i)
    # cols_new.append('Среднее')
    # table_data = table_data[cols_new]
    # return table_data




@app.callback(
    Output('z-time-series', 'children'),
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
    Input('ASN', 'value'),
    Input('OS', 'value'),
    Input('VPN', 'value'),
    Input('Oper', 'value'),
    Input('datePicker', 'start_date'),
    Input('datePicker', 'end_date'),    
    )
def update_k_timeseries(Type, Testing_type, ASN, OS, VPN, Oper, Period_begin, Period_end): # City, 
    if len(Oper) == 1:
        Oper = Oper[0]
    sqlB = "SELECT type, blocked, asnnumber, os_names, operator_names, week_period, week_sorting_date, vpn_android, vpn_ios, AVG(mean_all) as mean_all, AVG(mean_web) as mean_web, AVG(mean_app) as mean_app from asnData WHERE "
    sqlE = " GROUP BY type, blocked, asnnumber, os_names, operator_names, week_period, week_sorting_date, vpn_android, vpn_ios"
    if Type == '*':
         sqlType = ""
    else:
         sqlType = "type = '{}' AND ".format(Type)
    if Testing_type == '*':
         sqlTestingType = ""
    else:
         sqlTestingType = "blocked = '{}' AND ".format(Testing_type)
    sqlVpn = "(vpn_android = '{}' OR vpn_ios = '{}') AND ".format(VPN, VPN)
    sqlAsn = "asnnumber = '{}' AND ".format(ASN)
    if OS == 'Все':
        sqlOS = ''
    else:
        sqlOS = "os_names = '{}' AND ".format(OS)
    
    if isinstance(Oper, list):
        sqlopr = "operator_names IN {} AND ".format(tuple(Oper))
    else:
        sqlopr = "operator_names = '{}' AND ".format(Oper)
    sqlDate = "created >= '{}' AND created <= '{}'".format(Period_begin, Period_end)
    conn = connectToBD()
        
    sql = sqlB + sqlType + sqlTestingType + sqlVpn + sqlAsn + sqlOS + sqlopr + sqlDate + sqlE #  + sqlos + sqlAsn + sqlopr + sqlDate 
    
    
    data = getData(sql, conn)
    conn.close()


    tab = create_table(data)
    # tab = tab[tab['type'] == 'mean_all']
    # tab.drop('type', axis=1, inplace=True)
    fug = [dash_table.DataTable(tab.to_dict('records'), [{"name": i, "id": i} for i in tab.columns], 
                                page_size=10,
                                )]

    return fug











@app.callback(
    Output('ASN', 'options'),
    Output('ASN', 'value'),
    
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
)
def updateASNNames(Type, Testing_type):
    conn = connectToBD()
    if Type == '*' and Testing_type == '*':
        data = getData("SELECT asnnumber FROM asndata", conn)['asnnumber'].unique()
    elif Type == '*' and Testing_type != '*':
        data = getData("SELECT asnnumber FROM asndata WHERE blocked = '{}'".format(Testing_type), conn)['asnnumber'].unique()
    elif Type != '*' and Testing_type == '*':
        data = getData("SELECT asnnumber FROM asndata WHERE type = '{}'".format(Type), conn)['asnnumber'].unique()
    else:
        data = getData("SELECT asnnumber FROM asndata WHERE type = '{}' AND blocked = '{}'".format(Type, Testing_type), conn)['asnnumber'].unique()
    conn.close()
    data.sort()
    return data, data[0]
        

@app.callback(
    Output('OS', 'options'),
    Output('OS', 'value'),
    
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
    Input('ASN', 'value'),
)
def updateOSNames(Type, Testing_type, ASN):
    conn = connectToBD()
    if Type == '*' and Testing_type == '*':
        data = getData("SELECT os_names FROM asndata WHERE asnnumber = '{}'".format(ASN), conn)['os_names'].unique()
    elif Type == '*' and Testing_type != '*':
        data = getData("SELECT os_names FROM asndata WHERE blocked = '{}' AND asnnumber = '{}'".format(Testing_type, ASN), conn)['os_names'].unique()
    elif Type != '*' and Testing_type == '*':
        data = getData("SELECT os_names FROM asndata WHERE type = '{}' AND asnnumber = '{}'".format(Type, ASN), conn)['os_names'].unique()
    else:
        data = getData("SELECT os_names FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}'".format(Type, Testing_type, ASN), conn)['os_names'].unique()
    conn.close()
    data.sort()
    if len(data) == 2:
        data = ['Все', 'Android', 'IOS']
    return data, data[0]


@app.callback(
    Output('VPN', 'options'),
    Output('VPN', 'value'),
    
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
    Input('ASN', 'value'),
    Input('OS', 'value'),
)
def updateVpnNames(Type, Testing_type, ASN, OS):
    conn = connectToBD()
    if Type == '*' and Testing_type == '*':
        if OS != 'Все':
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE asnnumber = '{}' AND os_names = '{}'".format(ASN, OS), conn).drop_duplicates()
        else:
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE asnnumber = '{}'".format(ASN), conn).drop_duplicates()
    elif Type == '*' and Testing_type != '*':
        if OS != 'Все':
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND os_names = '{}'".format(Testing_type, ASN, OS), conn).drop_duplicates()
        else:
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE blocked = '{}' AND asnnumber = '{}'".format(Testing_type, ASN), conn).drop_duplicates()
    elif Type != '*' and Testing_type == '*':
        if OS != 'Все':
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND os_names = '{}'".format(Type, ASN, OS), conn).drop_duplicates()
        else:
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE type = '{}' AND asnnumber = '{}'".format(Type, ASN), conn).drop_duplicates()
    else:
        if OS != 'Все':
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND os_names = '{}'".format(Type, Testing_type, ASN, OS), conn).drop_duplicates()
        else:
            data = getData("SELECT vpn_ios, vpn_android FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}'".format(Type, Testing_type, ASN), conn).drop_duplicates()
    conn.close()
    # print(data)
    data = vpnCount(data)['vpn_android'].unique()
    data.sort()
    return data, data[0]


@app.callback(
    Output('Oper', 'options'),
    Output('Oper', 'value'),
    
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
    Input('ASN', 'value'),
    Input('OS', 'value'),
    Input('VPN', 'value'),
)
def updateOperNames(Type, Testing_type, ASN, OS, VPN):
    conn = connectToBD()
    if Type == '*' and Testing_type == '*':
        if OS != 'Все':
            data = getData("SELECT operator_names FROM asndata WHERE asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(ASN, OS, VPN, VPN), conn)['operator_names'].unique()
        else:
            data = getData("SELECT operator_names FROM asndata WHERE asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(ASN, VPN, VPN), conn)['operator_names'].unique()
    elif Type == '*' and Testing_type != '*':
        if OS != 'Все':
            data = getData("SELECT operator_names FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(Testing_type, ASN, OS, VPN, VPN), conn)['operator_names'].unique()
        else:
            data = getData("SELECT operator_names FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(Testing_type, ASN, VPN, VPN), conn)['operator_names'].unique()
    elif Type != '*' and Testing_type == '*':
        if OS != 'Все':
            data = getData("SELECT operator_names FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(Type, ASN, OS, VPN, VPN), conn)['operator_names'].unique()
        else:
            data = getData("SELECT operator_names FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(Type, ASN, VPN, VPN), conn)['operator_names'].unique()
    else:
        if OS != 'Все':
            data = getData("SELECT operator_names FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(Type, Testing_type, ASN, OS, VPN, VPN), conn)['operator_names'].unique()
        else:
            data = getData("SELECT operator_names FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}')".format(Type, Testing_type, ASN, VPN, VPN), conn)['operator_names'].unique()
    conn.close()
    data.sort()
    return data, data[0]


@app.callback(
    Output('datePicker', 'min_date_allowed'),
    Output('datePicker', 'max_date_allowed'),
    Output('datePicker', 'initial_visible_month'),
    Output('datePicker', 'start_date'),
    Output('datePicker', 'end_date'),
    
    Input('Type', 'value'),
    Input('Testing_type', 'value'),
    Input('ASN', 'value'),
    Input('OS', 'value'),
    Input('VPN', 'value'),
    Input('Oper', 'value'),
)
def updateDatesNames(Type, Testing_type, ASN, OS, VPN, Oper):
    conn = connectToBD()
    print(Oper)
    if len(Oper) == 1:
        Oper = Oper[0]
    print(Oper)
    if isinstance(Oper, list):
        if Type == '*' and Testing_type == '*':
            if OS != 'Все':
                data = getData("SELECT created FROM asndata WHERE asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(ASN, OS, VPN, VPN, tuple(Oper)), conn)['created'].unique()
            else:
                data = getData("SELECT created FROM asndata WHERE asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(ASN, VPN, VPN, tuple(Oper)), conn)['created'].unique()
        elif Type == '*' and Testing_type != '*':
            if OS != 'Все':
                data = getData("SELECT created FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(Testing_type, ASN, OS, VPN, VPN, tuple(Oper)), conn)['created'].unique()
            else:
                data = getData("SELECT created FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(Testing_type, ASN, VPN, VPN, tuple(Oper)), conn)['created'].unique()
        elif Type != '*' and Testing_type == '*':
            if OS != 'Все':
                data = getData("SELECT created FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(Type, ASN, OS, VPN, VPN, tuple(Oper)), conn)['created'].unique()
            else:
                data = getData("SELECT created FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(Type, ASN, VPN, VPN, tuple(Oper)), conn)['created'].unique()
        else:
            if OS != 'Все':
                data = getData("SELECT created FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(Type, Testing_type, ASN, OS, VPN, VPN, tuple(Oper)), conn)['created'].unique()
            else:
                data = getData("SELECT created FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names IN {}".format(Type, Testing_type, ASN, VPN, VPN, tuple(Oper)), conn)['created'].unique()

    else:
        if Type == '*' and Testing_type == '*':
            if OS != 'Все':
                data = getData("SELECT sorting_date FROM asndata WHERE asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(ASN, OS, VPN, VPN, Oper), conn)['sorting_date'].unique()
            else:
                data = getData("SELECT sorting_date FROM asndata WHERE asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(ASN, VPN, VPN, Oper), conn)['sorting_date'].unique()
        elif Type == '*' and Testing_type != '*':
            if OS != 'Все':
                data = getData("SELECT sorting_date FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(Testing_type, ASN, OS, VPN, VPN, Oper), conn)['sorting_date'].unique()
            else:
                data = getData("SELECT sorting_date FROM asndata WHERE blocked = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(Testing_type, ASN, VPN, VPN, Oper), conn)['sorting_date'].unique()
        elif Type != '*' and Testing_type == '*':
            if OS != 'Все':
                data = getData("SELECT sorting_date FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(Type, ASN, OS, VPN, VPN, Oper), conn)['sorting_date'].unique()
            else:
                data = getData("SELECT sorting_date FROM asndata WHERE type = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(Type, ASN, VPN, VPN, Oper), conn)['sorting_date'].unique()
        else:
            if OS != 'Все':
                data = getData("SELECT sorting_date FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND os_names = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(Type, Testing_type, ASN, OS, VPN, VPN, Oper), conn)['sorting_date'].unique()
            else:
                data = getData("SELECT sorting_date FROM asndata WHERE type = '{}' AND blocked = '{}' AND asnnumber = '{}' AND (vpn_ios = '{}' OR vpn_android = '{}') AND operator_names = '{}'".format(Type, Testing_type, ASN, VPN, VPN, Oper), conn)['sorting_date'].unique()
    conn.close()
    data.sort()
    return data[0], data[len(data)-1], data[len(data)-1], data[0], data[len(data)-1], 

# AS12958


if __name__ == '__main__':

    app.run_server(debug=True, port='16600')