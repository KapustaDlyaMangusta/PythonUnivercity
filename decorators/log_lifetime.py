def log_lifetime(func):
    def wrapper(*args, **kwargs):
        print("Function params:")
        print("args: ", args)
        print("kwargs: ", kwargs)

        print("Started...")

        print("Getting results...")
        result = func(*args, **kwargs)

        print("Result:")
        print("returned: ", result)

        print("Ended...")

        return result

    return wrapper
