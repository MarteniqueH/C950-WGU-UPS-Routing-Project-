
def distance_between(Address_one, Address_two, distance_data):
    try:
        distances = distance_data[Address_one][Address_two].strip()
        if distances == "":
            distances = distance_data[Address_two][Address_one].strip()
        return float(distances)
    except (IndexError, ValueError) as e:
        print(f"Error getting distance between {Address_one} and {Address_two}: {e}")
        return 0.0