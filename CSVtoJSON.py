# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:25:56 2020

@author: Dipesh Patel
"""

import pandas as pd
import OC_test
import json


data = pd.read_csv('datastore_test.csv')
length = len(data['tweet'])
dict = {}
nested = {}

for x in range(0,100):
    OC_test.api_call(str(data['tweet'][x]))
    nested['tweet'] = data['tweet'][x]
    nested['date'] = data['date'][x]
    nested['URL'] = data['url'][x]
    try:
        entity_tag = OC_test.entity_tagger()
        nested['Topics'] = entity_tag[0]
        nested['Score'] = entity_tag[1]
        nested['Social Tags'] = entity_tag[2]
        nested['Importance'] = entity_tag[3]
    except:
        print("Exception Occured for JSON decoding OR API CALL LIMIT passed")
    dict[data['tweet id'][x]] = nested
    nested = {}
print(dict)
with open('NLP_processed_datastore.json','w') as fp:
    json.dump(dict, fp)


