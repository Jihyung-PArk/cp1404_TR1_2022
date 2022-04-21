from unreliable_car import UnreliableCar

car_1 = UnreliableCar("Car 1", 100, 80)
car_2 = UnreliableCar("Car 2", 100, 10)

print(car_1)
print(car_2)

for i in range(1, 10):
    print("Drive {}km".format(i))
    print("{} drove {}km".format(car_1.name, car_1.drive(i)))
    print("{} drove {}km".format(car_2.name, car_2.drive(i)))

print(car_1)
print(car_2)