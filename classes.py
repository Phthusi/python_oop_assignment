class Animal:
    def __init__(self, name,body_covering):
        self.name = name
        self.body_covering = body_covering
    
    def move_around(self,movement):
        print(f'{self.name} is {movement}')
    
    def make_sound(self, sound):
        return sound


class Human(Animal):
    def __init__(self, name,secret):
        super().__init__(name,'skin')
        self.__secret = secret
    
    def tell_my_secret(self):
        print(self.__secret)

    def make_sound(self):
        print(super().make_sound(self.name+' is talking'))

    def move_around(self, movement):
        return super().move_around(movement)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'fur')

    def make_sound(self):
        print(super().make_sound(self.name+' says woof woof'))

    def wag_tail(self):
        print(f"{self.name} is wagging its tail happily!")

person = Human('dave','xyz')
barky = Dog('barky')

#person.__secret this doesn't work because this attribute is private
person.tell_my_secret()

for animal in [person,barky]:
    animal.make_sound()
