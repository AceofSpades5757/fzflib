import logging.config
import os
from pathlib import Path


logs_path: Path = Path(__file__).parent / 'logs'
logs_path.mkdir(exist_ok=True)
log_file: Path = logs_path / Path(__file__).with_suffix('.log').name


logging_config: dict = dict(
    version=1,
    disable_existing_loggers=False,
    root=dict(
        level=logging.DEBUG,
        handlers=['file_handler'],
    ),
    formatters={
        'default': {
            'date_format': '%Y-%m-%dT%H:%M:%S+0000%z',
            'format': '{asctime} - {name} - {levelname:<8} - {message}',
            'style': '{',
            'validate': True,
        }
    },
    handlers={
        'file_handler': {
            'level': logging.DEBUG,
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': log_file,
        }
    },
    loggers={},
)


def get_logger(options: dict = None) -> "Logger":
    """Get logger."""

    # Default Options
    if options is None:
        options = dict(
            name='root',
        )

    # Get Logger
    name: str = options['name']
    logger = logging.getLogger(name)

    # Global Helpers
    date_format = '%Y-%m-%dT%H:%M:%S%z'
    message_format = '{asctime} - {name} - {levelname:<8} - {message}'
    formatter = logging.Formatter(
        datefmt=date_format,
        style='{',
        fmt=message_format,
    )

    # Debug
    if os.environ.get('FZFLIB_DEBUG') is not None:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)

    return logger
