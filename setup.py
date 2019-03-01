from setuptools import setup, find_packages

setup(
    name='redis-shelve',
    version='1.0.0',
    author='Niels van Huijstee',
    author_email='niels@fuga.cloud',
    description='Alternative shelve that uses Redis as storage',
    packages=find_packages(),
    install_requires=[
        'redis',
    ],
    classifiers=[
        "Development Status:: 5 - Production / Stable",
        "Intended Audience :: Developers",
        "License:: OSI Approved:: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ]
)
