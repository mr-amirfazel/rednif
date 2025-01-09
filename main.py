import Preprocess.normalize
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
    TOP_K = 10
    p = Preprocessor([test_text, test_text])
    preprocdocs = p.apply()
    index, collection_size = PII(preprocdocs, TOP_K).get_index()
    term: Term = index['فرهاد']
    print(term.get_postings())



if __name__ == "__main__":
    # input_data = utils.file.json_reader("./dataset/IR_data_news_12k.json");
    # for doc in list(input_data.values())[0:10]:
    #     print(doc["content"])
    # count = 0
    # for doc in list(input_data.values()):
    #     count +=1
    # print(count)
    # print(stopwords_list())
    # store = Storage()
    # store.set("docs_size", 2)
    test_preprop()

