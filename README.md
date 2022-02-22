# Description

Bring the incredible utility of FZF to Python.

Probably one of the best tools I've ever found.

# Installation

## Requirements

* [FZF](https://github.com/junegunn/fzf)

# Usage

Create an FZF instance.

`fzf = FZF()`

Create an FZF instance, with additional options during instantiation.

`fzf = FZF(fzf='~/fzf.exe', multi=True)`

## Change Options

Use the FZF instance to search for various options.

```python
fzf.input = ['option 1', 'option 2']
fzf.run()
```

Set different working directory, when running FZF.

`fzf.cwd: PathLike = '~'`

# Contribution

This package follows a similar style found in the Python standard library of using a central class, or set of classes, to generate a set of useful functions (e.g. `difflib`).

Feel free to submit an Issue for any bugs, or suggestions.

Support the people behind [FZF](https://github.com/junegunn/fzf).
