class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def my_self(self):
        return f'Hi my name is {self.name}, I am {self.age} years old and I am a {self.gender}'

person = Person('Phumulani',10,'male')
print(person.my_self())