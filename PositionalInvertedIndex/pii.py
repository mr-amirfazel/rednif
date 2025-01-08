from PositionalInvertedIndex.term import Term
from utils.store import Storage

TOP_K = 10

class PII:
    def __init__(self, pre_processed_docs):
        self.__positional_inverted_index = {}
        self.storage = Storage()
        self.__construct_pii(pre_processed_docs)


    def __construct_pii(self, pre_processed_docs):
        self.__index_terms(pre_processed_docs)
        self.__calculate_weights()
        self.__create_champions()

    def __index_terms(self, pre_processed_docs):
        for doc_id, doc in enumerate(pre_processed_docs):
            for pos, token in enumerate(doc):
                if token in self.__positional_inverted_index:
                    term = self.__positional_inverted_index[token]
                else:
                    term = Term(token)
                term.add_posting(doc_id, pos)
                self.__positional_inverted_index[token] = term

    def __calculate_weights(self):
        docs_size = self.storage.get("docs_size")
        for term in self.__positional_inverted_index.values():
            for doc_id in term.get_docs():
                term.compute_weight_per_doc(doc_id, docs_size)

    def __create_champions(self):
        for term in self.__positional_inverted_index.values():
            term.create_champions_list(TOP_K)

    def get_index(self):
        return self.__positional_inverted_index
