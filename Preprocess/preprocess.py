from Preprocess.stem import Stemmer
from Preprocess.tokenize import Tokenizer
from Preprocess.normalize import Normalizer


class Preprocess:
    def __init__(self, contents: list[str]):
        self.__contents = contents
        self.tokenizer = Tokenizer()
        self.normalizer = Normalizer()

    def set_contents(self, contents):
        self.__contents = contents

    def apply(self):
        for content in self.__contents:
            self.__normalize(content)


    def __normalize(self, text):
        return self.normalizer.apply(text)

    def __stem_word(self, word: str):
        return Stemmer.apply(word)

    def __tokenize(self, content: str):
        return self.tokenizer.apply(content)

    def __remove_frequents(self):
        pass
