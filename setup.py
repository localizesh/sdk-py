from setuptools import setup

setup(
    name='localizesh-sdk',
    version='0.0.3',
    description="Sdk",
    package_dir={"localizesh_sdk": "src"},
    long_description=open('README.md').read(),
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
)