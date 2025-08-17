#Student ID: 011509876
#Martenique Harmon
#Library imports for handling csv files and modules
import csv
from datetime import datetime, timedelta
#Classes and functions for a delivery system
from hash_table import HashTable
from package import Package
from routing import greedy_algorithm
from truck import Truck
import logging


#Loading in distance data from the distance file
with open("distance.csv") as distance_file:
    distance_CSV = list(csv.reader(distance_file))[1:]

# Loading in address data from the address file
with open("Addresses.csv") as address_file:
    address_csv = list(csv.reader(address_file))


#Loading the data from the CSV files into the hash table data structure
def loading_packages():
#Created a hash table to store the package object in
    package_table = HashTable()
#Opens and reads the package CSV file
    with open("Package.csv") as package_file:
        package_data = csv.reader(package_file)
        next (package_data)
        for row in package_data:
            if len (row) < 7:
                print(f"Skipping problem rows: {row}")
                continue
            try:
                #Taking the package information form the CSV rows
                package_id = int(row[0])
                package_address = row[1]
                package_city = row[2]
                package_state = row[3]
                package_zip = row[4]
                package_delivery_deadline = row[5]
                package_weight = row[6]
                package_note = row[7] if len(row) > 7 else ""
                package_status = "At Hub"
                #Creates a package object with the information taken from the CSV rows
                package_object = Package(package_id,package_address,package_city,package_state,package_zip,package_delivery_deadline,package_weight,package_note,package_status)
                #Inserts the package object into the hash table with the package ID
                package_table.insert(package_id, package_object)
            except Exception as e:
                print(f"Failed to process row {row}: {e}")

    return package_table



def main():
    #Configuration for logging to track delivery activity
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    #Loading all packages into the hash table
    package_table = loading_packages()


    # Creating the three delivery trucks and setting each trucks start time
    truck_one = Truck(1,datetime.strptime("08:00", "%H:%M"))
    truck_two = Truck(2,datetime.strptime("09:05", "%H:%M"))
    truck_three = Truck(3,datetime.strptime("10:00", "%H:%M"))

    # Loading packages by the lookup function of the Hash table
    #loading packages for truck one
    truck_one_packages = [1, 2, 7, 10, 11, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37]
    for package_id in truck_one_packages:
        package = package_table.lookup(package_id)
        if package:
            truck_one.load_package(package)
            print(f"Package Id {package_id} loaded onto Truck one")
    #loading packages for truck two
    truck_two_packages = [6, 4, 3, 17, 18, 21, 22, 23, 24, 26, 27, 33, 35, 36, 38, 40]
    for package_id in truck_two_packages:
        package = package_table.lookup(package_id)

        if  package:
            truck_two.load_package(package)
            print(f"Package Id {package_id} loaded onto Truck Two")
    #loading packages for truck three
    truck_three_packages = [8, 5, 9, 12, 25, 28, 32, 39]
    for package_id in truck_three_packages:
        package = package_table.lookup(package_id)
        if package :
            truck_three.load_package(package)
            print(f"Package Id {package_id} loaded onto Truck Three.")

    #Run delivery routes using the greedy algorithm for each truck
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
#Calcuate the total mileage for all trucks combined
    total_mileage = (
        truck_one.total_mileage +
        truck_two.total_mileage +
        truck_three.total_mileage
    )
    print(f"The total mileage for all trucks: {total_mileage:.2F}")
    return truck_one,truck_two,truck_three, package_table
# Determines the status of a package at a specific time
def get_package_status(package,query_time):
    if package.package_delivery is None or query_time < package.package_departure:
        #Alterd print statement to align with delayed packages on fight
        return 'The package is still under processing and has not yet begun transit to the destinitation address'
    elif package.package_departure <= query_time < package.package_delivery:
        return "The package is En route to drop off address"
    else:
        return f"The package was delivered at {package.package_delivery.strftime('%H:%M')} "
#UI menu for querying package status and system information
def print_package_info(package,query_time):
    status = get_package_status(package, query_time)
    full_address = f"{package.package_address},{package.package_city},{package.package_state},{package.package_zip}"
    print(f"Package Id: {package.package_id}")
    print(f"Delivery Address: {full_address}")
    print(f"Delivery Deadline: {package.package_delivery_deadline}")
    print(f"Delivery Status: {status}")
    print(f"Truck Number: {package.truck_number or 'Truck number unavailable at this time'}")
    print("-" * 50)

def selection_menu(package_table, trucks):
    truck_one, truck_two, truck_three = trucks
    while True:
        #Menu selection options
        print("WGU UPS Delivery Program")
        print("1. See status of specific package")
        print("2. See status of ALL packages")
        print("3. View the total mileage of all trucks combined")
        print("4. Exit Menu")
        choice = input("Select a number option: ")
        #Choice #1 Checks the status of one package at a specific time
        if choice == "1":
            try:
                package_id = int(input("Enter the package ID: "))
                time_str = input("Enter time (HH:MM): ")
                query_time = datetime.strptime(time_str, "%H:%M")
                package = package_table.lookup(package_id)
                if package:
                   print_package_info(package, query_time)
                else:
                    print(f"Package {package_id} cannot be located")
            except ValueError:
                print("Invalid Input. Please Try again")
        #Choice #2 Checks the status of ALL packages at a specific time
        elif choice == "2":
            try:
                time_str = input("Enter time (HH:MM): ")
                query_time = datetime.strptime(time_str, "%H:%M")
                for i in range (1,41):
                    package = package_table.lookup(i)
                    if package:
                      print_package_info(package, query_time)
                    else:
                        print(f"Package {i} cannot be located")
            except ValueError:
                print("Invalid Time format. Please use the following format HH:MM")
       #Option #3 Displays the TOTAL Mileage for all trucks
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
    #Runs the main function to run deliveries and gets the system objects
    truck_one,truck_two,truck_three,package_table = main()
    #Runs selection menu
    selection_menu(package_table,(truck_one,truck_two,truck_three))
