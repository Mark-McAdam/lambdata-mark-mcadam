# setup.py

from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup (
    name='lambdata-mark-mcadam',
    version='1.0',
    author='Mark McAdam',
    author_email='mark.a.mcadam@gmail.com',
    description='For example description, read this',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # license = 'MIT',
    url='https://github.com/Mark-McAdam/lambdata-mark-mcadam',
    # keywords = 'lambdata util stuff etc',
    packages=find_packages()
)