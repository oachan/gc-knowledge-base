def timeit(func):
    fname = func.__name__

    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        logging.info("The '{}' cost time is {}.".format(fname, te - ts))

    return timed