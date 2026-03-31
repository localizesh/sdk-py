from setuptools import setup
import os

setup(
    name='localizesh-sdk',
    version=os.environ.get('VERSION'),
    description="Localize.sh SDK",
    package_dir={"localizesh_sdk": "src"},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
    install_requires=[
        'protobuf>=5.26.1',
    ],
)
