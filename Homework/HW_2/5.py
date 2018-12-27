import functools
def once(func):
    cache = dict()
    @functools.wraps(func)
    def wrapper(*args):
        key = (func, args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    return wrapper