# Redis Shelve
[![Build status](https://img.shields.io/travis/FugaCloud/redis-shelve.svg)](https://travis-ci.org/FugaCloud/redis-shelve)  
A Python shelve that uses Redis as storage. 

## Motivation
In some contexts writing state to files can be hard. Redis can be a more
suitable storage solution. If you need a shelve but cannot write to file and 
if you are friends with Redis already, you can use Redis Shelve.

## License
Redis Shelve is licensed under LGPLv3. See the LICENSE file for details.

## Installation
`pip install redis-shelve`

## Usage
The behaviour of the Redis shelve should be similar to Python shelve. Instead
of a filename, you can pass redis-shelve a redis instance. You can think of the
configured redis database being similiar to a file in Python shelve.

```python
import redisshelve
from redis import Redis

redis = Redis(db=15)
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

**NB:** As a side effect, if you also use writeback, the keys in the shelf's cache
are also prefixed.

```python
shelf = redisshelve.RedisShelf(redis=redis, key_prefix='my_prefix')

with redisshelve.open(redis=redis, key_prefix='my_prefix') as shelf:
    shelf['foo'] = 'Bar'
```

## More examples.

Please see the tests for more examples.  
  
unprefixed: `tests/test_redisshelve_unprefixed.py`  
prefixed: `tests/test_redisshelve_prefixed.py`
