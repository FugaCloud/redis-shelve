import collections
import pickle


class RedisShelf(collections.abc.MutableMapping):
    def __init__(self, redis, filename):
        self._prefix = filename
        self._redis = redis
        self._keys = []

    def _create_shelf_key(self, key):
        return "{prefix}|{key}".format(prefix=self._prefix, key=key)

    def _create_key(self, shelf_key):
        left = '{prefix}|'.format(prefix=self._prefix)
        key = shelf_key[len(left):]
        return key

    def _update_keys(self, shelf_key):
        if shelf_key not in self._keys:
            self._keys.append(shelf_key)

    def __setitem__(self, key, value):
        shelf_key = self._create_shelf_key(key)
        self._update_keys(shelf_key)
        pickled = pickle.dumps(value)
        self._redis.set(shelf_key, pickled)

    def __getitem__(self, key):
        shelf_key = self._create_shelf_key(key)
        if shelf_key not in self._keys:
            return None

        pickled = self._redis.get(shelf_key)
        return pickle.loads(pickled)

    def __delitem__(self, key):
        shelf_key = self._create_shelf_key(key)
        self._redis.delete(shelf_key)
        self._keys.remove(shelf_key)

    def __iter__(self):
        for shelf_key in self._keys:
            key = self._create_key(shelf_key)
            yield key

    def __len__(self):
        return len(self._keys)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


def open(filename, redis):
    return RedisShelf(redis, filename)
