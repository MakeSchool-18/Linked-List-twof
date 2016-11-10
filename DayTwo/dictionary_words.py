import random

fp = open("/usr/share/dict/words")
lines = fp.readlines()

sentence = []

for i in range(5):
    rand_index = random.randint(0, 235886 - 1)
    sentence.append(lines[rand_index].rstrip())

print(" ".join(sentence))
