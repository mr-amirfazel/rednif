from hazm import Stemmer as HStemmer
from parsivar.stemmer import FindStems


class Stemmer:
    def __init__(self):
        pass

    @staticmethod
    def apply(word):
        stemmer = HStemmer()
        ss = FindStems()
        # return ss.convert_to_stem(word)
        return stemmer.stem(word)
