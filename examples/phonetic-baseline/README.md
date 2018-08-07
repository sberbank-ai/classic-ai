Генератор стихотворений на основе фонетических шаблонов
=======================================================

Решение основано на простом алгоритме генерации стихотворения:
1. Берем случайное стихотворение поэта из его собрания сочинений
2. Последовательно заменяем слова в стихотворении на те, которые
  - похожи по звучанию (по ударению, число слогов, окончанию)
  - близки заданной теме (по близости word2vec векторов, обученных на русском текстовом корпусе)
3. Объявляем полученный результат замены слов — произведением алгоритма

Решение реализовано на Python 3 с использованием библиотек:
- [`Flask`](http://flask.pocoo.org): веб-сервер
- [`numpy`](http://www.numpy.org), [`scipy`](https://www.scipy.org): работа с векторами и расстояниями
- [`nltk`](https://www.nltk.org): токенизация предложений
- [`gensim`](https://radimrehurek.com/gensim/): работа с word2vec моделью
- [`pymystem3`](https://github.com/nlpub/pymystem3): лемматизация слова

Решению для работы необходимы наборы данных:
- [`data/word_accent.json.bz2`](data/word_accent.json.bz2) — словарь ударений (идет в архиве с решением)
- [`classic_poems.json`](../../data/classic_poems.json) — собрания сочинений поэтов от организаторов
- [`sdsj2017_sberquad.csv`](https://bucketeer-db1966c9-c9f8-427d-ae61-659a91a9fca7.s3.amazonaws.com/public/sdsj2017_sberquad.csv) — набор данных для обучения вопросо-ответной системы из [Sberbank Data Science Journey 2017](https://github.com/sberbank-ai/data-science-journey-2017)
- [`rusvectores/web_upos_cbow_300_20_2017.bin.gz`](http://rusvectores.org/static/models/web_upos_cbow_300_20_2017.bin.gz) — предобученная word2vec модель для русского языка

При локальном тестировании, общедоступные наборы данных должны лежать в каталоге `/data/` (в корне репозитория).

Описание используемой word2vec модели [RusVectores](http://rusvectores.org/ru/about/) можно найти в публикации:

Kutuzov A., Kuzmenko E. (2017) **WebVectors: A Toolkit for Building Web Interfaces for Vector Semantic Models.** In: Ignatov D. et al. (eds) Analysis of Images, Social Networks and Texts. AIST 2016. Communications in Computer and Information Science, vol 661. Springer, Cham



