from datetime import timedelta
from helper import distance_between

#Implements greedy nearest neighbor algorithm for package delivery routing
def greedy_algorithm(truck,distance_data,address_data):
    truck.current_location = "4001 South 700 East"
    while truck.packages:
        #Seperating the EOD packages from the Packages with a specific time deadline
        urgent_packages = [p for p in truck.packages if p.package_delivery_deadline != "EOD"]
        non_urgent_packages = [p for p in truck.packages if p.package_delivery_deadline == "EOD"]
        package_consideration = urgent_packages if urgent_packages else non_urgent_packages
        current_address_index = next(
            (i for i, row in enumerate(address_data)
             if row[1].strip() == truck.current_location.strip()),
            -1)

        next_package = None
        closest_distance = float('inf')
#finds the nearest package
        for package in package_consideration:
        #finds the address index for the package delivery address
            package_address_index = next(
                (i for i, row in enumerate(address_data)
                 if row[1].strip() == package.package_address.strip()),
                -1)
        #clacuates distance if both addresses are found in the data
            if current_address_index != -1 and package_address_index != -1:
                distance = distance_between(current_address_index, package_address_index, distance_data)
            #updates the closest package if this one is closer
                if distance < closest_distance:
                    closest_distance = distance
                    next_package = package
            #Avoids a bad infinite looping problem
        if not next_package:
            print("No next package was found. The route for this truck ended early to avoid infinite looping")
            break

    #The DELIVERY PROCESS BEGINS

        #Packages Delivery for each truck
        travel_distance = closest_distance
        truck.total_mileage += travel_distance
        travel_time = timedelta(hours=travel_distance / truck.speed)

        truck.current_time += travel_time
        truck.current_location = next_package.package_address
        next_package.package_status = f"Delivered at {truck.current_time.strftime('%H:%M')}"
        next_package.package_delivery = truck.current_time
        truck.packages.remove(next_package)

        print(f"Delivered package at {truck.current_time.strftime('%H:%M')}:")
        print(next_package)
        print("-" * 40)




    # Return the truck to the hub after all the packages have been delivered
    current_address_index = next(
        (i for i, row in enumerate(address_data)
         if row[1].strip()== truck.current_location.strip()),
        -1
    )
    hub_address_index = 0

    if current_address_index != -1:
        distance_to_hub = distance_between(current_address_index, hub_address_index, distance_data)
        truck.total_mileage += distance_to_hub
        return_time = timedelta(hours=distance_to_hub / truck.speed)

        truck.current_time += return_time
        truck.current_location = address_data[hub_address_index][1]


    print(f"The truck returned back to the hub at {truck.current_time.strftime('%H:%M')}")
    print(f"Total mileage for truck: {truck.total_mileage:.2f} miles")
    print(f"Packages remaining on truck: {len(truck.packages)}")
