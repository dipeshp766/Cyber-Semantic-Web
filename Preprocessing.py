# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:30:09 2020

@author: Dipesh Patel
"""

#Other regexp to remove noise and features from tweets.
#(b('))
#(b("))
#(RT @\w*:)
#(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?

import pandas as pd
import re


data = pd.read_csv('EHackerNews_tweets_DUMP.csv')
count = len(data['text'])
flag = 0
clean_tweets = []
url_clean = []

while(flag != count):
    processed = re.sub(r'(\\x\w?\d*)+', '', data['text'][flag])
    processed = re.sub(r"b\'", '', processed)
    processed = re.sub(r'b\"', '', processed)
    processed = re.sub(r'RT @\w*:', '', processed)
    processed = re.sub(r'RT @\w* :', '', processed)
    processed = re.sub(r'\\n', '', processed)
    processed = re.sub(r'&amp\;', 'and', processed)
    processed = re.sub(r'(-)+\&gt\;', '', processed)
    url_list = re.findall(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,?^=%&:/~+-]*[\w])?', processed)
    url_list_1 = [i for sub in url_list for i in sub]
    if url_list_1 == []:
        url_clean.append(url_list_1)
    else:
        url = url_list_1[0]+'://'+url_list_1[1]+url_list_1[2]
        url_clean.append(url)
    processed = re.sub(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,?^=%&:/~+-]*[\w])?', '', processed)
    clean_tweets.append(processed)
    flag += 1

flag = 0
data_store_tuple = []

while (flag != count):
    temp = {}
    temp['date'] = data['created_at'][flag]
    temp['tweet'] = clean_tweets[flag]
    temp['url'] = url_clean[flag]
    data_store_tuple.append(temp)
    flag += 1

datastore = pd.DataFrame(data_store_tuple)

datastore.to_csv('datastore_test.csv')





