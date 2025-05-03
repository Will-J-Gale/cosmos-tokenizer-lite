from setuptools import setup, find_packages

setup(
    name='cosmos-tokenizer-lite',
    version='0.1.0',
    packages=find_packages(include=['cosmos_tokenizer', 'cosmos_tokenizer.*']),
    description='Cosmos Tokenizer Lite'
)