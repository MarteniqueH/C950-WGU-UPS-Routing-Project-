from datetime import timedelta
from helper import distance_between


def greedy_algorithm(truck,distance_data,address_data):
    truck.current_location = address_data[0][1]
    while truck.packages:
        urgent_packages = []
        non_urgent_packages = []

        for packages in truck.packages:
            if packages.package_delivery_deadline != "EOD":
                urgent_packages.append(packages)
            else:
                non_urgent_packages.append(packages)
        next_package_delivery = None
        closest_distance = float('inf')

        package_consideration = urgent_packages if urgent_packages else non_urgent_packages
        current_address_index = -1
        for i, row in enumerate(address_data):
            if row [1] == truck.current_location:
                current_address_index = i
                break
        for package in package_consideration:
            package_address = package.package_address
            package_address_index = -1
            for i, row in enumerate (address_data):
                if row[1] == package_address:
                    package_address_index = i
                    break
            if current_address_index != -1 and package_address_index != -1 :
                distance = distance_between(current_address_index,package_address_index)
                if distance < closest_distance:
                    closest_distance = distance
                    next_package_delivery = package

        if next_package_delivery:
            distance_to_next_package = closest_distance
            truck.total_mileage += distance_to_next_package
            travel_time = timedelta(hours = distance_to_next_package / truck.speed)
            truck.current_time += travel_time
            truck.current_location = next_package_delivery.package_address
            next_package_delivery.package_status = f" The package was delivered at {truck.current_time.strftime('%H:%M')}"
            next_package_delivery.package_delivery = truck.current_time
            truck.packages.remove(next_package_delivery)
            print(f"Delivered package at {truck.current_time.strftime('%H:%M')}:")
            print(next_package_delivery)
            print("-" * 40)

    current_address_index = -1
    for i, row in enumerate(address_data):
        if row[1] == truck.current_location:
            current_address_index = i
        break
    hub_address_index = 0
    if current_address_index != -1:
            distance_back_to_hub = distance_between(current_address_index, hub_address_index)
            truck.total_mileage += distance_back_to_hub
            travel_time_back_to_hub = timedelta(hours = distance_back_to_hub / truck.speed)
            truck.current_time += travel_time_back_to_hub
            truck.current_location = address_data[hub_address_index][1]
            print(f"The truck returned back to the hub at {truck.current_time.strftime('%H:%M')}")
            print(f"Total mileage for truck: {truck.total_mileage:.2f} miles")
            print(f"Packages remaining on truck: {len(truck.packages)}")
