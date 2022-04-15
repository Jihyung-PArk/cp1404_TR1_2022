from sliver_service_taxi import SliverServiceTaxi

sliver_taxi_1 = SliverServiceTaxi("Hummer", 200, 2)
print(sliver_taxi_1)

sliver_taxi_1.drive(18)
print(sliver_taxi_1)
print(sliver_taxi_1.get_fare())