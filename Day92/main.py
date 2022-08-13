import streamlit as st
import pandas as pd
#import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objects as go

st.write("""
#  Notion Dashboard
Viz of different Notion dbs
""")

df = pd.read_csv('habits.csv')


for index, row in df.iterrows():
    df.loc[index,'count'] = int(row['Sleep'])+int(row['Journaling'])+ int(row['Coden'])+ int(row['dehnen'])+int(row['Training'])+int(row['SAVERS'])

df_week = df.groupby(by="Week")['count'].sum()
st.write(df_week.head())


fig = px.line(df_week, y=df_week.values, x=df_week.index.values, title='Life expectancy in Canada')
st.plotly_chart(fig)

####
# Current Week stats
####


curr_week = datetime.datetime.now().isocalendar().week
curr_last_week = curr_week-1 if curr_week != 1 else 53
df_curr_week = df[df['Week'] == curr_week]
df_last_week  = df[df['Week'] == curr_last_week]
st.write("Current Week metrics")
col1, col2, col3 = st.columns(3)
delta_sleep = df_curr_week['Sleep'].sum() - df_last_week['Sleep'].sum()
print(delta_sleep)
cols = ['Sleep', 'Journaling', 'Coden', 'dehnen','Training','SAVERS']
for colum in range(1,len(cols)+1):
    val = colum
    current_column = cols[colum-1]
    delta = df_curr_week[current_column].sum() - df_last_week[current_column].sum()
    print(current_column, delta, df_curr_week[current_column].sum() , df_last_week[current_column].sum())
    if val % 3 == 0:
        col1.metric(current_column,df_curr_week[current_column].sum(), f"{int(delta)} change")
    if val % 3 == 1:
        col2.metric(current_column, df_curr_week[current_column].sum(), f"{int(delta)} change")
    if val % 3 == 2:
        col3.metric(current_column, df_curr_week[current_column].sum(), f"{int(delta)} change")

st.write()
st.write()
st.write("# Heatmap weekly overview of habits")

fig_heat = go.Figure(data=go.Heatmap(
                   z=df['count'].values,
                   x=df['Weekday'].values,
                   y=df['Week'].values,
                   hoverongaps = False))
st.plotly_chart(fig_heat)