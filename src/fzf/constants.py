from typing import Final
from typing import Iterable
from typing import Union


ENCODING: Final[str] = 'utf-8'
FZFInputValues = Union[bytes, str, Iterable[str], Iterable[bytes]]
MULTI_FLAG: Final[str] = '--multi'
