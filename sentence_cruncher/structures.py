from random import randint

class Word:
    def __init__(self, name):
        self.name = name
        self.count = 1
        self.next_words = {}
        self.is_starter = False

    def is_a_starting_word(self):
        self.is_starter = True

    def put_next_word(self, next_word):
        if (next_word in self.next_words):
            self.next_words[next_word] += 1
        else:
            self.next_words[next_word] = 1

    def find_next_word(self):
        max_count = 0
        for word in self.next_words:
            if (self.next_words[word] > max_count):
                max_count = self.next_words[word]
                ret_string = word
        if (ret_string is None):
            print 'End of sentence because no following words.'
            return '.'
        else:
            return ret_string

    def increment(self):
        self.count += 1

    def printer(self):
        print '\nWord: ' + self.name
        print 'Count: ' + str(self.count)
        print 'Next words: '
        for words in self.next_words:
            print words

class MainMap:
    def __init__(self):
        self.map = {}
        eos = Word('.')
        eos.count = 0
        self.map['ENDOFSENTENCE']  = eos

    def put(self, word1, word2, is_first):
        if not (word1 in self.map):
            self.map[word1] = Word(word1)

        self.map[word1].put_next_word(word2)
        if (is_first):
            self.map[word1].is_a_starting_word()
        if (word2 in self.map):
            self.map[word2].increment()
        else:
            self.map[word2] = Word(word2)

    def process_sentence(self, sentence):
        sentence  = sentence.lower()
        arr = sentence.split(' ')
        if (len(arr) == 1):
            print 'One word sentence.'
            self.put(arr[0], 'ENDOFSENTENCE', True)
            return
        elif (len(arr) == 0):
            print 'Invalid sentence..'
            return
        for i in range(len(arr)):
            if (i == 0):
                self.put(arr[0], arr[1], True)
            elif (i == len(arr) - 1):
                self.put(arr[i], 'ENDOFSENTENCE', False)
            else:
                self.put(arr[i], arr[i+1], False)

    def print_map(self):
        for word in self.map:
            self.map[word].printer()

    def print_starters(self):
        print 'Printing possible starter words.'
        for word in self.map:
            if (self.map[word].is_starter):
                print word

    def generate_first_word(self):
        count = 0
        temp_map = {}
        for word in self.map:
            if (self.map[word].is_starter):
                count += self.map[word].count
                temp_map[count] = word
        random_num = randint(0, count)
        for nums in temp_map:
            if random_num < nums:
                return temp_map[nums]


    def generate_next(self, word):
        word_obj = self.map[word]
        count = 0
        temp_map = {}
        for poss_next in word_obj.next_words:
            count += word_obj.next_words[poss_next]
            temp_map[count] = poss_next
        random_num = randint(0, count)
        for nums in temp_map:
            if random_num < nums:
                return temp_map[nums]
        return temp_map[count]
