def log(text: str, condition: bool):
    end = "\n" if condition else ''
    print(text if condition else '', end=end)