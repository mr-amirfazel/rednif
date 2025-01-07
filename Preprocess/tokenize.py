from hazm import WordTokenizer


class Tokenizer:
    def __init__(self):
        self.word_tokenizer = WordTokenizer()

    def apply(self, content: str):
        return self.word_tokenizer.tokenize(content)
