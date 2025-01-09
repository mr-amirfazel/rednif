import math
from typing import Dict

import Preprocess.preprocess
from PositionalInvertedIndex.term import Term
from utils.tfidf import compute_tf_idf_query


class QueryProcessor:
    def __init__(self, positional_inverted_index, collection_size):
        self.__index: Dict[str, Term] = positional_inverted_index
        self.__collection_size = collection_size
        self.__pre_processor = Preprocess.preprocess.Preprocessor()
        self.__scores = {}

    def apply(self, query):
        normal_denoms = self.calculate_docs_normalization_denominator()
        self.__scores = self.__compute_cosine_similarity(query, normal_denoms)

    def __compute_cosine_similarity(self, query, denoms):
        raw_scores: dict = {}
        self.__pre_processor.set_contents([query])
        tokenized_query = self.__pre_processor.apply(True)
        tokenized_query = tokenized_query[0]

        for term in tokenized_query:
            if term not in self.__index:
                continue
            query_token_weight = compute_tf_idf_query(term, tokenized_query, self.__index, self.__collection_size)
            for doc_id in self.__index[term].get_champs():
                doc_token_weight = self.__index[term].get_weight_per_doc()[doc_id]
                if doc_id not in raw_scores:
                    raw_scores[doc_id] = 0
                raw_scores[doc_id] = doc_token_weight * query_token_weight
            scores = {doc_id: raw_scores[doc_id] / denoms[doc_id] for doc_id in raw_scores}
            return scores

    def __calculate_docs_normalization_denominator(self):
        denoms = [0 for _ in range(self.__collection_size)]
        for term in self.__index:
            for doc_id in term.get_docs():
                denoms[doc_id] = math.sqrt(sum(weight ** 2 for weight in term.get_weight_per_doc().values()))
        return denoms

    def print_results(self, dataset, top_n: int):
        scores = dict(sorted(self.__socres.items(), key=lambda item: item[1], reverse=True)[:top_n])
        for index, doc_id in enumerate(scores):
            title = dataset[doc_id]["title"]
            link = dataset[doc_id]["url"]
            print(f"====== Result ({index+1}) ======")
            print(f"\t\t title:  \"{title}\" ")
            print(f"\t\t link {link}")
