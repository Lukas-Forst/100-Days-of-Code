from __future__ import print_function

import os.path
import matplotlib.pyplot as plt
import seaborn as sns
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import pandas as pd
import lxml
import base64
from email.parser import BytesParser, Parser
from email.policy import default
import pickle
import os.path
import base64
import email
import re
from bs4 import BeautifulSoup
from transformers import pipeline

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

try:
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', q="newer_than:8d", maxResults=10).execute()#.labels().list(userId='me').execute()
    #print(results)
    messages = results.get('messages', [])
    #print(results)
    all_data = [service.users().messages().get(userId='me', id=msg['id'], format="full").execute() for msg in messages]
    df = pd.DataFrame(all_data)
    #print(df.head())
    #df.to_csv('first_test.csv')

    #print(len(all_data))
    #summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    #with open('data_full_7d_unread.json', 'w') as f:
    #    json.dump(all_data, f)
    #json.dumps(all_data)
        #print(key)
    #for i in messages[0]:
    #    print(i)
    #    print(i)
        #results.get(int(i['id']))
    #print(results.get())
    """
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__',
     '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
      '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
       '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__',
        '__weakref__', '_add_basic_methods', '_add_nested_resources', '_add_next_methods',
         '_baseUrl', '_developerKey', '_dynamic_attrs', '_http', '_model', '_requestBuilder',
          '_resourceDesc', '_rootDesc', '_schema', '_set_dynamic_attr', '_set_service_methods',
           'attachments', 'batchDelete', 'batchModify', 'close', 'delete', 'get', 'import_',
            'insert', 'list', 'list_next', 'modify', 'send', 'trash', 'untrash']
    """


    #labels = results.get('labels', [])

except Exception as e:
    print (f"An error occured {e}")

#GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages
def return_label(li):
    #print(li)
    #print(type(li))
    return [i for i in li if 'CATEGORY_' in i][0]

def fill_cols(dataframe):
    # Use try-except to avoid any Errors
    sender_stat = []
    date_stat = []
    label_stat = []
    list_dict = []
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    try:
        #payload = dataframe['payload']
        #print(dataframe.columns)
        dataframe['labelIds'] = dataframe['labelIds'].apply(lambda x: return_label(x))
        #print(dataframe['labelIds'])
        #headers = payload['headers']
        #print(dataframe['payload'][0]['headers'])
        headers = 0
        for index, val in dataframe.iterrows():
            # print(val)
            for i in dict(val)['payload']['headers']:
                #print(i)
                subject = None

                if i['name'] == 'Subject':
                    dataframe.loc[index,'subject'] = i['value']
                    subject= i['value']
                if i['name'] == 'From':
                    dataframe.loc[index,'sender'] = i['value']
                if i['name'] == 'Date':
                    dataframe.loc[index,'date'] = i['value']
            #print('here?', val['payload']['headers'])
            #print(val['payload'], val['payload'].keys())

            #print('body?', soup.body)
            try:
                parts = val['payload'].get('parts')[0]

                data = parts['body']['data']
                data = data.replace("-", "+").replace("_", "/")
                decoded_data = base64.b64decode(data)
                soup = BeautifulSoup(decoded_data, "lxml")
                body = soup.body(text=True)[0]
                #dataframe['name'] = dataframe['payload'].
                # Look for Subject and Sender Email in the headers
                #print('Parts?')
                body = str(body)
                # body = body.replace("\n"," ")
                text = body.replace("\r\n", "")
                text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text,
                                  flags=re.MULTILINE)
                tokens = text.split(" ")
                trun_token = ' '.join(tokens[:200])
                # stocks = body.replace("\r\n", "")
                # print(len(text), text)

                summary = summarizer(str(trun_token), max_length=100, min_length=30)
                dataframe.loc[index,'summary'] = summary[0]["summary_text"]
                #list_dict.append(data_dict)
            except Exception as e:
                if subject:
                    dataframe.loc[index,'summary'] = subject#val['subject']
                else:
                    dataframe.loc[index, 'summary'] = val['snippet']
                #list_dict.append(data_dict)
                print(e)
                pass

    except Exception as e:
        print(e)
        pass
    dataframe = dataframe.drop(['payload'], axis=1)
    return dataframe

df_n = fill_cols(df)
df_n['date'] = df_n['date'].apply(lambda x: pd.to_datetime(x, utc=True))
sns.set(rc={'figure.figsize':(11.7,8.27)})
plot = sns.barplot(x=df_n.sender.value_counts().index, y=df_n.sender.value_counts().values)
plot.tick_params(axis='x', rotation=90)
plot.figure.savefig('foo1.png')
df_n['day'] =df_n['date'].apply(lambda x: x.strftime("%d"))
df_n['day_name'] =df_n['date'].apply(lambda x: x.strftime("%a"))
df_n['month'] = df_n['date'].apply(lambda x: x.strftime("%m"))

labels = ['CATEGORY_PROMOTIONS','CATEGORY_SOCIAL','CATEGORY_UPDATES']
datalist = []
df_new_d = df_n.groupby(by=['day','labelIds']).count()
df_new_d = df_n.reset_index()
print(df_n.day.unique())
for day in df_n.day.unique():
    if int(day) > 0:
        value1 = df_new_d[(df_new_d['labelIds']==labels[0]) & (df_new_d['day']==day)]['sender'].values[0]
        value2 = df_new_d[(df_new_d['labelIds']==labels[1]) & (df_new_d['day']==day)]['sender'].values[0]
        value3 = df_new_d[(df_new_d['labelIds']==labels[2]) & (df_new_d['day']==day)]['sender'].values[0]
        datalist.append([day,value1,value2,value3])

df_viz = pd.DataFrame(datalist, columns=['day','CATEGORY_PROMOTIONS','CATEGORY_SOCIAL','CATEGORY_UPDATES'])
plt = df_viz.plot(x='day', kind='bar', stacked=True,
        title='Stacked Bar Graph by dataframe')
plt.savefig('foo.png')

df_n.to_csv("first_test.csv", encoding="utf-8")
