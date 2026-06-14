def listing(func):
    def wrapper(*args, **kwargs):
        print("listing all arguments")
        result = func(*args,**kwargs)
        print(f"Result is {result}")
        return result
    return wrapper
@listing
def items():
    d = {"shoes":4,"socks":5}
    return d
items()