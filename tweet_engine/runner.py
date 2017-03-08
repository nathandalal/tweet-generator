from structures import Word, MainMap
import twitter_handler
import time

def capitalize_first_word(self):
    self[0] = self[0].title()

def turn_arr_to_sentence(self):
    return ' '.join(self)

def process_all_tweets(map, tweets):
    for sent in tweets:
        map.process_sentence(sent)

def do_it():
    print 'Entering do_it().'
    tweets = twitter_handler.get_tweets()
    print 'Got tweets.'
    map = MainMap()
    process_all_tweets(map, tweets)
    print 'Processed all tweets.'
    first_word = map.generate_first_word()
    currWord = map.generate_next(first_word)
    char_count = len(currWord)
    new_sentence = []
    while currWord is not 'ENDOFSENTENCE':
        if not ('http' in currWord):
            new_sentence.append(currWord)
            currWord = map.generate_next(currWord)
            char_count += len(currWord)
            if '.' in currWord:
                break
    print 'Created sentence.'
    capitalize_first_word(new_sentence)
    final_sentence = turn_arr_to_sentence(new_sentence)
    twitter_handler.publish_tweet(final_sentence)
    print 'Tweet published.'    
    return final_sentence


def run():
    errorCount = 0
    while errorCount < 10:
        try:
            f = open('workfile', 'w')
            print 'Opened file!'
            currSent = do_it()
            f.write(currSent)
            print 'Wrote to file!'
            f.close()
            print 'Closed file!'
            print '5 more minutes till tweet.'
            time.sleep(60)
            print '4 more minutes till tweet.'
            time.sleep(60)
            print '3 more minutes till tweet.'
            time.sleep(60)
            print '2 more minutes till tweet.'
            time.sleep(60)
            print '1 more minutes till tweet.'
            time.sleep(60)
            print 'now!'
        except:
            print 'An error has occurred.'
            errorCount += 1
            time.sleep(300)

if __name__ == "__main__":
    run()