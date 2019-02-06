from nltk import pos_tag


class POSTokenizer(object):
    def __init__(self, processor):
        self.lp = processor

    def __call__(self, article):
        # tokenize article
        tokenizer = self.lp.get_tokenizer()

        # lemmatize article
        pos_article = pos_tag(tokenizer(article))

        return [item[1] for item in pos_article]
