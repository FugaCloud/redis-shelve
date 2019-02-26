import fakeredis
import pytest

from redishelve import RedisShelve


@pytest.fixture
def redis():
    fake_server = fakeredis.FakeServer()
    fake_redis = fakeredis.FakeStrictRedis(
        server=fake_server, decode_responses=True)
    return fake_redis


def test_shelve_value(redis):
    shelve = RedisShelve(redis)
    shelve['test'] = 'TEST'
    assert 'TEST' == shelve['test']
