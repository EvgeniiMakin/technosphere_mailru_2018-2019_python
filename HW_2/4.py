import functools
import time

def stopwatch(func):
    @functools.wraps(func)
    def wrapped(*args, **argv):
        print('`'+str(func.__name__)+'` started')
        time_start = time.perf_counter()
        result = func(*args, **argv)
        time_finish = time.perf_counter()
        time_watch = time_finish - time_start
        print('`'+str(func.__name__)+'` finished in '+str(round(time_watch,2))+'s')
        return result
    return wrapped