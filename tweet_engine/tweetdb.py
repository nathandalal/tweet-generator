from datetime import date
import os

def get_time_file_path(time = date.today()):
    path = 'tweets/%s.txt' % time
    return os.path.join(os.path.dirname(__file__), path)

def writetweets(tweets):
    with open(get_time_file_path(), 'w') as target:
        for tweet in tweets:
            target.write('%s\n' % tweet)
        target.close()

def readtweet(time = date.today()):
    with open(get_time_file_path(time), 'r') as target:
        tweets = target.read().splitlines()
        target.close()
    return tweets