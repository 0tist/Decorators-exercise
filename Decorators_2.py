# lets dive into some real world applicaitons

# I made some changes to have a neat boilerplate for create our applications

# lets start with a timer application

import functools
import time

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

@timer
def waste_some_time(num):
    for _ in range(num):
        sum([i**2 for i in range(1000)])

waste_some_time(10)
waste_some_time(1000)

### making our own debugger - SUPERRRR COOL

def debugger(func):
    @functools.wraps(func)
    def wrap_debugger(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f'{k} = {v!r}' for k, v in kwargs.items()]
        signature = ", ".join(args_list + kwargs_list)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrap_debugger


@debugger
def greeter(name, age=None):
    if age is None:
        return f'Hello {name}'

    return f'hello {name}, congratulations on {age}th birthday' # lol 1th birthday

greeter('lalit', 58)

# we can add this to decorator.py and then use import to use it here, though i'll keep the above code for reference.

from decorators import debugger
import math
#another example

math.factorial = debugger(math.factorial)

def approximate_e(n_terms=20):
    return sum(1/math.factorial(i) for i in range(n_terms))

value = approximate_e()
print(value)

# another example - slow down the python code or delay its execution (might not be very useful)
import time

def slow_down(func):
    @functools.wraps(func)
    def wrap_slowly(*args, **kwargs):
        time.sleep(1)
        value = func(*args, **kwargs)
        return value
    return wrap_slowly

@slow_down
def add(n1, n2):
    return n1+n2

value = add(3, 4)
print(value)

import random
PLUGINS = dict()

def register(func):
    '''register a function as a plug-in'''
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f'Hello {name}!'

@register
def be_awesome(name):
    return f'{name}! you are awesome'

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f'using {greeter!r}')
    return greeter_func(name)

greetings = randomly_greet('Jayesh')
print(greetings)

# Then there's this crazy secret login webpage decorator example
# check it out on: https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples


