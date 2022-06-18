# -*- coding: utf-8 -*-
import nltk
nltk.download('vader_lexicon')

from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Authentication

# twitter developer site is here ↓
# https://developer.twitter.com/en
# please register and get your api key before you analysis twitter.

consumerKey = 'conumerkey'
consumerSecret = 'conumerseacretkey'
accessToken = 'accessToken'
accessTokenSecret = 'accessTokenSeacret'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sentiment Analysis

def percentage(part, whole):
    return 100*float(part)/float(whole)

keyword = input("Please enter keyword or hashtag to search: ")
get_tweet = int(input ("Please enter how many tweets to analyze: "))  

tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(get_tweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for t in tweets:
    # print(t.text)
    tweet_list.append(t.text)
    analysis = TextBlob(t.text)
    score = SentimentIntensityAnalyzer().polarity_scores(t.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    com = score['compound']
    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(t.text)
        neg += 1

    elif pos > neg:
        positive_list.append(t.text)
        pos += 1

    elif pos == neg:
        neutral_list.append(t.text)
        neu += 1
pos = percentage(pos, get_tweet)
neg = percentage(neg, get_tweet)
neu = percentage(neu, get_tweet)
pol = percentage(polarity, get_tweet)
positive = format(pos, '.1f')
negative = format(neg, '.1f')
neutral = format(neu, '.1f')

#Number of Tweets (Total, Positive, Negative, Neutral)
tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total: ",len(tweet_list))
print("positive: ",len(positive_list))
print("negative: ", len(negative_list))
print("neutral: ",len(neutral_list))

tweet_list

tweet_list.drop_duplicates(inplace = True)

tw_list = pd.DataFrame(tweet_list)
tw_list["text"] = tw_list[0]
tw_list
