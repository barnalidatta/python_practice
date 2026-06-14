# difference __str__ and __repr__
# The Cheat Sheet: What Triggers Which Method?
# If you write this in your code......Python triggers this method behind the scenes
# print(obj) --> __str__
# str(obj) -->__str__
# f"Hello {obj}" -->__str__
# repr(obj) -->__repr__
# [obj, obj2] (Inside any collection) -->__repr__
# Just typing obj in the interactive terminal -->__repr__
#
# __repr__ acts as a backup safety net for __str__.
# If you define only __str__ and try to put your object in a list, Python ignores __str__ and falls back to printing the ugly default memory address (<__main__.Child object at 0x...>).
# If you define only __repr__, it covers both bases! If __str__ is completely missing, Python will automatically use your __repr__ string as a fallback for regular print() statements.
# Because of this fallback behavior, Python developers follow a golden rule: Always define __repr__ first.

class adder:
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        self.data += other    
        return self

class Child(adder):
    def __str__(self):
        return "user friendly %s" %self.data

    def __repr__(self):
        return "developer friendly %s" %self.data

a = Child(10)
a = a+1
# built-in str() works on string.This is built-in str() on object.
print(a)
print(f"which one triggers f-string --> {a!r}")
mylist=[a]
print(mylist)

# print(getattr(a, "__str__"))
# print(getattr(a,  "__repr__"))
