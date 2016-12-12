# -*- coding: utf-8 -*-
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


def tokenize_and_clean_subs(sanitized_subs):
    p = "(?:'([\wÀ-ÿ]+[\'\-]?[\wÀ-ÿ]*)'|((?:[\wÀ-ÿ]+[\'\-]?[\wÀ-ÿ]*[\'\-]?"\
        ")+)|((?:'?[\wÀ-ÿ]+[\'\-]?[\wÀ-ÿ]*)+))"
    pattern = re.compile(p)
    return pattern.findall(sanitized_subs)


subs = open_doc("Reservoir Dogs.srt")
sanitized_subs = sanitize(subs)
print(clean_subs(sanitized_subs))
