# Redishelve

A python shelve that uses Redis as storage.

## Usage

```python
import redisshelve
from redis import Redis

redis = Redis()
shelf = redisshelve.RedisShelf(redis=redis)

shelf['test'] = 'Test'
assert 'Test' == shelf['test']
assert 'Test' == shelf.get('test')
```

You can also use the `redisshelve.open` context manager.

```python
with redisshelve.open(redis=redis) as shelf:
    shelf['foo'] = 'Bar'
```

## Prefixing keys
By default, the keys you enter in the shelf are used as keys in Redis. If you
think this might conflict with existing values, you can prefix your keys.  

As a side effect, if you also use writeback, the keys in the shelf's cache
are also prefixed.

```python
shelf = redisshelve.RedisShelf(redis=redis, key_prefix='my_prefix')

with redisshelve.open(redis=redis, key_prefix='my_prefix') as shelf:
    shelf['foo'] = 'Bar'
```


Please see the tests for more examples.  
unprefixed: [tests/test_redisshelve_unprefixed.py](tests/test_redisshelve_unprefixed.py)  
prefixed: [tests/test_redisshelve_prefixed.py](tests/test_redisshelve_prefixed.py)
