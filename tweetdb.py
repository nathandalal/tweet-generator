from datetime import date

def writetweets(tweets):
    filename = '%s.txt' % date.today()
    path = 'tweets/%s' % (filename)
    target = open(path, 'w')

    for tweet in tweets:
        target.write('%s\n' % tweet)
    target.close()

def readtweet(time = date.today()):
    filename = '%s.txt' % time
    path = 'tweets/%s' % (filename)
    target = open(path, 'r')

    tweets = target.read().splitlines()
    target.close()
    return tweets
