from taxi import Taxi

new_taxi = Taxi("Prius 1", 100)
# print(new_taxi)

new_taxi.drive(40)
print(new_taxi)
print(new_taxi.get_fare())

new_taxi.start_fare()
new_taxi.drive(100)
print(new_taxi)
print(new_taxi.get_fare())