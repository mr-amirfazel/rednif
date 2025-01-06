import Preprocess.normalize

if __name__ == "__main__":
    def test_normalize():
        test_text = """
          ﷽   این یک پیام می باشد. این پیامها زشتند. 123 سالِ پیشّ هوا سرد نمیتوانم برم بَیرون. ! ای بابا # چرا ، نمیشه کاری کَرد
        """
        print("parsivar: ")
        print(Preprocess.normalize.parsivar_normalizer(test_text))
        print("hazm: ")
        print(Preprocess.normalize.hazm_normalizer(test_text))

    test_normalize()