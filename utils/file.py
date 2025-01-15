import gzip
import json
import pickle
from pathlib import Path


def json_reader(path):
    f = open(path)
    data = json.load(f)
    return data


def save_index_compressed(index, collection_size, file_path):
    with gzip.open(file_path, 'wb') as file:
        pickle.dump((index, collection_size), file)


def load_index_compressed(file_path):
    if Path(file_path).exists():
        with gzip.open(file_path, 'rb') as file:
            return pickle.load(file)
    else:
        return False
