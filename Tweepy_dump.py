# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:30:11 2020

@author: Dipesh Patel
"""

import tweepy
import csv
import credentials
import keywords

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    with open('%s_tweets_DUMP.csv' % screen_name, 'a') as a:
        writer = csv.writer(a)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
    pass

if __name__ == '__main__':

    user_list = keywords.cybersecurity_specialists
    for uid in user_list:
        get_all_tweets(uid)