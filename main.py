import inflect
from english_words import english_words_set
from itertools import permutations


p = inflect.engine()

question = input('What are the letters?')

keywords = [''.join(i) for i in permutations(question)]
keywords_3 = [''.join(i) for i in permutations(question, 3)]
keywords_4 = [''.join(i) for i in permutations(question, 4)]
keywords_5 = [''.join(i) for i in permutations(question, 5)]

keywords = keywords_3 +keywords_4 +keywords_5+keywords
real_words = []

for x in keywords:
  if x in english_words_set:
    real_words.append(x)
    if len(x) < 5:
      #real_words.append(p.plural(x))
      z = list(x)
      if z[-1]!= 'y':
        real_words.append(x+'s')
print(real_words)