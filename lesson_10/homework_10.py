import logging
import os

def _get_log_path() -> str:
    return os.path.join(os.path.dirname(__file__), "login_system.log")

def _get_logger() -> logging.Logger:

    log_path = _get_log_path()
    logger = logging.getLogger("login_system_logger")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        logger.handlers.clear()

    fh = logging.FileHandler(log_path, encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger

def log_event(username: str, status: str):

    logger = _get_logger()
    message = f"Login event – Username: {username}, Status: {status}"

    if status == "success":
        logger.info(message)
    elif status == "expired":
        logger.warning(message)
    else:
        logger.error(message)