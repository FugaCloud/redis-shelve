import pickle

import fakeredis
import pytest

from redishelve import RedisShelf


@pytest.fixture
def redis():
    fake_server = fakeredis.FakeServer()
    fake_redis = fakeredis.FakeStrictRedis(server=fake_server)
    return fake_redis


@pytest.fixture
def shelf(redis):
    return RedisShelf(redis=redis, key_prefix='test')


@pytest.fixture
def unprefixed_shelf(redis):
    return RedisShelf(redis=redis)


def test_shelf_value(shelf):
    shelf.writeback = True
    shelf['test'] = 'TEST'
    assert 'TEST' == shelf['test']


def test_shelf_get_method_returns_like_dict(shelf):
    shelf['test'] = 'TEST'
    assert 'TEST' == shelf.get('test')


def test_shelf_get_returns_none_as_default(shelf):
    assert None is shelf.get('nothing')


def test_shelf_len(shelf):
    shelf['one'] = 'ONE'
    shelf['two'] = 'TWO'

    assert 2 == len(shelf)


def test_shelf_iteration(shelf):
    shelf['one'] = 'ONE'
    shelf['two'] = 'TWO'

    assert ['one', 'two'] == list(shelf.keys())
    assert ['ONE', 'TWO'] == list(shelf.values())
    actual = {}
    for k, v in shelf.items():
        actual[k] = v
    assert {'one': 'ONE', 'two': 'TWO'} == actual


def test_shelf_delete(shelf):
    shelf['one'] = 'ONE'
    shelf['two'] = 'TWO'
    shelf['three'] = 'THREE'

    del (shelf['two'])

    assert None is shelf.get('two')


def test_shelf_shelves_to_redis(shelf, redis):
    shelf['test'] = 'TEST'
    assert 'TEST' == pickle.loads(redis.get(b'test|test'))


def test_mutable_values_with_writeback(redis):
    shelf = RedisShelf(key_prefix='test', redis=redis, writeback=True)
    shelf.writeback = True
    shelf['list'] = [1, 2, 3]
    shelf['list'].append(4)

    # before syncing, old value is in Redis.
    assert [1, 2, 3] == pickle.loads(redis.get(b'test|list'))
    shelf.sync()
    assert [1, 2, 3, 4] == pickle.loads(redis.get(b'test|list'))


def test_open_as_context_manager(redis):
    import redishelve

    with redishelve.open(key_prefix='test', redis=redis) as test_shelf:
        test_shelf['test'] = 'Test 1'
        assert 'Test 1' == test_shelf['test']

    with pytest.raises(ValueError):
        test_shelf['test']
