# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='flatmapy',
    version='0.0.2',
    description="Provide scala's flatMap with Python",
    long_description=readme,
    author='Futoshi Nagata',
    author_email='futoshinagata@gmail.com',
    url='https://github.com/futnag/flatmapy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

