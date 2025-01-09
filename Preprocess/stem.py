from hazm import Stemmer as HStemmer
from parsivar.stemmer import FindStems


class Stemmer:
    def __init__(self):
        self.__stemmer = HStemmer()

    def apply(self, word):
        return self.__stemmer.stem(word)
