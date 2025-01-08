import math

def compute_tf_idf(term, doc_id, docs_size):
    return calculate_tf(term, doc_id) * calculate_idf(term, docs_size)


def compute_tf_idf_query(term: str, query_tokens, index, docs_size):
    return calculate_tf_query(term, query_tokens) * calculate_idf(index[term], docs_size)


def calculate_tf_query(term: str, query_tokens: list[str]):
    tf = 0
    for token in query_tokens:
        if token == term:
            tf += 1
    if tf > 0:
        (1 + math.log10(tf))
    else:
        return 0


def calculate_tf(term, doc_id):
    tf = term.get_freq_in_doc(doc_id)
    tf = (1 + math.log10(tf)) if tf > 0 else 0
    return tf


def calculate_idf(term, docs_size):
    if term:
        df = term.get_document_frequency()
        idf = math.log10(docs_size / df)
        return idf
    else:
        return 0
