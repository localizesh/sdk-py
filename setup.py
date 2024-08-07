from setuptools import setup, find_packages

setup(
    name='sdk-py',
    version='0.1.3',
    description="Sdk",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=open('README.md').read(),
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
)