
import pandas as pd
import os

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


print(len(df_n))
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
        html.H1("Crypto Dashboard"),

        dcc.Graph(id='graph-with-slider'),
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
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },
    columns=[{'id': c, 'name': c} for c in df.columns],
    

    style_as_list_view=True,
)



])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
   # Input('xaxis-column', 'value') xaxis_column_name

def update_figure(selected_year ):
    filtered_df = df[df.year == selected_year]
    #print(xaxis_column_name)
   # print(filtered_df[filtered_df['Symbol'] == xaxis_column_name]["Symbol"].head())
    fig = px.line(filtered_df, x="Date", y="Marketcap",
                     color="Symbol", hover_name="Name")

    fig.update_layout(transition_duration=500)

    return fig




if __name__ == "__main__":
    app.run_server(debug=True)