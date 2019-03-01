# Redishelve

A python shelve that uses Redis as storage.

## Usage
```python
import redishelve

from redis import Redis

# create your redis instance
redis = Redis()

# Pass the redis instance
with redishelve.open(filename='my_shelf', redis=redis) as shelf:
    # use like a python shelve
    shelf['foo'] = 'Bar'
```
