def decorator_with_args(arg1, arg2):
    def actual_decorator(func):
        def wrapper(name):
            print(f"{arg1}")
            func(name)
            print(f"{arg2}")
           # func( * args, ** kwargs)
        return wrapper
    return actual_decorator

@decorator_with_args("Starting...", "Ending...")
def greet(name):

    print(f"Hi, {name}!")
greet("John")
