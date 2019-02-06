from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag


class LemmaTokenizer(object):
    def __init__(self, processor):
        self.lp = processor
        self.wnl = WordNetLemmatizer()

    def __call__(self, article):
        # tokenize article
        tokenizer = self.lp.get_tokenizer()

        # lemmatize article
        pos_article = pos_tag(tokenizer(article))
        lem_article = [self.wnl.lemmatize(pair[0], self.get_wordnet_pos(pair[1])) for pair in pos_article]

        # lemmatize stopwords
        pos_stopwords = pos_tag(self.lp.get_stopwords())
        lem_stopwords = [self.wnl.lemmatize(pair[0], self.get_wordnet_pos(pair[1])) for pair in pos_stopwords]

        return [item for item in lem_article if item not in lem_stopwords]

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
