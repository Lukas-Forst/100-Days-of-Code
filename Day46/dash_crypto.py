
import pandas as pd
import os
import dash_daq as daq
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
files = ["./archive/"+i for i in os.listdir('./archive')]


df = pd.concat(
    map(pd.read_csv, files), ignore_index=True)

#print(df.columns)
df['year'] = pd.DatetimeIndex(df['Date']).year
#df.columns = Index(['SNo', 'Name', 'Symbol', 'Date', 'High', 'Low', 'Open', 'Close',
#       'Volume', 'Marketcap'],
df_n = df.groupby(by="Symbol")
blue_chip = ["BTC","ETH","BNB"]
df_small = df[~df["Symbol"].isin(blue_chip)]
df_test = df_small.groupby(by="Symbol")
#print(df.columns)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(className="row", children=[
        html.H1("Crypto Dashboard"),
        dcc.Graph(id='graph-with-slider'),

html.Div(id='dark-theme-container',children=[
        dcc.Graph(id='scatter-with-slider',style={'display': 'inline-block','width':'50%', 'background-color':'black'}),
        dcc.Graph(id="small-graph-with-slider",style={'display': 'inline-block','width':'50%', 'background-color':'black'})]),

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
        'background-color':'black'
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'background-color':'black'
    },
    columns=[{'id': c, 'name': c} for c in df.columns],


    style_as_list_view=True,
),

], style={'text-align':'center', 'font-size':22,
              # Update the background color to the entire app
              'background-color':'black',
              # Change the text color for the whole app
              'color':'white'
               })



@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
   # Input('xaxis-column', 'value') xaxis_column_name

def update_figure(selected_year ):
    filtered_df = df[df.year == selected_year]

    fig = px.line(filtered_df, x="Date", y="Marketcap",
                     color="Symbol", hover_name="Name")

    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('small-graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
   # Input('xaxis-column', 'value') xaxis_column_name

def update_figure_small(selected_year ):
    #print(df_test.columns)
    df_filtered = df_small[df_small.year == selected_year]
    filtered_df = df_filtered.groupby(by="Symbol")['Marketcap'].mean()
    print(filtered_df.values)
    print(pd.DataFrame(filtered_df))
    fig_bar = px.bar(x=filtered_df.index,
                     y=filtered_df.values,
                     color=filtered_df.index,
                     labels={"x":"Symbol", "y":"Marketcap"},
                     title=f"Mean marketcap in {selected_year}")

    fig_bar.update_layout(transition_duration=500)

    return fig_bar

@app.callback(
    Output('scatter-with-slider', 'figure'),
    Input('year-slider', 'value'))
   # Input('xaxis-column', 'value') xaxis_column_name

def update_figure(selected_year ):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, y="Volume", x="Marketcap",
                     color="Symbol", hover_name="Name")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)