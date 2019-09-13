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

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Niels van Huijstee",
    author_email="niels@fuga.cloud",
    classifier=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    descripion="Alternative shelve that uses Redis as storage",
    install_requires=["redis"],
    license="GNU Lesser General Public License v3 (LGPLv3)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="redis-shelve",
    packages=["redisshelve"],
    setup_requires=["pytest-runner"],
    tests_require=["fakeredis", "pytest", "pytest-cov"],
    url="https://github.com/FugaCloud/redis-shelve",
    version="1.0.3",
)
