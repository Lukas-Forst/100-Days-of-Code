import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json


with open("data.json", "r") as file:
    data = json.load(file)

list_ = []
for i in range(len(data['data'])):
    cryp_dict = {}
    cryp_dict['symbol'] = data['data'][i]['symbol']
    cryp_dict['max_supply'] = data['data'][i]['max_supply']
    cryp_dict['circulating_supply'] = data['data'][i]['circulating_supply']
    cryp_dict['total_supply'] = data['data'][i]['total_supply']
    cryp_dict['market_cap'] = data['data'][i]['quote']['USD']['market_cap']
    cryp_dict['price'] = data['data'][i]['quote']['USD']['price']
    cryp_dict['volume_24h'] = data['data'][i]['quote']['USD']['volume_24h']
    cryp_dict['percent_change_24h'] = data['data'][i]['quote']['USD']['percent_change_24h']
    cryp_dict['percent_change_7d'] = data['data'][i]['quote']['USD']['percent_change_7d']
    cryp_dict['percent_change_30d'] = data['data'][i]['quote']['USD']['percent_change_30d']
    cryp_dict['percent_change_60d'] = data['data'][i]['quote']['USD']['percent_change_60d']
    list_.append(cryp_dict)


df = pd.DataFrame(list_)


app = dash.Dash()
fig = px.bar(
    df,
    x="symbol",
    y="market_cap",
    hover_name="symbol",
    color="symbol"
)

app.layout = html.Div([html.H1("My Crypto Dashboard", style={"color": "#011833"}),dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)