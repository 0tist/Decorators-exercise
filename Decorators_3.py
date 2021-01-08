from decorators import debugger, timer, do_twice
import functools
# Decorators on classes

class spend_time:

    @debugger
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @timer
    def repeat(self):
        for i in range(10000):
            print(f'name is {self.name}')
            print(f'{self.age} years old')

obj = spend_time('jayesh', 21)
obj.repeat()

# lets see if we can put our timer decorator on a class

@timer
class waste_time():

    def __init__(self, num: int):
        self.num  = num

    def waster(self):
        l = [i for i in range(10000000)]

# with this the timer only takes the time that is used to instantiate the class or execute __init__ function
wt = waste_time(10000)
wt.waster()

# we can also nest the python decorators

@debugger
@do_twice
def greet_me():
    print("hello this is computron!")

greet_me()

# sequence of defining the decorators matters

@do_twice
@debugger
def greet_me():
    print("hello this is computron!")

greet_me()

# Decorators with arguments
# for exmple: do_twice can be changed to repeat(n_times)

def repeat(n_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            for i in n_times:
                value = func(*args, **kwargs)
            return value
        return wrap
    return repeat_decorator

# this looks nasty but its very similar to the previous decorators we wrote, the only difference is
# it takes another def to give arguments