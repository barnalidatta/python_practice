# First class has no __init__, so setdata method is only pr
class Base:
    def __init__(self, value):
        self.data = value
    def setdata(self, val2):
        self.data = self.data + val2 
    def display(self):
        print(self.data)

# Second class is inheriting First. 
class Child(Base):
    def display(self):
        print(f"Current value is {self.data}")

# if instance is created in different file after importing the filename(class2), then obj = class2.Child("abc")
# but if you do from class2 import Child , then you can write obj=Child("abc)
# because "import class2" creats a module object
# obj = Child("abc")
# # 1. Is it in the instance memory space?
# print('setdata' in obj.__dict__)          # Output: False
# print('data' in obj.__dict__)             # Output: True
# # 2. Is it in the child blueprint memory space?
# print('setdata' in Child.__dict__)        # Output: False
# print('data' in Child.__dict__)        # Output: False
# # 3. Is it in the base blueprint memory space?
# print('setdata' in Base.__dict__)         # Output: True
# print('data' in Base.__dict__)         # Output: False

#    FROM Interpreter
# >>> from class2 import Base, Child
#
# >>> Base.__dict__
# mappingproxy({'__module__': 'class2', '__init__': <function Base.__init__ at 0x000001656EA3D4E0>, 'setdata': <function Base.setdata at 0x000001656EA3D580>, 'display': <function Base.display at 0x000001656EA3D620>, '__dict__': <attribute '__dict__' of 'Base' objects>, '__weakref__': <attribute '__weakref__' of 'Base' objects>, '__doc__': None})
# >>> Child.__dict__
# mappingproxy({'__module__': 'class2', 'display': <function Child.display at 0x000001656EA3D6C0>, '__doc__': None})
# 
# >>> obj1=Base("sss")
# >>> obj1.__dict__
# {'data': 'sss'}
#
# >>> obj2=Child("abc")
# >>> obj2.__dict__    
# {'data': 'abc'}
#
# >>> print(dir(obj1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data', 'display', 'setdata']
# >>> print(dir(obj2)) 
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data', 'display', 'setdata']

# >>> print(dir(Base))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'display', 'setdata']
# >>> print(dir(Child))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'display', 'setdata']
# 
# >>> obj1.__class__
# <class 'class2.Base'>
# >>> obj2.__class__
# <class 'class2.Child'>
#
# >>> obj1.__bases__
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Base' object has no attribute '__bases__'. Did you mean: '__class__'?
# >>> obj2.__bases__
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Child' object has no attribute '__bases__'. Did you mean: '__class__'?
#
# >>> Base.__bases__
# (<class 'object'>,)
# >>> Child.__bases__
# (<class 'class2.Base'>,)
#
# >>> Base.__class__
# <class 'type'>
# >>> Child.__class__
# <class 'type'>
# >>> 
