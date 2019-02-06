

class WordlistEntryTokenizer(object):
    def __init__(self, processor, wordlist):
        self.lp = processor
        self._wordlist = list()
        self._simple_words = True

        self.load_wordlist(wordlist)

    def load_wordlist(self, wordlist):
        with open(wordlist) as file:
            for line in file:
                term = line.rstrip('\n')
                self._wordlist.append(term)

                if " " in term.strip():
                    self._simple_words = False

    def tokenize_wordlist(self, wordlist):
        article = " ".join(self._wordlist)
        tokenize = self.lp.get_tokenizer()
        self._wordlist = tokenize(article)

    def __call__(self, article):
        if self._simple_words:
            tokenize = self.lp.get_tokenizer()
            article = " ".join(tokenize(article))

        # TODO: this does not retain the order of words in the article which leads to erroneous n-grams
        tokenlist = list()
        for item in self._wordlist:
            for _ in range(article.count(item)):
                tokenlist.append(item)

        if len(tokenlist) is not 0:
            util.print_warning(tokenlist)

        return tokenlist
