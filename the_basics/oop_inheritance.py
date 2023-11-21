class Animal: # parent class
    def __init__(self):
        self.alive = True
    
    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")
    
class Rabit(Animal): # child class
    def run(self):
        print("This rabbit is running")

class Fish(Animal): # child class
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal): # child class
    def fly(self):
        print("This hawk is flying")

rabbit = Rabit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
        