import random
import sys


class Node:
    word = ""
    # dictionary where the key is the word and the value is [Node, frequency]
    verticies = {}
    total_subsequence_count = 0

    def upsert_vert(self, word, node_dict):
        if word in self.verticies:
            self.verticies[word][1] += 1
            self.total_subsequence_count += 1
        else:
            self.verticies[word] = [node_dict[word], 1]
            self.total_subsequence_count += 1

    def __init__(self, word):
        self.word = word


class Graph:
    # dictionary of word: Node
    nodes = {}

    def insert_word(self, word):
        if word not in self.nodes:
            self.nodes[word] = Node(word)

    def upsert_vert(self, prev_word, subsequent_word):
        self.nodes[prev_word].upsert_vert(subsequent_word, self.nodes)

    def rand_next_node(self, node):
        rand_index = random.randint(0, node.total_subsequence_count)

        traversal_index = 0
        for key, value in node.verticies.items():
            if rand_index in range(traversal_index, value[1]
                                   + traversal_index):
                return node.verticies[key][0]
            else:
                traversal_index += value[1]


def open_doc(source_text):
    doc = open(source_text)
    lines = doc.readlines()
    return lines


def gen_histogram_dict(lines):
    hist_dict = {}

    if isinstance(lines, list):
        for line in lines:
            for word in line.split(' '):
                stripped_word = ''.join([i for i in word if i.isalpha()])
                if stripped_word != '':
                    if stripped_word in hist_dict:
                        hist_dict[stripped_word] += 1
                    else:
                        hist_dict[stripped_word] = 1
    else:
        for word in line.split(' '):
            stripped_word = ''.join([i for i in word if i.isalpha()])
            if stripped_word != '':
                if stripped_word in hist_dict:
                    hist_dict[stripped_word] += 1
                else:
                    hist_dict[stripped_word] = 1

    return hist_dict


def gen_histogram_graph(lines):
    graph = Graph()
    previous_word = ""

    if isinstance(lines, list):
        for line in lines:
            for word in line.split(' '):
                stripped_word = ''.join([i for i in word if i.isalpha()])
                if stripped_word != '':
                    graph.insert_word(stripped_word)
                    if previous_word == "":
                        previous_word = stripped_word
                    else:
                        graph.upsert_vert(previous_word, stripped_word)
                        print(previous_word)
                        previous_word = stripped_word
    return graph


def sentence_from_graph(source_text):
    sentence = []
    graph = gen_histogram_graph(open_doc(source_text))
    current_node = graph.nodes[random.choice(list(graph.nodes.keys()))]

    for i in range(10):
        current_node = graph.rand_next_node(current_node)
        sentence.append(current_node.word)

    print(" ".join(sentence))


def unique_words(hist_dict):
    return len(hist_dict)


def frequency(word, hist_dict):
    if word not in hist_dict:
        return 0
    else:
        return hist_dict[word]

sentence_from_graph(sys.argv[1])
