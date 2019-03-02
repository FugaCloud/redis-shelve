# Copyright (c) 2019 Cyso < development [at] cyso . com >
#
# This file is part of redis-shelve.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see
# <http://www.gnu.org/licenses/>.

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
            print(key)
            our_key = self._remove_key_prefix(key.decode())
            print(our_key)
            yield our_key


def open(redis, key_prefix=None, protocol=None, writeback=False):
    return RedisShelf(
        redis, key_prefix, protocol=protocol, writeback=writeback)
