from utils.logger import log

from PositionalInvertedIndex.term import Term
from utils.tfidf import calculate_idf


class PII:
    def __init__(self, pre_processed_docs, top_k):
        self.__positional_inverted_index = {}
        self.__docs_size = len(pre_processed_docs)
        self.__top_k = top_k
        self.__construct_pii(pre_processed_docs)

    def __construct_pii(self, pre_processed_docs):
        log("=== Creating Positional Inverted Index Started... ===", True)
        self.__index_terms(pre_processed_docs)
        self.__calculate_weights()
        self.__create_champions()
        log("=== Creating Positional Inverted Index Ended... ===", True)

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
        for term in self.__positional_inverted_index.values():
            for doc_id in term.get_docs():
                term.compute_weight_per_doc(doc_id, self.__docs_size)

    def __create_champions(self):
        for term in self.__positional_inverted_index.values():
            term.create_champions_list(self.__top_k)

    def get_index(self):
        return self.__positional_inverted_index, self.__docs_size

    @staticmethod
    def calculate_tfidf_vector_for_document(doc_id, index):
        tfidf_vector = {}
        for term, term_obj in index.items():
            if int(doc_id) in list(term_obj.get_docs()):
                tfidf_vector[term] = term_obj.get_weight_per_doc()[int(doc_id)]
        return tfidf_vector

    @staticmethod
    def find_nth_terms_by_idf(index, n, collection_size):
        idf_scores = {}
        for term, term_obj in index.items():
            idf_scores[term] = calculate_idf(term_obj, collection_size)

        sorted_by_idf_desc = sorted(idf_scores.items(), key=lambda x: x[1], reverse=True)

        sorted_by_idf_asc = sorted((item for item in idf_scores.items() if item[1] > 0), key=lambda x: x[1])

        nth_highest = sorted_by_idf_desc[n - 1] if n <= len(sorted_by_idf_desc) else None
        nth_lowest = sorted_by_idf_asc[n - 1] if n <= len(sorted_by_idf_asc) else None

        return nth_highest, nth_lowest

