import streamlit as st
import pandas as pd
#import seaborn as sns
import json
import requests
import matplotlib.pyplot as plt
token = ""
database_id = ""

st.write("""
#  Notion Dashboard
Viz of different Notion dbs
""")
def mapNotionResult(result):
  # you can print result here and check the format of the answer.
    id_ = result['id']
    properties = result['properties']
    #print(result)
    Sleep = properties['😴7+ hrs Sleep']['checkbox']
    Journaling = properties['✍🏼Journaling']['checkbox']
    Coden = properties['Coden']['checkbox']
    dehnen = properties['Dehnen']['checkbox']
    Training = properties['Training']['checkbox']
    SAVERS = properties['SAVERS']['checkbox']
    # check for none
    if properties['Date']['date'] != None:
        Date = properties['Date']['date']['start']
    else:
        Date = properties['Date']['date']#['start']
    return {
    'Date': Date,
    'Sleep': Sleep,
    'Journaling': Journaling,
    'Coden': Coden,
    'dehnen': dehnen,
    "Training": Training,
    "SAVERS": SAVERS
    }

def getData():
    url = f'https://api.notion.com/v1/databases/{database_id}/query'

    r = requests.post(url, headers={
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2021-08-16"
  })

    result_dict = r.json()
    list_result = result_dict['results']

    data = []

    for day in list_result:

        _dict = mapNotionResult(day)
        data.append(_dict)

    return data

habits = getData()
habits = [habit for habit in habits if habit['Date']!=None]
df = pd.DataFrame(habits)


for index, row in df.iterrows():
    df.loc[index,'count'] = int(row['Sleep'])+int(row['Journaling'])+ int(row['Coden'])+ int(row['dehnen'])+int(row['Training'])+int(row['SAVERS'])
fig, ax = plt.subplots()
ax.bar(df.Date.values, df['count'].values,width=0.5)
st.pyplot(fig)
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")