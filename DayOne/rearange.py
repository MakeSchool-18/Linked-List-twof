import random
import sys

word_list = []


def randomize_words():
    entry_list = sys.argv[1:]

    for entry in entry_list:
        rand_index = random.randint(0, len(entry_list) - 1)
        word_list.append(entry_list[rand_index])
    return ' '.join(word_list)


if __name__ == '__main__':
    print(randomize_words())
