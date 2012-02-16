def TODO(func):
    """unittest test method decorator that ignores
       exceptions raised by test
   
    Used to annotate test methods for code that may
    not be written yet.  Ignores failures in the
    annotated test method; fails if the text
    unexpectedly succeeds.
    """
    def wrapper(*args, **kw):
        try:
            func(*args, **kw)
            succeeded = True
        except:
            succeeded = False
        assert succeeded is False, \
               "%s marked TODO but passed" % func.__name__
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper
