# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:25:57 2020

@author: Dipesh Patel
"""

import requests
import os
import credentials
calais_url = credentials.OPEN_CALAIS_URL

def sendFiles(files, headers, output_dir):
    is_file = os.path.isfile(files)
    if is_file == True:
        sendFile(files, headers, output_dir)
    else:
        for file_name in os.listdir(files):
            if os.path.isfile(file_name):
                sendFile(file_name, headers, output_dir)
            else:
                sendFiles(file_name, headers, output_dir)

def sendFile(file_name, headers, output_dir):
    with open(file_name, 'rb') as input_data:
        response = requests.post(calais_url, data=input_data, headers=headers, timeout=80)
        print ('status code: %s' % response.status_code)
        content = response.text
        print ('Results received: %s' % content)
        if response.status_code == 200:
            saveFile(file_name, output_dir, content)

def saveFile(file_name, output_dir, content):
    output_file_name = os.path.basename(file_name) + '.json'
    output_file = open(os.path.join(output_dir, output_file_name), 'wb')
    output_file.write(content.encode('utf-8'))
    output_file.close()

def api_call():
    #input_file = 'tweet.txt'
    output_dir = 'results'
    access_token = credentials.OPEN_CALAIS
    #if not os.path.exists(input_file):
        #print('The file [%s] does not exist' % input_file)
        #return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    headers = {'X-AG-Access-Token': access_token, 'Content-Type': 'text/raw', 'outputformat': 'application/json'}
    sendFiles('ASUS wireless routers are vulnerable to MITM attacks', headers, output_dir)

api_call()