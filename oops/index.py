"""
The __init__ method, also known as the constructor, is used in Python classes.
 It is called automatically when an object
is created from a class and allows us to initialize the attributes of the object.
"""
"""class Student:
    name = 'Arnab',
    lname= 'Golder',
    skills= ['java', 'python']

s1 = Student()
print(type(s1))"""
class Student:
    def __init__(self,name):
        self.name = name
    @staticmethod
    def enrololId():
         print('your id is E2231289K098')
    def welcome(self):
          print('Welcome to', self.name)


s2 = Student('Arnab')
# print(s2.welcome())
s2.enrololId()