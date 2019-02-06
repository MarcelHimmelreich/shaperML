from shapercore.Modules.metaclass.Module_Natural_Language import Data
from shapercore.Modules.natural_language.language_processor.processor import LanguageProcessor
from shapercore.Modules.natural_language.language_processor.lemma_tokenizer import LemmaTokenizer
from shapercore.Modules.natural_language.language_processor.named_entity_tokenizer import NamedEntityTokenizer
from shapercore.Modules.natural_language.language_processor.pos_tokenizer import POSTokenizer
from shapercore.Modules.natural_language.language_processor.word_list_entry_tokenizer import WordlistEntryTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer



class NaturalLanguageProcessor(Data):
    def __init__(self, column=None, extraction_target="word", extraction_type="bow", measure=None, ngram=None):
        self._column = column
        self._extraction_target = extraction_target
        self._extraction_type = extraction_type
        self._ngram = ngram
        self._measure = measure
        self._max_features = 100
        "Measure: tfidf, presence, count"

    def visit(self, featureset):
        try:
            # TODO: outsource into method "set_tokenizer" (tokenizer as member - no extraction_target required then)
            tokenizer = None
            if self._extraction_target == "word":
                tokenizer = LemmaTokenizer(LanguageProcessor())
            elif self._extraction_target == "pos":
                tokenizer = POSTokenizer(LanguageProcessor())
            elif self._extraction_target == "ne_simple":
                tokenizer = NamedEntityTokenizer(LanguageProcessor())
            elif self._extraction_target == "ne_detailed":
                tokenizer = NamedEntityTokenizer(LanguageProcessor(), detailed=True)
            elif self._extraction_target.startswith("wordlist"):
                path = self._extraction_target.split("_")[1]
                tokenizer = WordlistEntryTokenizer(LanguageProcessor(), wordlist=path)

            # TODO: outsource into method "set_vectorizer" (vectorizer as member - no measure required then)
            print(self._ngram)
            print(self._column)
            vectorizer = None
            binary = self._measure == "presence" or self._extraction_type == "presence"
            if self._ngram is None:
                if self._measure == "tfidf":
                    vectorizer = TfidfVectorizer(tokenizer=tokenizer)
                else:
                    # TODO: here it is absolute term-frequency - what about relative?
                    #   For ngrams not easy:
                    #   - needs to count the amount of n-gram for each document and divide each feature generated from
                    #     the ngram-counts of the document by that amount
                    #   For named-entities:
                    #   - count words inside named entities (not just the amount of NEs) devide by num tokens of doc
                    #   ...

                    vectorizer = CountVectorizer(tokenizer=tokenizer, binary=binary)
            else:
                if self._measure == "tfidf":
                    vectorizer = TfidfVectorizer(tokenizer=tokenizer, ngram_range=self._ngram)
                else:
                    vectorizer = CountVectorizer(tokenizer=tokenizer, ngram_range=self._ngram, binary=binary)
            temp_column = featureset.get_featureset()[self._column]
            temp_column = temp_column.values

            new_column = []
            "Note: Presence and Count for every(einzeln) feature or for all(alle) feature"
            if self._extraction_type == "bow" or self._extraction_type == "ngram":
                # Return Matrix
                new_column = list(vectorizer.fit_transform(temp_column).toarray())
            elif self._extraction_type == "list":
                # Return String Array
                analyzer = vectorizer.build_tokenizer()
                for row in temp_column:
                    print(row)
                    print(analyzer(row))
                    new_column.append(analyzer(row))
            elif self._extraction_type == "presence":
                # Return Numeric Array
                analyzer = vectorizer.build_tokenizer()
                for row in temp_column:
                    new_column.append(1 if len(analyzer(row)) > 0 else 0)
                    # new_column.append(len(analyzer(row)) > 0)
            elif self._extraction_type == "count":
                # Return Numeric Array
                analyzer = vectorizer.build_tokenizer()
                for row in temp_column:
                    new_column.append(len(analyzer(row)))
            return new_column
        except Exception as error:
            util.print_error("Failed to use Language Processor " + str(error))
            util.print_detailed_error()

