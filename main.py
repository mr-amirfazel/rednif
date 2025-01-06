import Preprocess.normalize
import utils.file
from hazm import stopwords_list

def test_normalize(text):
    test_text = """
        این یک پیام می باشد. این پیامها زشتند. 123 سالِ پیشّ هوا سرد نمیتونم برم بَیرون. ! ای بابا # چرا ، نمیشه کاری کَرد
    """
    print("parsivar: ")
    print(Preprocess.normalize.parsivar_normalizer(text))
    print("hazm: ")
    print(Preprocess.normalize.hazm_normalizer(text))


if __name__ == "__main__":
    input_data = utils.file.json_reader("./dataset/IR_data_news_12k.json");
    print(list(input_data))
    count = 0
    for doc in list(input_data.values()):
        count +=1
    print(count)
    print(stopwords_list())