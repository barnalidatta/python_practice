
# Decorator
def add_greeting(func):
    def wrapper(name):
        return f"Greetings, {func(name)}"
    return wrapper

# Using the decorator
@add_greeting
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))