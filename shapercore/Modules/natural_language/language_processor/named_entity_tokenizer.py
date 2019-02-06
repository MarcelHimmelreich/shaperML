from nltk import ne_chunk, pos_tag


class NamedEntityTokenizer(object):
    def __init__(self, processor, detailed=False):
        self.lp = processor
        self._detailed = detailed

    def __call__(self, article):
        # tokenize article
        tokenizer = self.lp.get_tokenizer()

        # lemmatize article
        pos_tagged_tokens = pos_tag(tokenizer(article))

        named_entities = []
        if self._detailed:
            ne_tree = ne_chunk(pos_tagged_tokens, binary=False)
            for sub in ne_tree.subtrees():
                if sub.label() != "S":
                    named_entities.append(sub.label())
        else:
            ne_tree = ne_chunk(pos_tagged_tokens, binary=True)
            for sub in ne_tree.subtrees():
                if sub.label() == "NE":
                    named_entities.append(self.get_simple_name(sub))

        return named_entities

    def get_simple_name(self, subtree):
        return " ".join([item[0] for item in list(subtree)])


