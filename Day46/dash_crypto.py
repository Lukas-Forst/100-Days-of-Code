from datetime import datetime

import pandas as pd
import os
import dash_daq as daq
from dash import Dash, dcc, html, Input, Output, dash_table, no_update
import plotly.express as px

files = ["./archive/" + i for i in os.listdir('./archive')]

df = pd.concat(
    map(pd.read_csv, files), ignore_index=True)

# print(df.columns)
df['year'] = pd.DatetimeIndex(df['Date']).year
# df.columns = Index(['SNo', 'Name', 'Symbol', 'Date', 'High', 'Low', 'Open', 'Close',
#       'Volume', 'Marketcap'],
df_n = df.groupby(by="Symbol")
df["Key"]=df['Date']+df['Symbol']
#print(df['Key'])
blue_chip = ["BTC", "ETH", "BNB"]
df_small = df[~df["Symbol"].isin(blue_chip)]
df_test = df_small.groupby(by="Symbol")
# print(df.columns)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#print(df['Name'].unique())

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(className="row", children=[
    html.H1("Crypto Dashboard"),
    dcc.Graph(id='graph-with-slider'),

    html.Div(id='dark-theme-container', children=[
        dcc.Graph(id='scatter-with-slider',
                  style={'display': 'inline-block', 'width': '50%', 'background-color': 'black'}),
        dcc.Graph(id="small-graph-with-slider",
                  style={'display': 'inline-block', 'width': '50%', 'background-color': 'black'})]),
    dcc.Tooltip(id="graph-tooltip"),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].max(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        filter_action='native',
        style_table={
            'height': 400,
            'background-color': 'black'
        },
        style_data={
            'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'background-color': 'black'
        },
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_filter={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        columns=[{'id': c, 'name': c} for c in df.columns],

        style_as_list_view=True,
    ),

], style={'text-align': 'center', 'font-size': 22,
          # Update the background color to the entire app
          'background-color': 'black',
          # Change the text color for the whole app
          'color': 'white'
          })


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
# Input('xaxis-column', 'value') xaxis_column_name

def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.line(filtered_df, x="Date", y="Marketcap",
                  color="Symbol", template="plotly_dark", hover_name="Name")

    fig.update_layout(transition_duration=500)

    return fig


@app.callback(
    Output('small-graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
# Input('xaxis-column', 'value') xaxis_column_name

def update_figure_small(selected_year):
    # print(df_test.columns)
    df_filtered = df_small[df_small.year == selected_year]
    filtered_df = df_filtered.groupby(by="Symbol")['Marketcap'].mean()
    #print(filtered_df.values)
    #print(pd.DataFrame(filtered_df))
    fig_bar = px.bar(x=filtered_df.index,
                     y=filtered_df.values,
                     color=filtered_df.index,
                     labels={"x": "Symbol", "y": "Marketcap"},
                     title=f"Mean marketcap in {selected_year}",
                     template="plotly_dark")

    fig_bar.update_layout(transition_duration=500)

    return fig_bar


@app.callback(
    Output('scatter-with-slider', 'figure'),
    Input('year-slider', 'value'))
# Input('xaxis-column', 'value') xaxis_column_name

def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    #print(filtered_df)
    fig = px.scatter(filtered_df,
                     y="Volume",
                     x="Marketcap",
                     color="Symbol",
                     hover_name="Name",
                     title=f"Volume and marketcap of coins in {selected_year}",
                     template="plotly_dark",
                     hover_data={'Key'})

    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input('scatter-with-slider', 'hoverData'),
    Input('year-slider', 'value')
)

def display_tip(hoverData, selected_year):
    if hoverData is None:
        return False, no_update, no_update
    coins =  ['AAVE', 'BNB', 'BTC', 'ADA', 'LINK', 'ATOM', 'CRO', 'DOGE', 'EOS', 'ETH', 'MIOTA',
     'LTC', 'XMR', 'XEM', 'DOT', 'SOL', 'XLM', 'USDT', 'TRX', 'UNI', 'USDC', 'WBTC',
     'XRP']
    df_n = df[df.year == selected_year]
    df_n = df_n.reset_index(drop=True)
    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]
    #print(pt, hoverData)
    cust = pt['customdata'][0]

    #print(hoverData, cust)
    #print(df_n[(df_n['Key']==cust)])
    src_dict = {
        'AAVE':7278,
        'BNB':1839,
        'BTC':1,
        'ADA':2010,
        'LINK':1975,
        'ATOM':3794,
        'CRO':3635,
        'DOGE':74,
        'EOS':1765,
        'ETH':1027,
        'MIOTA':1720,
         'LTC':2, 'XMR':328,
        'XEM':873, 'DOT':6636, 'SOL':5426,
        'XLM':512, 'USDT':825, 'TRX':1985, 'UNI':7083, 'USDC':3408, 'WBTC':3717,
         'XRP':52
    }


    df_row = df_n[(df_n['Key']==cust)]
    name = df_row['Name'].values[0]
    Date = df_row['Date'].values[0]
    Mcap = df_row['Marketcap'].values[0]
    vol = df_row['Volume'].values[0]
    src = df_row['Symbol'].values[0]
    #print(src)
    day =datetime.strptime(Date, '%Y-%m-%d %H:%M:%S').strftime("%d")
    month = datetime.strptime(Date, '%Y-%m-%d %H:%M:%S').strftime("%B")
    url = [f"https://s2.coinmarketcap.com/static/img/coins/64x64/{src_dict[i]}.png" for i in src_dict.keys() if src.lower() == i.lower()]
    children = [
        html.Div([
            #html.Img(src=img_src, style={"width": "100%"}),
            html.Div([html.Img(src=f"{url[0]}", style={"float":"left"}),  html.P(f"{name}", style={"color": "darkblue","margin":"0px"})],
                     style={"display":"inline"}),

            html.P(f"{day}, {month}"),
            html.P(f"{Mcap}"),
            html.P(f"{vol}"),
        ], style={'width': '200px', 'white-space': 'normal', 'color':'black'})
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True)
