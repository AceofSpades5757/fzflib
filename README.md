[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fzflib?label=Python%20Version&logo=python&logoColor=yellow)
![PyPI - License](https://img.shields.io/pypi/l/fzflib?color=green)
![PyPI](https://img.shields.io/pypi/v/fzflib?color=darkred)
[![Coverage](https://github.com/AceofSpades5757/fzflib/actions/workflows/tests.yml/badge.svg)](https://github.com/AceofSpades5757/fzflib/actions/workflows/tests.yml)

# Description

Bring the incredible utility of FZF to Python.

Probably one of the best tools I've ever found.

# Installation

Using the official The Python Package Index (PyPI).

`pip install fzflib`

## Requirements

- [FZF](https://github.com/junegunn/fzf)

# Usage

Create an FZF instance.

`fzf = FZF()`

Create an FZF instance, with additional options during instantiation.

`fzf = FZF(fzf='~/fzf.exe', multi=True)`

## Change Options

Use the FZF instance to search for various options.

```python
fzf.input = ['option 1', 'option 2']
fzf.prompt()
```

Set different working directory, when running FZF.

`fzf.cwd: PathLike = '~'`

## Install FZF

This will attempt to install FZF on your machine.

`FZF.install()`

# Contribution

This package follows a similar style found in the Python standard library of using a central class, or set of classes, to generate a set of useful functions (e.g. `difflib`).

Feel free to submit an Issue for any bugs, or suggestions.

Support the people behind [FZF](https://github.com/junegunn/fzf).
