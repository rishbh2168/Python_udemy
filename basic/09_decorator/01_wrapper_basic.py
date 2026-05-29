from functools import wraps

def my_decorator(func):  #---- param as func
    @wraps(func)
    def wrapper():
        print("before function run")
        func()   #----- decorator function
        print("after function run")
    return wrapper

@my_decorator   #---- run decorator

def greet():
    print("hello i am decorator")    #----- decorator function

greet()