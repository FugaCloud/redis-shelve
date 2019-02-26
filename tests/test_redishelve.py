import fakeredis
import pytest
from redishelve import RedisShelf


@pytest.fixture
def redis():
    fake_server = fakeredis.FakeServer()
    fake_redis = fakeredis.FakeStrictRedis(
        server=fake_server)
    return fake_redis


@pytest.fixture
def shelf(redis):
    return RedisShelf(redis, filename='test')


def test_shelf_value(shelf):
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
