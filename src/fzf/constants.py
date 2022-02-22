import sys

if sys.version_info > (3, 7):
    from typing import Final
from typing import Iterable
from typing import Union


if sys.version_info > (3, 7):
    ENCODING: Final[str] = 'utf-8'
    MULTI_FLAG: Final[str] = '--multi'
else:
    ENCODING: str = 'utf-8'
    MULTI_FLAG: str = '--multi'
FZFInputValues = Union[bytes, str, Iterable[str], Iterable[bytes]]
