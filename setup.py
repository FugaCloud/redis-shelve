from setuptools import setup, find_packages

setup(
    name='Redishelve',
    version = '0.0.1',
    author = 'Niels van Huijstee',
    author_email = 'niels@fuga.cloud',
    description = 'Alternative shelve that uses Redis as storage',
    packages = find_packages(),    
    install_requires=[
        'redis',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'fakeredis',
    ]
)