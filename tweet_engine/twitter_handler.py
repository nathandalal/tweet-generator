import tweepy
from datetime import date
from config import *
import urllib

def __setup_api():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth)
__api = __setup_api()


def __format_tweet(search_result):
	text = search_result.text
	return text

#
#	returns top retweeted tweets
#
#	params:
#		limit -> number of tweets (changed to multiple of 50)
# 		duration -> over how many days
#
#
#
def get_tweets(limit = 1500, duration = 1, formatted = True):
	tweets = __api.home_timeline(result_type="popular", count=limit)
	if formatted:
		tweets = map(__format_tweet, tweets)
	return tweets

def publish_tweet(tweet):
	print tweet
	__api.update_status(tweet)
