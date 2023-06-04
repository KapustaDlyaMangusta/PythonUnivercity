def print_iterable_length(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            length = len(result)
        except TypeError:
            length = 1

        print(f"Length of result of this function is {length}")
        return result

    return wrapper
