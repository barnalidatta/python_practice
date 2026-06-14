class Test:
    def __init__(self):
        self.__x = 10
    
    def get_x(self):
        return self.__x
    
t = Test()

#print(t.__x) # No complains but AttributeError
#print(t._Test__x) # works when no get_x method defined but pylance complains
print(t.get_x())

