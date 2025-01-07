from hazm import Stemmer as HStemmer


class Stemmer:
    def __init__(self):
        pass

    @staticmethod
    def apply(word):
        stemmer = HStemmer()
        return stemmer.stem(word)
