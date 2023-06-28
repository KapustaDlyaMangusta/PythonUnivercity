import logging


def logger(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                level = logging.ERROR

                if mode == "console":
                    logging.basicConfig(
                        level=level)
                elif mode == "file":
                    logging.basicConfig(
                        filename="error.log",
                        level=level)

                logging.error(e)

        return wrapper

    return decorator
