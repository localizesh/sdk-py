from setuptools import setup
import os

VERSION = os.environ.get('VERSION')

setup(
    name='localizesh-sdk',
    version=VERSION,
    description="Sdk",
    package_dir={"localizesh_sdk": "src"},
    long_description=open('README.md').read()
)
