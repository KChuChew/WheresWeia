# Bird, Steven, Edward Loper and Ewan Klein (2009).
# Natural Language Processing with Python.  O'Reilly Media Inc.

# Do not use memes for evil! 

import sys
import codecs
import nltk
from nltk.corpus import stopwords

x = ["Hey, you should xD me in the ass.", "You should yolo", "You should 420 me", "You should just fuckityoloxD"]

ignored_words = nltk.corpus.stopwords.words('english')

print(ignored_words)
