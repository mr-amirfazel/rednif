from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count

from tqdm import tqdm

import Preprocess.normalize
import Queryprocess.queryprocess
import utils.file
from hazm import stopwords_list, WordTokenizer

from PositionalInvertedIndex.pii import PII
from PositionalInvertedIndex.term import Term
from Preprocess.preprocess import Preprocessor


def test_preprop():
    test_text = """
      کتابها
      کتابهایی
      کتابی
      کتابهای
      بزرگتر
      بزرگترین
      کتاب        اش
      کتاب    ات
      خسته    ام
      بسته     ای
      میخواهم
      نمیتوانم
      کوزه گر
      شیشه    گری
      کتابهایی که میخوانم گر زیبا باشد اما کتابهایم هنوز نیستند.
        شما هم کتابهایتان را بردارید و ببرید
        این یکی پر ! . علامت # $ % ^ & * ) ( ملامت @
        amirfazel@gmail.com
        می خواهم بروم
        فروشنده
        کلیله
        دمنه
        فرانسه
        قسطنتنیه
        اسنیکرز
        فرهاد
        سجاد
        هاشم
        گیتی پسند اصفهان
        در جام جهانی فوتبال
    """
    TOP_K = 20
    news_dataset = utils.file.json_reader("./dataset/IR_data_news_12k.json");
    print(list(list(news_dataset.values())[0].values())[0])
    print(list(list(news_dataset.values())[0].values())[4])
    contents = [doc["content"] for doc in list(news_dataset.values())[:500]]
    ds = contents[:160]
    p = Preprocessor(ds)
    preprocdocs = p.apply()
    index, collection_size = PII(preprocdocs, TOP_K).get_index()
    qp = Queryprocess.queryprocess.QueryProcessor(news_dataset, index, collection_size)
    scores = qp.apply("تیم ملی")
    qp.print_results(scores, 10)

def preprocess_in_chunks(docs, chunk_size):
    """
    Preprocess documents in chunks using multiprocessing.
    :param docs: List of documents to preprocess.
    :param chunk_size: Number of documents to process per chunk.
    :return: List of preprocessed documents.
    """
    total_docs = len(docs)

    # Split the dataset into chunks
    chunks = [docs[i:i + chunk_size] for i in range(0, total_docs, chunk_size)]

    with Pool(processes=cpu_count()) as pool:
        # Process each chunk in parallel
        results = list(
            tqdm(
                pool.imap(pre_processing_phase, chunks),
                total=len(chunks),
                desc="Preprocessing Documents"
            )
        )

    # Flatten the results
    preprocessed_results = [doc for chunk in results for doc in chunk]
    return preprocessed_results

def pre_processing_phase(docs):
    p = Preprocessor(docs)
    return p.apply()

def indexing_phase():
    pass

def query_processing_phase():
    pass

def execute():
    news_dataset = utils.file.json_reader("./dataset/IR_data_news_12k.json");
    contents = [doc["content"] for doc in list(news_dataset.values())]
    chunk_size = 435
    preprocessed_dataset = preprocess_in_chunks(contents, chunk_size)
    print(len(preprocessed_dataset))


if __name__ == "__main__":
    execute()

