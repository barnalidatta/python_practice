# Dictionary Builtin
# get()
# items()
# keys()
# values()
# update()
# pop()
# setdefault()
# copy()
# clear()
# fromkeys()
# popitem()
# Common Built-in Functions Used With Dictionaries
# len()
# in
# del
# sorted()
# max()
class MyDict:
    def __init__(self):
        self.data = {}

    def check_empty(self):
        if not self.data:
            raise KeyError("Dictionary is empty")
    
    def check_missing_key(self,key):
        if key not in self.data:
            raise KeyError(f"Missing key: {key}")
    
    def get_item(self,key):
        self.check_empty()
        self.check_missing_key(key)
        return self.data[key]
        #return self.data.get(key)
        
    def get_keys(self): 
        self.check_empty()
        return self.data.keys()
    
    def get_values(self):
        self.check_empty()
        return self.data.values()
    
    def remove_key(self,key):
        self.check_missing_key(key)
        return self.data.pop(key)
        # or 
        # return self.data.pop(key,None)

    def remove_last_item(self):
        self.check_empty()
        return self.data.popitem()
    
    def clear_alldata(self):
        self.check_empty()
        self.data.clear()
        
    def shallow_copy(self):
        self.check_empty()
        return self.data.copy()
           
    def update_item(self, key, value):
        self.check_empty()
        self.check_missing_key(key)
        self.data.update({key:value})

    def add_item(self,key,value):
        if key in self.data:
            raise KeyError(f"key already exists {key}")
        self.data[key] = value

    def display(self):
        self.check_empty()
        for key,value in self.data.items():
            print(f"({key}:{value})")

    def sizeof_data(self):
        self.check_empty()
        return len(self.data)
    
    def maxof_values(self):
        if not self.data:
            raise ValueError("Cannot get max from empty dictionary")
        return max(self.data.values())