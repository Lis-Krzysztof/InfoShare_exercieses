import os
import collections as cl

data = ""

for filename in os.listdir('zadanie_1_words'):
    data+=(open(os.path.join('zadanie_1_words',filename)).read().lower())

result = cl.Counter(data)

print(result)