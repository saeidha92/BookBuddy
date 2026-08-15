import time
from config.logger import logger


def retry(times=3, delay=0.5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except OSError as e:
                    logger.warning(f"Attempt {attempt}/{times} failed: {e}")
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
