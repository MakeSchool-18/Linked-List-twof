from flask import Flask, request
from sampling import get_total, rand_word
from histogram import gen_histogram_dict, open_doc
import json

app = Flask(__name__)


@app.route("/word", methods=['GET'])
def get_rand_word():
    histogram = gen_histogram_dict(open_doc("beeMovie.txt"))
    sentence = []
    for i in range(10):
        sentence.append(rand_word(histogram, get_total(histogram)))
    return " ".join(sentence)


if __name__ == "__main__":
    app.run()
