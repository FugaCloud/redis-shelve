# Redishelve

A python shelve that uses Redis as storage.

## Usage

```python
import redishelve
from redis import Redis

redis = Redis()
shelf = redishelve.RedisShelve(redis=redis)

shelf['test'] = 'Test'
assert 'Test' == shelf['test']
assert 'Test' == shelf.get('test')
```

You can also use the `redishelve.open` context manager.

```python
with redishelve.open(redis=redis) as shelf:
    shelf['foo'] = 'Bar'
```

## Prefixing keys
By default, the keys you enter in the shelf are used as keys in Redis. If you
think this might conflict with existing values, you can prefix your keys.  

As a side effect, if you also use writeback, the keys in the shelf's cache
are also prefixed.

```python
shelf = redishelve.RedisShelve(redis=redis, key_prefix='my_prefix')

with redishelve.open(redis=redis, key_prefix='my_prefix') as shelf:
    shelf['foo'] = 'Bar'
```


Please see the tests for more examples.  
unprefixed: [tests/test_redishelve_unprefixed.py](tests/test_redishelve_unprefixed.py)  
prefixed: [tests/test_redishelve_prefixed.py](tests/test_redishelve_prefixed.py)
