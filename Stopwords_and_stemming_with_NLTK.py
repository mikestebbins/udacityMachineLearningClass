# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:42:47 2016

@author: mstebbins
"""

# BAG OF WORDS STUFF
from nltk.corpus import stopwords
sw = stopwords.words("english")
print sw[0]
print sw[10]
print len(sw)

from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("english")

print stemmer.stem("responsiveness")
print stemmer.stem("resonsivity")
print stemmer.stem("unresponsive")