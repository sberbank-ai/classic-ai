import os
import copy

from utils import Phonetic, PoemTemplateLoader, Word2vecProcessor

# Каталог с общими наборами данных, доступный на проверяющем сервере
# Нет необходимости добавлять файлы из этого каталога в архив с решением
# (подробности см. в описании соревнования)
DATASETS_PATH = os.environ.get('DATASETS_PATH', '../../data')

# Шаблоны стихов: строим их на основе собраний сочинений от организаторов
template_loader = PoemTemplateLoader(os.path.join(DATASETS_PATH, 'classic_poems.json'))

# Word2vec модель для оценки схожести слов и темы: берем из каталога RusVectores.org
word2vec = Word2vecProcessor(os.path.join(DATASETS_PATH, 'rusvectores/web_upos_cbow_300_20_2017.bin.gz'))

# Словарь ударений: берется из локального файла, который идет вместе с решением
phonetic = Phonetic('data/words_accent.json.bz2')

# Словарь слов-кандидатов по фонетическим формам: строится из набора данных SDSJ 2017
word_by_form = phonetic.form_dictionary_from_csv(os.path.join(DATASETS_PATH, 'sdsj2017_sberquad.csv'))


def generate_poem(seed, poet_id):
    """
    Алгоритм генерации стихотворения на основе фонетических шаблонов
    """

    # выбираем шаблон на основе случайного стихотворения из корпуса
    template = template_loader.get_random_template(poet_id)
    poem = copy.deepcopy(template)

    # оцениваем word2vec-вектор темы
    seed_vec = word2vec.text_vector(seed)

    # заменяем слова в шаблоне на более релевантные теме
    for li, line in enumerate(poem):
        for ti, token in enumerate(line):
            if not token.isalpha():
                continue

            word = token.lower()

            # выбираем слова - кандидаты на замену: максимально похожие фонетически на исходное слово
            form = phonetic.get_form(token)
            candidate_phonetic_distances = [
                (replacement_word, phonetic.sound_distance(replacement_word, word))
                for replacement_word in word_by_form[form]
                ]
            if not candidate_phonetic_distances or form == (0, 0):
                continue
            min_phonetic_distance = min(d for w, d in candidate_phonetic_distances)
            replacement_candidates = [w for w, d in candidate_phonetic_distances if d == min_phonetic_distance]

            # из кандидатов берем максимально близкое теме слово
            word2vec_distances = [
                (replacement_word, word2vec.distance(seed_vec, word2vec.word_vector(replacement_word)))
                for replacement_word in replacement_candidates
                ]
            word2vec_distances.sort(key=lambda pair: pair[1])
            new_word, _ = word2vec_distances[0]

            poem[li][ti] = new_word

    # собираем получившееся стихотворение из слов
    generated_poem = '\n'.join([' '.join([token for token in line]) for line in poem])

    return generated_poem
