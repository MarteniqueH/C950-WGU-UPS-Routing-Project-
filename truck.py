from datetime import datetime
from hash_table import HashTable

package_table = HashTable()

class Truck:

    def __init__(self,starting_time, max_load_capacity = 16, speed =18):
        self.packages = []
        self.starting_time = starting_time
        self.total_mileage = 0.0
        self.speed = speed
        self.max_load_capacity = max_load_capacity
        self.current_time = starting_time
        self.current_location = 0


    def load_package(self,package):
        """ Package an object load on to the truck"""
        if len(self.packages) < self.max_load_capacity:
            self.packages.append(package)
        else:
            print("The truck is full")

#Creating the three delivery trucks
truck_one = Truck(starting_time=datetime.strptime("08:00","%H:%M" ))
truck_two = Truck(starting_time=datetime.strptime("09:05","%H:%M" ))
truck_three = Truck(starting_time=datetime.strptime("10:00","%H:%M" ))

#Manually loading each truck with packages based on package IDs
Truck_one_packages = [1,2,4,5,7,8,9,10,11,13,29,30,31,34,37,40]
Truck_two_packages = [3,15,17,18,19,20,21,22,23,24,26,27,33,35,36,38]
Truck_three_packages = [6,12,14,16,25,28,32,39]




#Loading packages by the lookup function of the Hash table
for package_id in Truck_one_packages:
    truck_one.load_package(package_table.lookup(package_id))
for package_id in Truck_two_packages:
    truck_two.load_package(package_table.lookup(package_id))
for package_id in Truck_three_packages:
    truck_three.load_package(package_table.lookup(package_id))