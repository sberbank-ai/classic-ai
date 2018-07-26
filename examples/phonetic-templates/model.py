import json
from random import choice
from phonetic import text2template, get_phoneme, find_token


def get_seed_type(seed):
    seed_keywords = json.loads(open("seed_keywords.json").read())

    for seed_type in seed_keywords:
        for keyword in seed_keywords[seed_type]:
            if keyword in seed:
                break
        else:
            continue
        break
    else:
        seed_type = "other"

    return seed_type


def load_poem(author_id):
    poems = json.loads(open("styles.json").read())
    poems = poems[author_id]
    poem = choice(poems)

    return poem


def generate_text(template, corpus):
    text = []
    for temp_line in template:
        row = []
        for t in temp_line:
            row.append(find_token(t, corpus))
        text.append(" ".join(row))

    return "\n".join(text)


def load_corpus(seed_type):
    corpus_text = open("corpus/%s.txt" % seed_type).read()

    tokens = corpus_text.split()
    corpus = dict()

    for token in tokens:
        word_end, vowel_count, accent = get_phoneme(token)

        key = "%s-%s" % (vowel_count, accent)
        w = corpus.get(key, dict())

        w[token] = word_end
        corpus[key] = w

    return corpus


def generate_poem(author_id, seed):
    seed_type = get_seed_type(seed)
    poem = load_poem(author_id)
    template = text2template(poem)
    corpus = load_corpus(seed_type)
    poem = generate_text(template, corpus)

    return poem


if __name__ == "__main__":
    author_id = input("author_id: ")
    seed = input("seed")

    poem = generate_poem(author_id, seed)
    print()
    print(poem)
