import logging.config
import platform
import subprocess
from pathlib import Path
from typing import List
from typing import Optional
from typing import Union

from fzf.constants import ENCODING
from fzf.constants import MULTI_FLAG
from fzf.logging_ import logging_config
from fzf.utilities import resolve_input


PathLike = Union[bytes, str, Path]


logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


class FZF:
    """Class abstracting FZF command."""

    def __init__(
        self,
        executable: str = None,
        input: Optional[str] = None,
        cwd: PathLike = None,
        multi: bool = False,
        fzf_extras: List[str] = None,
    ) -> None:

        if executable is None:
            executable = 'fzf'
        if fzf_extras is None:
            fzf_extras = []

        self.fzf = executable
        self.input = input
        self.cwd: Optional[PathLike] = cwd
        self.multi: bool = multi

        # Extra Arguments
        self.fzf_args: List = fzf_extras

    def run(self, *args, **kwargs) -> Union[str, List[str]]:
        """Given current configuration, run fzf and return selection."""

        # Buid Command
        command: List[str] = [self.fzf]
        if self.multi:
            command.append(MULTI_FLAG)

        command += self.fzf_args

        input_: bytes = resolve_input(self.input)
        if input_:
            kwargs['stdin'] = subprocess.PIPE

        # Run FZF as Process
        process: subprocess.Popen = subprocess.Popen(
            command,
            *args,
            stdout=subprocess.PIPE,
            encoding=ENCODING,
            cwd=self.cwd,
            **kwargs,
        )  # type: ignore

        # Process - Input
        if input_:
            stdout, _ = process.communicate(input_.decode(ENCODING))
        else:
            stdout, _ = process.communicate()

        # Process - Output
        if self.multi:
            return stdout.splitlines()
        else:
            return stdout.strip()

    @classmethod
    def install(cls, method=None, dry_run: bool = False) -> None:
        """Install fzf, using git.

        Will attempt to install FZF, if possible, matching the style of
        `fzf#install()` from the Vim plugin installation.

        [Documentation](https://github.com/junegunn/fzf#using-git)
        """
        cls.download(method=method)

        if dry_run:
            return
        else:
            cls._run_installer()

    @classmethod
    def _run_installer(cls) -> None:
        """Run fzf installer."""

        download_dir: Path = Path('./fzf')
        process_options: dict = {}

        if platform == 'Windows':
            install_script: Path = download_dir / 'install.ps1'
        else:
            install_script = download_dir / 'install'

        subprocess.run(['powershell.exe', install_script], **process_options)

    @classmethod
    def download(cls, method: str = None) -> None:

        if method is None:
            method = 'https'
        method = method.lower()

        options: List[str] = [
            *('--depth', '1'),
        ]

        if method == 'https' or method == 'http':
            exe: str = 'git'
            args: List[str] = [
                'clone',
            ]
            uri: str = 'https://github.com/junegunn/fzf.git'
        elif method == 'ssh':
            exe = 'git'
            args = [
                'clone',
            ]
            uri = 'git@github.com:junegunn/fzf.git'
        elif method == 'gh':
            exe = 'gh'
            args = [
                'repo',
                'clone',
            ]
            options = []
            uri = 'junegunn/fzf'

        command: List[str] = [exe] + args + options + [uri]

        subprocess.run(command)
