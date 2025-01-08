class Storage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._storage = {}  # Initialize storage as an empty dictionary
        return cls._instance

    def set(self, key, value):
        self._storage[key] = value

    def get(self, key, default=None):
        return self._storage.get(key, default)

    def remove(self, key):
        if key in self._storage:
            del self._storage[key]

    def clear(self):
        self._storage.clear()

