# lets wrap classes with decorators
# as we have seen previously.....@my_decorator is just an easier way to write my_decorator(func)
# so in this case, we will have to have pass the 'func' in __init__ in order to pass the parameter to the class

class counter:

    def __init__(self, start = 0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

# __call__ will be called each time you use call a particular instance(object) of the class

count_1 = counter()
count_2 = counter()
count_3 = counter()

count_1()
print(count_1.count)
count_2()
count_2()
print(count_2.count)
count_3()
count_3()
count_3()
print(count_3.count)

# lets do this

import functools

class CountCalls:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.n_calls = 0

    def __call__(self, *args, **kwargs):
        self.n_calls += 1
        print(f"call {self.n_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

# handy tip: its good to add a return statement of the function in the decorator class/function

@CountCalls
def say_whee():
    print("wheeeeeeee!")

say_whee()
say_whee()