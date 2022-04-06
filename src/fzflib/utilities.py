from typing import Iterable
from typing import Optional
from typing import Union

from fzf.constants import ENCODING
from fzf.constants import FZFInputValues


def resolve_input(input_values: Optional[FZFInputValues]) -> bytes:
    """Resolve input values, for FZF, to bytes."""

    if not input_values:
        return b''

    if isinstance(input_values, bytes):
        return input_values

    if isinstance(input_values, str):
        return input_values.encode(ENCODING)

    if isinstance(input_values, Iterable):

        first_value: Union[str, bytes] = input_values[0]  # type: ignore

        if isinstance(first_value, bytes):
            return b'\n'.join(input_values)  # type: ignore
        elif isinstance(first_value, str):
            return '\n'.join(input_values).encode(ENCODING)  # type: ignore

    raise TypeError(f'Unsupported input type: {type(input_values)}')
