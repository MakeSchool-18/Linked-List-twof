from histogram import gen_histogram_dict, open_doc
from functools import reduce
import random
import sys


def get_total(histogram):
    return reduce(lambda x, y: x + y, histogram.values())


def rand_word(histogram, total):
    rand_index = random.randint(0, total)

    # binary search
    # found = False
    # traversal_index = len(histogram)
    # while not found:
    #     if rand_index in histogram.items()[traversal_index]

    traversal_index = 0
    for key, value in histogram.items():
        if rand_index in range(traversal_index, value + traversal_index):
            return key
        else:
            traversal_index += value
