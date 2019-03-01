from setuptools import setup, find_packages

setup(
    name='redishelve',
    version='1.0.0',
    author='Niels van Huijstee',
    author_email='niels@fuga.cloud',
    description='Alternative shelve that uses Redis as storage',
    packages=find_packages(),
    install_requires=[
        'redis',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta", "License :: Public Domain",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers", "Topic :: Utilities"
    ]
)
