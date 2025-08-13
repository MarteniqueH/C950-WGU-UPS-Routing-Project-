from datetime import  datetime

class Truck:

    def __init__(self,starting_time, max_load_capacity = 16, speed =18):
        self.packages = []
        self.starting_time = starting_time
        self.total_mileage = 0.0
        self.speed = speed
        self.max_load_capacity = max_load_capacity
        self.current_time = starting_time
        self.current_location = None


    def load_package(self,package):
        if len(self.packages) < self.max_load_capacity:
            self.packages.append(package)
            package.package_departure = self.current_time
        else:
            print("The truck is full")

