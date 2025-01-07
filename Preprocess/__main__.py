from hazm import WordTokenizer, stopwords_list

from Preprocess import stem, normalize


def test_normalize():
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
        این یکی پر ! . علامت # $ % ^ & * ) ( ملامته @
        amirfazel@gmail.com
        می خواهم بروم
    """
    n =  normalize.Normalizer()
    print("hazm: ")
    test_text = n.apply(test_text)
    print(test_text)
    wt = WordTokenizer()
    tokens = wt.tokenize(test_text)
    print(tokens)
    sl = stopwords_list()
    stemmed_tokens = [stem.Stemmer.apply(token) if token not in sl else token for token in tokens]
    print(stemmed_tokens)


if __name__ == "__main__":
    test_normalize()