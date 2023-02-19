import time
import timeit

#lowest seen: 4.999872700005653

def speedCheck():
    start = timeit.default_timer()

    time.sleep(5)

    stop = timeit.default_timer()

    if stop - start < 5:
        return True

    return False
