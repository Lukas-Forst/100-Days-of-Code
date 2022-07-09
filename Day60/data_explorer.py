import json
import base64
from email.parser import BytesParser, Parser
from email.policy import default
import pickle
import os.path
import base64
import email
import pandas as pd
import lxml
from bs4 import BeautifulSoup
from transformers import pipeline

f = open('data_full.json')
data = json.load(f)
###


messages = data
sender_stat = []
date_stat = []
label_stat = []
list_dict = []
for msg in messages:
    # Get the message from its id


    # Use try-except to avoid any Errors
    try:
        # Get value of 'payload' from dictionary 'txt'
        payload = msg['payload']
        data_dict = {}
        cat = [i for i in msg['labelIds'] if 'CATEGORY_' in i]
        #label_stat.append(cat[0])
        data_dict['label'] = cat[0]
        headers = payload['headers']

        # Look for Subject and Sender Email in the headers
        for d in headers:
            if d['name'] == 'Subject':
                #subject = d['value']
                data_dict['subject'] = d['value']
            if d['name'] == 'From':
                #sender = d['value']
                #sender_stat.append(sender)
                data_dict['sender'] =  d['value']
            if d['name'] == 'Date':
                #date = d['value']
                #date_stat.append(date)
                data_dict['date'] = d['value']

            # data_dict['id'] = i
            # print(i)
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        # The Body of the message is in Encrypted format. So, we have to decode it.
        # Get the data and decode it with base 64 decoder.
        parts = payload.get('parts')[0]
        data = parts['body']['data']
        data = data.replace("-", "+").replace("_", "/")
        decoded_data = base64.b64decode(data)

        # Now, the data obtained is in lxml. So, we will parse
        # it with BeautifulSoup library
        soup = BeautifulSoup(decoded_data, "lxml")
        body = soup.body(text=True)[0]
        list_dict.append(data_dict)
        print(body)
        # Printing the subject, sender's email and message
        print(type(body))
        #print(test)
        #print(body.get_text())
        #summary = summarizer(str(body), max_length=130, min_length=30)
        #print(summary)
        #print("Subject: ", subject)
        #print("From: ", sender)
        #print("Message: ", body)
        #print("\n")
    except Exception as e:
        print(f"Error occured in {e}")
        pass


#data_dict = {}
#print(sender_stat, date_stat)


#print(list_dict)

#df = pd.DataFrame(list_dict)
#df.to_csv('sender.csv')
#print(df.head())