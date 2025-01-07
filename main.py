import Preprocess.normalize
import utils.file
from hazm import stopwords_list, WordTokenizer

def test_normalize():
    test_text = """
        این یک پیام می باشد. این پیامها زشتند. 123 سالِ پیشّ هوا سرد نمیتونم برم بَیرون. ! ای بابا # چرا ، نمیشه کاری کَرد
    """
    test_text = Preprocess.normalize.hazm_normalizer(test_text)



if __name__ == "__main__":
    # input_data = utils.file.json_reader("./dataset/IR_data_news_12k.json");
    # for doc in list(input_data.values())[0:10]:
    #     print(doc["content"])
    # count = 0
    # for doc in list(input_data.values()):
    #     count +=1
    # print(count)
    # print(stopwords_list())
    test_normalize()

