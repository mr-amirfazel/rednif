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

def pre_processing_phase():
    pass

def indexing_phase():
    pass

def query_processing_phase():
    pass

def execute():
    pass

if __name__ == "__main__":

    # count = 0
    # for doc in list(input_data.values()):
    #     count +=1
    # print(count)
    # print(stopwords_list())
    # store = Storage()
    # store.set("docs_size", 2)
    # test_preprop()
    execute()

