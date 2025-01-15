from multiprocessing import Pool, cpu_count
from tqdm import tqdm

import Queryprocess.queryprocess
from utils.file import *

from PositionalInvertedIndex.pii import PII
from PositionalInvertedIndex.term import Term
from Preprocess.preprocess import Preprocessor
from Queryprocess.queryprocess import QueryProcessor
from utils.logger import log

TOP_K = 20
INDEX_PATH = './store/index.pkl.gz'


def preprocess_in_chunks(docs, chunk_size):
    total_docs = len(docs)

    chunks = [docs[i:i + chunk_size] for i in range(0, total_docs, chunk_size)]

    with Pool(processes=cpu_count()) as pool:
        results = list(
            tqdm(
                pool.imap(pre_processing_phase, chunks),
                total=len(chunks),
                desc="Preprocessing Documents"
            )
        )

    preprocessed_results = [doc for chunk in results for doc in chunk]
    return preprocessed_results


def pre_processing_phase(docs):
    p = Preprocessor(docs)
    return p.apply()


def indexing_phase(pre_processed_docs):
    pii = PII(pre_processed_docs, TOP_K)
    return pii.get_index()


def query_processing_phase(data_set, positional_inverted_index, collection_size, queries):
    query_processor = QueryProcessor(data_set, positional_inverted_index, collection_size)
    log("=====> Answering Queries", True)
    for query in queries:
        results = query_processor.apply(query)
        print("\nQuery: ", query)
        query_processor.print_results(results, 4)

def exam_alteration_phase(index, collection_size):
    print(PII.calculate_tfidf_vector_for_document('122', index))
    h, l = PII.find_nth_terms_by_idf(index, 99, collection_size)
    print(h, l)


def execute():
    news_dataset = json_reader("./dataset/IR_data_news_12k.json");
    contents = [doc["content"] for doc in list(news_dataset.values())]
    print(len(contents))
    queries = [
      "ملوان بندر  انزلی",
        "داربی پایتخت"
    ]

    loaded_data = load_index_compressed(INDEX_PATH)
    if not loaded_data:
        preprocessed_dataset = pre_processing_phase(contents)
        index, collection_size = indexing_phase(preprocessed_dataset)
        save_index_compressed(index, collection_size, INDEX_PATH)
    else:
        index, collection_size = loaded_data
    query_processing_phase(news_dataset, index, collection_size, queries)
    # exam_alteration_phase(index, collection_size)

if __name__ == "__main__":
    execute()
