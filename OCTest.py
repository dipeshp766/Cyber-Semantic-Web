# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:25:59 2020

@author: Dipesh Patel
"""

import requests
import credentials
import json
calais_url = credentials.OPEN_CALAIS_URL

def saveFile(content):
    output_file_name = 'analysis_tweet.json'
    output_file = open(output_file_name, 'wb')
    output_file.write(content.encode('utf-8'))
    output_file.close()

def api_call(x):
    headers = {'X-AG-Access-Token': credentials.OPEN_CALAIS, 'Content-Type': 'text/raw', 'outputformat': 'application/json'}
    response = requests.post(calais_url, data=x, headers=headers, timeout=80)
    saveFile(response.text)

def entity_tagger():
    json_file = open('analysis_tweet.json')
    json_str = json_file.read().encode('utf-8')
    json_data = json.loads(json_str)
    keys =  list(json_data.keys())
    keys.pop(0)
    Topics = []
    SocialTags = []
    Score = []
    Importance = []
    final_list = []
    for x in keys:
        if (json_data[x]['_typeGroup'] == 'topics'):
            Topics.append(json_data[x]['name'])
            Score.append(str(json_data[x]['score']))
        elif (json_data[x]['_typeGroup'] == 'socialTag'):
            SocialTags.append(json_data[x]['name'])
            Importance.append(str(json_data[x]['importance']))
        else:
            pass
    final_list.append(Topics)
    final_list.append(Score)
    final_list.append(SocialTags)
    final_list.append(Importance)
    return final_list


