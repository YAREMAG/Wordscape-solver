import requests
import nltk
import time
from english_words import english_words_set
from itertools import permutations, combinations
key = '17382436-3621-47df-aba5-5c12e228f123'
start_time = time.time()
# thesaurus key 79cac01e-87b1-418a-ab22-1152876f140a

#url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/energetic?key='+key

#url_loops = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + '''word''' + '''?key=''' + key


#p = requests.get(url).json()
#print(p)
#print(p[0]['def'][0]['sseq'][0][0][1]['dt'])  #THIS IS NEEDED TO GET TO THE WORD DEFINITION

#ABOVE DOES NOT WORK IF THERE IS MORE THAN ONE VARIATION OF THE WORD
#methodology for creating all possible words

question =input('What are the letters?')

keywords = [''.join(i) for i in permutations(question)]
keywords_3 = [''.join(i) for i in permutations(question, 3)]
keywords_4 = [''.join(i) for i in permutations(question, 4)]
keywords_5 = [''.join(i) for i in permutations(question, 5)]

keywords = keywords_3 +keywords_4 +keywords_5+keywords

real_words = []

for x in keywords:
  if x in english_words_set:
    real_words.append(x)
print(real_words)
end_time = time.time()
total = round(end_time-start_time,2)
print(f"total time {total}")
