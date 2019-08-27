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

from setuptools import setup

setup(
    install_requires=[
        'redis',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    packages=['redisshelve'],
    tests_require=[
        'fakeredis',
        'pytest',
        'pytest-cov',
    ],
)
