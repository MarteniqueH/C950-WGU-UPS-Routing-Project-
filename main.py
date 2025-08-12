#Student ID: 011509876
#Martenique Harmon


import csv
from turtledemo.nim import HUNIT

from package import  Package


from hash_table import  HashTable

#Importing a Distance CSV file
with open("distance.csv") as distance_file:
    distance_CSV =csv.reader(distance_file)
    distance_CSV = list(distance_CSV)
print(distance_CSV)
#Importing a package CSV file
with open("Package.csv") as package_file:
    package_CSV =csv.reader(package_file)
    package_CSV = list(package_file)

#Importing an Address CSV file
with open("Addresses.csv") as address_file:
    address_file =csv.reader(address_file)
    address_file = list(address_file)



#Function that determines the distance between two addresses
def distance_between(Address_one, Address_two):
    distances = distance_CSV[Address_one][Address_two]
    if distances =="":
        distances = distance_CSV[Address_two][Address_one]
    return float(distances)

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
            package_note = row[7]
            package_status = "At Hub"

            package_object = Package(package_id,package_address,package_city,package_state,package_zip,package_delivery_deadline,package_weight,package_note,package_status)

            package_table.insert(package_id, package_object)

    return package_table

