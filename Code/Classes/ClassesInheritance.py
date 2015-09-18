class Animals:
        
    def eat(self):
        print('eat')
        
    def talk(self):
        print('talk')
        
class Cat(Animals):
    def talk(self):
        print('Meows')
        
    def move(self):
        print('jump')
        
class Dog(Animals):
    def talk(self):
        print('won')
        

muffin = Cat()
muffin.talk()
muffin.eat()
muffin.move()

tom = Dog()
tom.talk()
tom.eat()


    