#Student ID: 011509876
#Martenique Harmon
import csv
from datetime import datetime

from hash_table import HashTable
from package import Package
from routing import greedy_algorithm
from truck import Truck

#Importing a Distance CSV file
with open("distance.csv") as distance_file:
    distance_CSV = list(csv.reader(distance_file))

#Importing an Address CSV file
with open("Addresses.csv") as address_file:
    address_csv = list(csv.reader(address_file))


#Function for loading packages into hash table
def loading_packages():
    package_table = HashTable()
    with open("Package.csv") as package_file:
        package_data = csv.reader(package_file)
        next (package_data)
        for row in package_data:
            package_id = int(row[0])
            package_address = row[1]
            package_city = row[2]
            package_state = row[3]
            package_zip = row[4]
            package_delivery_deadline = row[5]
            package_weight = row[6]
            package_note = row[7] if len(row) > 7 else ""
            package_status = "At Hub"

            package_object = Package(package_id,package_address,package_city,package_state,package_zip,package_delivery_deadline,package_weight,package_note,package_status)

            package_table.insert(package_id, package_object)

    return package_table

def main():
    package_table = loading_packages()


    # Creating the three delivery trucks
    truck_one = Truck(starting_time=datetime.strptime("08:00", "%H:%M"))
    truck_two = Truck(starting_time=datetime.strptime("09:05", "%H:%M"))
    truck_three = Truck(starting_time=datetime.strptime("10:00", "%H:%M"))

    # Manually loading each truck with packages based on package IDs
    Truck_one_packages = [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 29, 30, 31, 34, 37, 40]
    Truck_two_packages = [3, 15, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 33, 35, 36, 38]
    Truck_three_packages = [6, 12, 14, 16, 25, 28, 32, 39]

    # Loading packages by the lookup function of the Hash table
    for package_id in Truck_one_packages:
        package = package_table.lookup(package_id)
        if isinstance(package,Package):
            truck_one.load_package(package)
        else:
            print(f"Package Id {package_id} is not found")
    for package_id in Truck_two_packages:
        package = package_table.lookup(package_id)
        if isinstance(package,Package):
            truck_two.load_package(package)
        else:
            print(f"Package Id {package_id} is not found")
    for package_id in Truck_three_packages:
        package = package_table.lookup(package_id)
        if isinstance(package,Package):
            truck_three.load_package(package)
        else:
            print(f"Package Id {package_id} is not found")

    print("Deliveries for Truck one have begun")
    greedy_algorithm(truck_one,distance_CSV,address_csv)
    print("Deliveries for Truck two have begun")
    greedy_algorithm(truck_two,distance_CSV,address_csv)
    print("Deliveries for Truck three has begun ")
    greedy_algorithm(truck_three,distance_CSV,address_csv)

if __name__ == "__main__":
    main()

