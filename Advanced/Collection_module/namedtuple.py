# Python code to demonstrate namedtuple() and 
# _make(), _asdict()
  

from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 

# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name)

# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li)) 
  
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict()) 

# Output:
# The namedtuple instance using iterable is  : 
# Student(name='Manjeet', age='19', DOB='411997')
# The OrderedDict instance using namedtuple is  : 
# OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])