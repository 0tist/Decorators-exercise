# you can pass functions as arguments to a function
# First class objects
def say_hello(name):
    return f'Hello {name}'


def share_name(name):
    return f'Hello from {name}'


def greeter_function(greet):
    return greet('Jayesh')


print(greeter_function(share_name))  # when we pass the function as a param, notice that we have passed '()'


# this means that only the reference to the function is passed as the parameter.


# Inner Functions

def parent():
    print("printing parent function")

    def first_child():
        print("print first child")

    def second_child():
        print("print second child")

    second_child()
    first_child()


parent()


# first_child() and second_child() are only defined in the scope of parent() that means you can't call it outside.

# Returning function from a function

def parent(num):
    def first_child():
        print("this is first speaking")

    def second_child():
        print("this is second, pleasure to meet ya!")

    if num == 1:
        return first_child

    return second_child


first = parent(1)
print(first)
first()


# pyhton beast Decorator

def my_decorator(func):
    print("into the decorator function")

    def wrapper():
        print("something happening before the function is executed")
        func()
        print("something happening after the function is executed")

    return wrapper


def say_whee():
    print("whee!")


whee = my_decorator(say_whee)
whee()


# Put simply: decorators are wrappers that wrap around a function to change its behaviour.

# syntactic Sugar
# using say_whee() to say whee repeatedly is sort of fuss, instead we'll do this

def my_decorator(func):
    def wrapper():
        print("do something part 1")
        func()
        print("do something part 2")

    return wrapper


@my_decorator
def say_whee():
    print('whee')


say_whee()

# so as we did in the previous example, we saw that we didnt have
# to obtain the reference of the function say_whee() like we have seen whee = my_decorator(say_whee)

from decorators import do_twice


@do_twice
def say_whee():
    print('whee!!!!')


# say_whee() this will give u


# what if we pass a parameterised function
# @do_twice
# def hello(name):
#     print(f'hello {name}')
#
# hello('mok')

# this gives me an error, as the function used in
# there's solution to this, just use args and kwargs, updates in decorators.py
@do_twice
def hello(name):
    print(f'hello {name}')


# yo = hello('mok') this gives me an error

hello('mok')


# now if, we wish to return some value, or store it in a container, we can't do this with the current wrapper we have
# instead just a SMALL change is enough to do that -> return fun(*args, **kwargs)

@do_twice
def hello(name):
    print(f'hello {name}')
    return f'name is: {name}'


yo = hello('kshit')
print(yo)

# Who are you really?
print(print)
print(print.__name__)
help(print)

print(say_whee)
print(say_whee.__name__)
help(say_whee)

# after trying to get the nsame of say_whee() with say_whee.__name__ we observed that the function is confused about its identity.
# which makes sense as the final excution of the function is inside the function wrapper_do_twice

# we can help say_whee() retain its identity by changing the decorators.py

print(say_whee)
print(say_whee.__name__)
help(say_whee) # problem solved hehe

# what if u want / not want arguments at the same time

# If name has been called without arguments, the decorated function will be passed in as _func. If it has been called with arguments, then _func will be None, and some of the keyword arguments may have been changed from their default values. The * in the argument list means that the remaining arguments can’t be called as positional arguments.
# In this case, the decorator was called with arguments. Return a decorator function that can read and return a function.
# In this case, the decorator was called without arguments. Apply the decorator to the function immediately.

def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat


    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def say_whee():
    print("Whee!")

@repeat(num_times)
def greet_me(name):
    print(f'Hello {name} this is computron!')

# stateful decorators
# so sometimes i need a wrapper to help me determine the state of the function

# lets start with the help of an example

def count_call(func):
    def wrapper_count(*args, **kwargs):
        wrapper_count.num_calls += 1
        #here we are using attributes of functions
        print(f"function {func}")