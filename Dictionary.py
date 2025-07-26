my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

print (my_vehicle)

for x,y in my_vehicle.items():
    print(x,y)

my_vehicle2= my_vehicle.copy()

my_vehicle2['number_of_tires'] = 4

print(my_vehicle2)

my_vehicle2.pop('mileage')

for x in my_vehicle2:
    print(x)