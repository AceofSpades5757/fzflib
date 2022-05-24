Quickstart
==========

Initialize an instance of FZF. Reasonable default options are set when none are given.

``fzf = FZF()``

You can even set different options.

``fzf = FZF(fzf='~/fzf.exe', multi=True)``

Set different options, like working directory, after having created the FZF instance.

``fzf.cwd: PathLike = '~'``
