from object_oriented_programming.car import Car

car_1 = Car("Toyota", "Corolla", 1994, "black")

print(car_1) # <object_oriented_programming.car.Car object at 0x000001943D6BF710>
print(car_1.make) # Toyota
print(car_1.model) # Corolla
print(car_1.year) # 1994
print(car_1.color) # black

car_1.drive() # This Corolla is driving
car_1.stop() # This Corolla is stopped