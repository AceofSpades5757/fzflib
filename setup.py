#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools


with open('README.md', 'r', encoding='utf-8') as fin:
    long_description = fin.read()


setuptools.setup(
    name='fzflib',
    version='0.1.15',
    license='MIT',
    author='Kyle L. Davis',
    author_email='AceofSpades5757.github@gmail.com',
    url='https://github.com/AceofSpades5757/fzflib',
    project_urls={
        'Documentation': 'https://fzflib.readthedocs.io/en/latest/',
        'Author': 'https://github.com/AceofSpades5757',
    },
    description='A Python library for interacting with FZF.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src', 'fzflib': 'src/fzflib'},
    test_suite="tests",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
