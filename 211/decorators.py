from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    retries = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal retries
        if retries > MAX_RETRIES:
            raise MaxRetriesException
        else:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
