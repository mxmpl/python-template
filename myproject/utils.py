import logging
import sys


def get_logger(
    name: str,
    level: str,
    formatter: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
) -> logging.Logger:
    """Configures and returns a logger sending messages to standard error
    Parameters
    ----------
    name : str
        Name of the created logger, to be displayed in the header of
        log messages.
    level : str
        The minimum log level handled by the logger (any message above
        this level will be ignored). Must be 'debug', 'info',
        'warning' or 'error'. Default to 'warning'.
    formatter : str
        A string to format the log messages, see
        https://docs.python.org/3/library/logging.html#formatter-objects. By
        default display level and message. Use '%(asctime)s -
        %(levelname)s - %(name)s - %(message)s' to display time,
        level, name and message.
    Returns
    -------
    logging.Logger
        A configured logging instance displaying messages to the
        standard error stream.
    Raises
    ------
    ValueError
        If the logging `level` is not 'debug', 'info', 'warning' or
        'error'.
    """
    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
    }

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter(formatter))

    logger = logging.getLogger(name)
    logger.handlers = []
    logger.addHandler(handler)

    try:
        logger.setLevel(levels[level])
    except KeyError:
        raise ValueError(
            "Invalid logging level '{}', must be in {}".format(
                level, ", ".join(levels.keys())
            )
        )
    return logger
