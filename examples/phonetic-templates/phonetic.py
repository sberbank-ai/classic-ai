import json
from random import choice
from nltk.tokenize import word_tokenize
from jellyfish import levenshtein_distance

word_accents_dict = json.loads(open("words_accent.json").read())


def get_vowel_count(word):
    vowels = "уеыаоэёяию"
    vowel_count = 0

    for ch in word:
        if ch in vowels:
            vowel_count += 1

    return vowel_count


def get_accent(word):
    if word in word_accents_dict:
        return word_accents_dict[word]

    vowel_count = get_vowel_count(word)
    return (vowel_count + 1) // 2


def get_phoneme(word):
    word = word.lower()

    word_end = word[-3:]
    vowel_count = get_vowel_count(word)
    accent = get_accent(word)

    return word_end, vowel_count, accent


def text2template(text):
    lines = text.split("\n")

    for i, line in enumerate(lines):
        tokens = word_tokenize(line)
        tokens = [(get_phoneme(token)) for token in tokens if token.isalpha()]

        lines[i] = tokens

    return lines


def find_token(phoneme, corpus):
    word_end, vowel_count, accent = phoneme
    min_dist = 100000
    result_tokens = []

    key = "%s-%s" % (vowel_count, accent)
    if key not in corpus:
        key = choice([i for i in corpus])

    mini_corpus = corpus[key]

    for token, token_phoneme in mini_corpus.items():
        dist = levenshtein_distance(word_end, token_phoneme)

        if dist < min_dist:
            min_dist = dist
            result_tokens = [token]
        elif dist == min_dist:
            result_tokens += [token]

    return choice(result_tokens)
