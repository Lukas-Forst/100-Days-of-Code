from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

try:
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me').execute()#.labels().list(userId='me').execute()

    messages = results.get('messages', [])
    #print(results)
    all_data = [service.users().messages().get(userId='me', id=msg['id'], format="full").execute() for msg in messages]
    with open('data_full.json', 'w') as f:
        json.dump(all_data, f)
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

