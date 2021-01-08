# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
# In order for the above code to accept the parameters/arguments passed to it. we'll have to args and kwargs(keyword arguments)
#
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice

# SMALL change

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice

#HELP say_whee() keep its name

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

### BOILER PLATE for decorators

import functools
import time

def decorator(func):
    @functools.wrap(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value
    return wrapper_decorator

def debugger(func):
    @functools.wraps(func)
    def wrap_debugger(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ", ".join(args_list + kwargs_list)
        print(f'calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value}')
        return value
    return wrap_debugger

def timer(func):
    """print the runtime of the decortaor function"""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        t1 = time.time()
        value = func(*args, **kwargs)
        t2 = time.time()
        time_consumed = t2-t1
        print(f"Time consumed to execute {func.__name__} = {time_consumed} seconds")
        return value
    return wrapper_decorator

