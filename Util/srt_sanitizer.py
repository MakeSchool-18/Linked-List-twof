import pysrt
import re


def open_doc(source_text):
    try:
        subs = pysrt.open(source_text)
        return subs
    except UnicodeDecodeError:
        subs = pysrt.open(source_text, encoding='iso-8859-1')
        return subs


def sanitize(subs):
    sanitized = ""

    for sub in subs:
        sanitized += sub.text + "\n"

    return sanitized


def concatinate_string_to_file(str, file):
    corpus = open(file, "a")
    corpus.write(str)


def clean_subs(sanitized_subs):



subs = open_doc("Reservoir Dogs.srt")
sanitized_subs = sanitize(subs)
concatinate_string_to_file(sanitized_subs, "corpus.txt")
