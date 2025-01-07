from hazm import stopwords_list

from Preprocess.stem import Stemmer
from Preprocess.tokenize import Tokenizer
from Preprocess.normalize import Normalizer

from collections import Counter

class Preprocessor:
    def __init__(self, contents: list[str]):
        self.__contents = contents
        self.tokenizer = Tokenizer()
        self.normalizer = Normalizer()
        self.__stop_words = [stopwords_list()[i] for i in range(0, len(stopwords_list()) - 1)]

    def set_contents(self, contents):
        self.__contents = contents

    def apply(self):
        doc_tokens = []
        all_tokens = []
        for content in self.__contents:
            normalized_content = self.__normalize(content)
            tokens = self.__tokenize(normalized_content)
            pre_stemmed_tokens = self.__stem_tokens(tokens, self.__stop_words)
            doc_tokens.append(pre_stemmed_tokens)
            all_tokens.extend(pre_stemmed_tokens)

        doc_tokens = self.__remove_frequents(all_tokens, doc_tokens)
        print(doc_tokens)



    def __normalize(self, text):
        print("============ Normalization Begin ============")
        result = self.normalizer.apply(text)
        print("============ Normalization Result ============")
        print(result)
        print("============ Normalization End ============", end="\n\n")
        return result

    def __stem_tokens(self, tokens: list[str], blacklist: list[str] = []):
        print("============ Stemming Begin ============")
        result = [Stemmer.apply(token) if token not in blacklist else token for token in tokens]
        print("============ Stemming Result ============")
        print(result)
        print("============ Stemming End ============", end="\n\n")
        return result

    def __tokenize(self, content: str):
        print("============ Tokenization Begin ============")
        result = self.tokenizer.apply(content)
        print("============ Tokenization Result ============")
        print(result)
        print("============ Tokenization End ============", end="\n\n")
        return result

    def __remove_frequents(self, all_tokens: list[str], doc_tokens: list[list[str]]):
        print("============ Removing Frequent Words ... ============")
        top_n = 14
        top_frequent_words = self.__find_frequent_words(all_tokens, top_n)
        print(f"Top {top_n} Frequent Words: {top_frequent_words}")
        black_list = list(self.__stop_words)
        black_list.extend(list(top_frequent_words))
        cleansed_doc_tokens = []
        for tokens in doc_tokens:
            new_tokens = []
            for token in tokens:
                if token not in black_list:
                    new_tokens.append(token)
            cleansed_doc_tokens.append(new_tokens)
        return cleansed_doc_tokens



    def __find_frequent_words(self, all_tokens: list[str], top_n=50):
        print("============ Removing Frequent Words Begin ============")
        word_counts = Counter(all_tokens)

        return set([word for word, _ in word_counts.most_common(top_n)])

