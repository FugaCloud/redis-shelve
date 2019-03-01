from shelve import Shelf


class RedisShelf(Shelf):
    def __init__(self, redis, key_prefix=None, protocol=None, writeback=False):
        self._prefix = '{}|'.format(key_prefix) if key_prefix else ''
        Shelf.__init__(
            self, dict=redis, protocol=protocol, writeback=writeback)

    def _prefix_key(self, key):
        if not self._prefix:
            return key
        if key.startswith('{}'.format(self._prefix)):
            # with writeback, shelf values are added by keys from cache.keys(),
            # but the cache keys are already prefixed.
            return key
        return "{prefix}{key}".format(prefix=self._prefix, key=key)

    def _remove_key_prefix(self, prefixed_key):
        return prefixed_key[len(self._prefix):]

    def __setitem__(self, key, value):
        return Shelf.__setitem__(self, self._prefix_key(key), value)

    def __getitem__(self, key):
        return Shelf.__getitem__(self, self._prefix_key(key))

    def __delitem__(self, key):
        return Shelf.__delitem__(self, self._prefix_key(key))

    def get(self, key, default=None):
        # Redis supports __getitem__ for getting values from redis
        # like redis['somevalue']. But redis.get actually gets things from
        # cache, breaking the dict-like behaviour.
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __len__(self):
        return len(self._redis_keys())

    def _redis_keys(self):
        # self.dict is actually redis.
        return self.dict.keys(pattern='{}*'.format(self._prefix))

    def __iter__(self):
        for key in self._redis_keys():
            our_key = self._remove_key_prefix(key.decode())
            yield our_key


def open(redis, key_prefix=None, protocol=None, writeback=False):
    return RedisShelf(
        redis, key_prefix, protocol=protocol, writeback=writeback)
