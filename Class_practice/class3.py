class Add:
    def __init__(self, value):
        self.data = value 
        #self.display() # Function call when instance is created 

    def display(self):
        print(self.data)

a=Add(4)
print(f"value is {a.data}")
#print(a)
# print(dir(a)) # Shows methods available to the instance
# print(a.__dict__) # only data
# print(Add.__dict__.keys())
# a.display()