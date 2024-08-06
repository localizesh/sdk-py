from setuptools import setup, find_packages

setup(
    name='sdk-py',
    version='0.0.3',
    description="Sdk",
    packages=find_packages(),
    long_description=open('README.md').read(),
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
)