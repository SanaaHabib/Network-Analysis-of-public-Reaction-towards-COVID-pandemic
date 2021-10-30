
import tweepy
import csv
import pandas
import datetime

import pandas as pd
consumer_key="upNRRvI9sGFKdm8O69iXNS5xx"
consumer_secret="NxCBMWyLAw7IlanDk7CZXDKYMZW3yaBfBhrBycgISmP1XxDl4K"
access_key="2301506694-nh8NNKSzteUBofgaRucugCEwcp8jfFEFl8jmOsJ"
access_secret="Sk9OPb7L3CCVFMDoK8hsW0ZgENajgfQraaTlhX7E097nF"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_key,access_secret)

api =tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('Corona.csv','w',encoding='utf-8-sig')
csvWriter = csv.DictWriter(csvFile, fieldnames = ["users", "comments","location","Date"])
csvWriter.writeheader()
csvWriter=csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Corona",lang='en',result_type="recent").items():
    csvWriter.writerow([tweet.user.name,tweet.text,tweet.user.location,tweet.created_at])
