#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:25:58 2020

@author: root
"""

from __future__ import print_function
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from datetime import datetime , timedelta
from email.mime.text import MIMEText
import base64
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request




iterations = 0

post_timing = []
post_hoods = []
post_title_texts = []
sqfts = []
post_links = []
post_prices = []


request= 'https://newjersey.craigslist.org/search/jjj'
response = get('https://newjersey.craigslist.org/search/jjj')

subject = 'Craiglist delivery job posting email.'
sender_address = 'easynapkin@gmail.com'
receiver_address = 'johnuzunkopru@gmail.com'


if response.status_code != 200:
    warn('Request: {}, status_code: {}'.format(request, response.status_code ))
    
    
    #define the html text
page_html = BeautifulSoup(response.text, 'html.parser')
    
    #define the posts
posts = page_html.find_all('li', class_= 'result-row')

current_datetime=datetime.now()


def findthejob():    
    for post in posts:
        post_title = post.find('a', class_='result-title hdrlnk')
        post_title_text=post_title.text.lower()
     
        post_datetime_str = post.find('time', class_= 'result-date')['datetime']
        post_datetime =datetime.strptime(post_datetime_str, '%Y-%m-%d %H:%M')
        
        test_list = ['delivery','driver']
        res = list(filter(lambda x:  x in post_title_text, test_list))
        post_link = post_title ['href']
        
        # post_title_texts.append(post_title_text)
        
        if len(res)  > 1  and (current_datetime - timedelta(hours=6) <= post_datetime) :
            print('OK')
            
            post_title_texts.append(post_title_text)
            post_timing.append(post_datetime_str)
            post_links.append(post_link)
   # else:
    #     print ('NO')
        
  

    

def create_html():
        html1 = ""
        for i in post_title_texts:
            html1 += """<div class='container'>{0}</div><br>""".format(i)
            
        html2 = ""
        for i in post_timing:
            html2 += """<div class='container'>{0}</div><br>""".format(i)
        
        html3 = ""
        for i in post_links:
            html3 += """<div class='container'>{0}</div><br>""".format(i)    



        email_content = """
            <html>
            <head>
              <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
              <title>Title</title>
              <style type="text/css">
                .some-style {{
                   some-css: rules;
                }}
              </style>
            </head>
            <body> 
                {0}<br>
                {1}<br>
                {2}<br>
            </body>
           </html>
            """.format(html1,html2,html3)
            
        return email_content




# message = MIMEMultipart()

# #The body and the attachments for the mail
# message.attach(MIMEText(email_content, 'html'))


def create_message(sender_address, receiver_address , subject, email_content):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(email_content, 'html')
  message['to'] = receiver_address
  message['from'] = sender_address
  message['subject'] = subject
  # return {'raw': base64.urlsafe_b64encode(message.as_string())}
  b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
  b64_string = b64_bytes.decode()
  return  {'raw': b64_string}



SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.labels'] 


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
            
  

    return service
            
            
            
            

if __name__ == '__main__':
    findthejob() 
    if(len(post_title_texts)>0):
        email_content=create_html()
        service=main()
        message= create_message(sender_address, receiver_address , subject, email_content)
        # sent_message = (service.users().messages().send(userId='me', body=message).execute())
        service.users().messages().send(userId='me',body=message).execute()



    












        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
