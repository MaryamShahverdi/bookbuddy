from functools import wraps
from config.logger import logger

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Running: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished: {func.__name__}")
        return result
    return wrapper
