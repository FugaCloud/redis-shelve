class RedisShelve:
    def __init__(self, redis):
        self._redis = redis

    def __setitem__(self, key, value):
        print(f'SET KEY {key} VAL {value}')
        self._redis.set(key, value)

    def __getitem__(self, key):
        print(f'GET KEY {key}')
        return self._redis.get(key)
