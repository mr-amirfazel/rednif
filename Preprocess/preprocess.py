from hazm import stopwords_list

from Preprocess.stem import Stemmer
from Preprocess.tokenize import Tokenizer
from Preprocess.normalize import Normalizer

from collections import Counter

from utils.logger import log


class Preprocessor:
    def __init__(self, contents: list[str] = []):
        self.__contents = contents
        self.tokenizer = Tokenizer()
        self.normalizer = Normalizer()
        self.__stop_words = [stopwords_list()[i] for i in range(0, len(stopwords_list()) - 1)]
        self.log_condition = False

    def set_contents(self, contents):
        self.__contents = contents

    def apply(self, is_query: bool = False):
        doc_tokens = []
        all_tokens = []
        for index, content in enumerate(self.__contents):
            log(f"===> Preprocessing document #{index+1}", True)
            normalized_content = self.__normalize(content)
            tokens = self.__tokenize(normalized_content)
            pre_stemmed_tokens = self.__stem_tokens(tokens, self.__stop_words)
            doc_tokens.append(pre_stemmed_tokens)
            all_tokens.extend(pre_stemmed_tokens)

        doc_tokens = self.__remove_frequents(all_tokens, doc_tokens, is_query)
        filtered_doc_tokens = [[token for token in tokens if token] for tokens in doc_tokens]
        return filtered_doc_tokens

    def __normalize(self, text):
        log("============ Normalization Begin ============", self.log_condition)
        result = self.normalizer.apply(text)
        log("============ Normalization Result ============", self.log_condition)
        log(result, self.log_condition)
        log("============ Normalization End ============", self.log_condition)
        return result

    def __stem_tokens(self, tokens: list[str], blacklist: list[str] = []):
        log("============ Stemming Begin ============", self.log_condition)
        result = [Stemmer.apply(token) if token not in blacklist else token for token in tokens]
        log("============ Stemming Result ============" , self.log_condition)
        log(result, self.log_condition)
        log("============ Stemming End ============",  self.log_condition)
        return result

    def __tokenize(self, content: str):
        log("============ Tokenization Begin ============", self.log_condition)
        result = self.tokenizer.apply(content)
        log("============ Tokenization Result ============", self.log_condition)
        log(result, self.log_condition)
        log("============ Tokenization End ============", self.log_condition)
        return result

    def __remove_frequents(self, all_tokens: list[str], doc_tokens: list[list[str]], is_query: bool):
        log("============ Removing Frequent Words ... ============", self.log_condition)
        black_list = list(self.__stop_words)
        if not is_query:
            top_n = 50
            top_frequent_words = self.__find_frequent_words(all_tokens, top_n)
            log(f"Top {top_n} Frequent Words: {top_frequent_words}", self.log_condition)
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
        log("============ Removing Frequent Words Begin ============", self.log_condition)
        word_counts = Counter(all_tokens)
        log("============ Removing Frequent Words End ============", False)

        return set([word for word, _ in word_counts.most_common(top_n)])
