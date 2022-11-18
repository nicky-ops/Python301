def my_decorator(func):
    def wrapper():
        print("Hello world")
        func()
        print("Original function finished executing")
    return wrapper

@my_decorator
def name():
    print("My name is Kangaroo")

name()