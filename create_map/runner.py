from structures import Word
from structures import MainMap
sentence = ["During the GOP convention, CNN cut away from the victims of illegal immigrant violence"]
sentence.append("They don\'t want them heard")
sentence.append("""When will CNN do a segment on Hillary's plan to increase Syrian refugees 550 and how much it will cost?""")
sentence.append('Hillary Clinton raked in money from regimes that horribly oppress women and gays &amp; refuses to speak out against Radical Islam')
sentence.append('Hillary, whose decisions have led to the deaths of many, accepted $ from a business linked to ISIS')
sentence.append('Silence at CNN')
sentence.append('Crooked Hillary Clinton is 100 owned by her donors #ImWithYou #MAGA')
sentence.append('Thank you Columbus, Ohio!')
sentence.append('I will be back soon #ImWithYou #MAGA')
sentence.append('People believe CNN these days almost as little as they believe Hillary')
sentence.append('''that's really saying something!''')
sentence.append('''The people who support Hillary sit behind CNN anchor chairs, or headline fundraisers, those disconnected from real life''')
sentence.append('''Will CNN send its cameras to the border to show the massive unreported crisis now unfolding, or are they worried it will hurt Hillary?''')
sentence.append('''When will we see stories from CNN on Clinton Foundation corruption and Hillary's pay-for-play at State Department?''')
sentence.append('''CNN anchors are completely out of touch with everyday people worried about rising crime, failing schools and vanishing jobs''')
sentence.append('''CNN will soon be the least trusted name in news if they continue to be the press shop for Hillary Clinton''')
sentence.append('''NEW MENS MILITARY BOOT''')
map = MainMap()
for sent in sentence:
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
