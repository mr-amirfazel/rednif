from typing import Dict, List

from utils.store import Storage
from utils.tfidf import compute_tf_idf


class Term:
    def __init__(self, word):
        self.__word = word
        self.__positions_in_doc: Dict[str, List[int]] = {}
        self.__frequency_in_doc: Dict[str, int] = {}
        self.__total_frequency = 0
        self.__champions_list = []
        self.__weight_per_doc: Dict[str, float] = {}
        self.__storage = Storage()

    def add_posting(self, doc_id, position):
        if doc_id not in self.__positions_in_doc:
            self.__positions_in_doc[doc_id] = []
            self.__frequency_in_doc[doc_id] = 0
        self.__positions_in_doc[doc_id].append(position)
        self.__frequency_in_doc[doc_id] += 1
        self.__total_frequency += 1

    def get_champs(self):
        return self.__champions_list

    def get_docs(self):
        return self.__positions_in_doc.keys()

    def get_document_frequency(self):
        return len(self.__positions_in_doc.keys())

    def get_postings(self):
        return self.__positions_in_doc

    def get_word(self):
        return self.__word

    def get_freq_in_doc(self, doc_id):
        if doc_id in self.__frequency_in_doc:
            return self.__frequency_in_doc[doc_id]
        else:
            return 0

    def get_total_frequency(self):
        return self.__total_frequency

    def create_champions_list(self, top_k: int):
        self.__champions_list = [doc_id for doc_id, _ in sorted(
            self.__weight_per_doc.items(),
            key=lambda item: item[1],
            reverse=True
        )[:top_k]]

    def compute_weight_per_doc(self, doc_id, docs_size):
        self.__weight_per_doc[doc_id] = compute_tf_idf(self, doc_id, docs_size)

    def get_weight_per_doc(self, doc_id):
        return self.__weight_per_doc[doc_id]

    def __repr__(self):
        return f"Term(word={self.__word}, champion_list={self.__champions_list})"
