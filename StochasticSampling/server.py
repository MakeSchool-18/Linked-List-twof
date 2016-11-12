from flask import Flask, request
from sampling import get_total, rand_word
from histogram import gen_histogram_dict, open_doc
import json

app = Flask(__name__)


@app.route("/word", methods=['GET'])
def get_rand_word():
    histogram = gen_histogram_dict(open_doc("beeMovie.txt"))
    sentence = []
    sentence_len = int(request.args.get('q'))

    for i in range(sentence_len):
        sentence.append(rand_word(histogram, get_total(histogram)))
    return " ".join(sentence)


if __name__ == "__main__":
    app.run()
