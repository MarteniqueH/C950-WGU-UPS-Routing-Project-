#Student ID: 011509876
#Martenique Harmon
import csv
from datetime import datetime, timedelta

from hash_table import HashTable
from package import Package
from routing import greedy_algorithm
from truck import Truck
import logging


#Importing a Distance CSV file
with open("distance.csv") as distance_file:
    distance_CSV = list(csv.reader(distance_file))[1:]

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
            if len (row) < 7:
                print(f"Skipping malformed row: {row}")
                continue
            try:
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
            except Exception as e:
                print(f"Failed to process row {row}: {e}")

    return package_table



def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    package_table = loading_packages()


    # Creating the three delivery trucks
    truck_one = Truck(starting_time=datetime.strptime("08:00", "%H:%M"))
    truck_two = Truck(starting_time=datetime.strptime("09:05", "%H:%M"))
    truck_three = Truck(starting_time=datetime.strptime("10:00", "%H:%M"))

    # Manually loading each truck with packages based on package IDs
    truck_one_packages = [1,2,7,10,11,13,14,15,16,19,20,29,30,31,34,37]
    truck_two_packages = [4,3,8,17,18,21,22,23,24,26,27,33,35,36,38,40]
    truck_three_packages = [6,5,9,12,25,28,32,39]

    # Loading packages by the lookup function of the Hash table
    for package_id in truck_one_packages:
        package = package_table.lookup(package_id)
        if package is None:
            print(f"Package ID {package_id} is not found in hash table.")
        else:
            truck_one.load_package(package)
            print(f"Package Id {package_id} loaded onto Truck one")
    for package_id in truck_two_packages:
        package = package_table.lookup(package_id)
        if package is None:
            print(f"Package ID {package_id} is not found in hash table.")
        else:
            truck_two.load_package(package)
            print(f"Package Id {package_id} loaded onto Truck Two")
    for package_id in truck_three_packages:
        package = package_table.lookup(package_id)
        if package is None:
            print(f"Package ID {package_id} is not found in hash table.")
        else:
            truck_three.load_package(package)
            print(f"Package Id {package_id} loaded onto Truck Three.")

    print("Deliveries for Truck one have begun")
    try:
        greedy_algorithm(truck_one, distance_CSV, address_csv)
    except Exception as e:
        print(f"Truck One delivery failed: {e}")

    print("Deliveries for Truck two have begun")
    try:
        greedy_algorithm(truck_two, distance_CSV, address_csv)
    except Exception as e:
        print(f"Truck Two delivery failed: {e}")

    print("Deliveries for Truck three have begun")
    try:
        greedy_algorithm(truck_three, distance_CSV, address_csv)
    except Exception as e:
        print(f"Truck Three delivery failed: {e}")
    print("All packages are Done")

    total_mileage = (
        truck_one.total_mileage +
        truck_two.total_mileage +
        truck_three.total_mileage
    )
    print(f"The total mileage for all trucks: {total_mileage:.2F}")
    return truck_one,truck_two,truck_three, package_table
    return truck_one,truck_two,truck_three, package_table
def get_package_status(package,query_time):
    if package.package_delivery is None or query_time < package.package_departure:
        return("The package is at the HUB")
    elif package.package_departure <= query_time < package.package_delivery:
        return "The package is En route to drop off address"
    else:
        return f"The package was delivered at {package.package_delivery.strftime('%H:%M')} "
def selection_menu(package_table, trucks):
    truck_one, truck_two, truck_three = trucks
    while True:
        print("WGU UPS Delivery Program")
        print("1. See status of specific package")
        print("2. See status of ALL packages")
        print("3. View the total mileage of all trucks combined")
        print("4. Exit Menu")
        choice = input("Select a number option: ")
        if choice == "1":
            try:
                package_id = int(input("Enter the package ID: "))
                time_str = input("Enter time (HH:MM): ")
                query_time = datetime.strptime(time_str, "%H:%M")
                package = package_table.lookup(package_id)
                if package:
                    status = get_package_status(package,query_time)
                    print(f"Package {package_id} status at {time_str}: {status}")
                else:
                    print(f"Package {package_id} cannot be located")
            except ValueError:
                print("Invalid Input. Please Try again")
        elif choice == "2":
            try:
                time_str = input("Enter time (HH:MM): ")
                query_time = datetime.strptime(time_str, "%H:%M")
                for i in range (1,41):
                    package = package_table.lookup(i)
                    if package:
                        status = get_package_status(package, query_time)
                        print(f"Package {i}: {status}")
                    else:
                        print(f"Package {i} cannot be located")
            except ValueError:
                print("Invalid Time format. Please use the following format HH:MM")
        elif choice == "3":
            total_mileage = (
                truck_one.total_mileage +
                truck_two.total_mileage +
                truck_three.total_mileage
            )
            print(f"Total mileage for all trucks: {total_mileage: .2f} miles ")
        elif choice == "4":
            print("Exiting selection menu")
            break
        else:
            print("Invalid selection, Please Try again")
if __name__ == "__main__":

    truck_one,truck_two,truck_three,package_table = main()
    selection_menu(package_table,(truck_one,truck_two,truck_three))
