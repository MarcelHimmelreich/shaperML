from sklearn.feature_extraction import stop_words
from nltk import word_tokenize


class LanguageProcessor:
    def __init__(self):
        self._tokenizer = word_tokenize
        self._stopwords = stop_words.ENGLISH_STOP_WORDS
        self._locale = None

    def get_tokenizer(self):
        return self._tokenizer

    def get_stopwords(self):
        return self._stopwords

    def get_locale(self):
        return self._locale
