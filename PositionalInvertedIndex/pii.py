from PositionalInvertedIndex.term import Term


class PII:
    def __init__(self, pre_processed_docs):
        self.__positional_inverted_index = {}
        self.__construct_pii(pre_processed_docs)

    def __construct_pii(self, pre_processed_docs):
        for doc_id, doc in enumerate(pre_processed_docs):
            for pos, token in enumerate(doc):
                if token in self.__positional_inverted_index:
                    term = self.__positional_inverted_index[token]
                else:
                    term = Term(token)
                term.add_posting(doc_id, pos)
                self.__positional_inverted_index[token] = term

    def get_index(self):
        return self.__positional_inverted_index