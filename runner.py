from structures import Word
from structures import MainMap
from tweet_engine import tweetdb, twitter_handler
from datetime import date

tweets = twitter_handler.get_tweets()
map = MainMap()
for sent in tweets:
    map.process_sentence(sent)
print '--------------'
currWord = map.generate_first_word()
char_count = len(currWord)
while currWord is not 'ENDOFSENTENCE':
    print currWord
    currWord = map.generate_next(currWord)
    char_count += len(currWord)
    if (char_count > 140):
        break
print '.'
