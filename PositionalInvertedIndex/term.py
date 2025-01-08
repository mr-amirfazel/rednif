from typing import Dict, List


class Term:
    def __init__(self, word):
        self.__word = word
        self.__positions_in_doc: Dict[str, List[int]] = {}
        self.__frequency_in_doc: Dict[str, int] = {}
        self.__total_frequency = 0
        self.__champions_list = []

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

    def get_freq_in_doc(self):
        return self.__frequency_in_doc

    def get_total_frequency(self):
        return self.__total_frequency

    def __repr__(self):
        return f"Term(word={self.__word}, champion_list={self.__champions_list})"
