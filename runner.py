from structures import Word
from structures import MainMap
from tweet_engine import tweetdb, twitter_handler
from datetime import date

def capitalize_first_word(self):
    self[0] = self[0].title()

def turn_arr_to_sentence(self):
    return ' '.join(self) + '.'

def process_all_tweets(map, tweets):
    for sent in tweets:
        map.process_sentence(sent)


tweets = twitter_handler.get_tweets()
map = MainMap()
process_all_tweets(map, tweets)
first_word = map.generate_first_word()
currWord = map.generate_next(first_word)
char_count = len(currWord)
new_sentence = []
while currWord is not 'ENDOFSENTENCE':
#    print currWord
    if not ('http' in currWord):
        new_sentence.append(currWord)
        currWord = map.generate_next(currWord)
        char_count += len(currWord)
        if '.' in currWord:
            break

capitalize_first_word(new_sentence)
final_sentence = turn_arr_to_sentence(new_sentence)
print final_sentence
