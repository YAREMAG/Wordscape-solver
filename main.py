import time
import inflect
p = inflect.engine()
from english_words import english_words_set
from itertools import permutations

start_time = time.time()

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
    if len(x)< 5:
      real_words.append(p.plural(x))
print(real_words)
end_time = time.time()
total = round(end_time-start_time,2)
print(f"total time {total}")
