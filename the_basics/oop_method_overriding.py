class Animal:
    def eat(self): # the name of the method and its parameters are called "method's signature"
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")
        
rabbit = Rabbit()
rabbit.eat() # This rabbit is eating a carrot