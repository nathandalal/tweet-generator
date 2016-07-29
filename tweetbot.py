from tweet_engine import tweetdb, tweetfetcher
from datetime import date

tweets = tweetfetcher.getTodayTweets()
tweetdb.writetweets(tweets)
print tweetdb.readtweet()

