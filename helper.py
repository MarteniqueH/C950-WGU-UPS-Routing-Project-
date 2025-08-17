#Calcuates the distance between two addresses using distance matrix
def distance_between(Address_one_index, Address_two_index, distance_data):
    try:
        distances = distance_data[Address_one_index][Address_two_index].strip()
        if distances == "":
            distances = distance_data[Address_two_index][Address_one_index].strip()
        return float(distances)
    except (IndexError, ValueError) as e:
        print(f"Error getting distance between {Address_one_index} and {Address_two_index}: {e}")
        return 0.0