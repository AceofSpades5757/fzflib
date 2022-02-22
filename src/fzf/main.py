import logging.config
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
