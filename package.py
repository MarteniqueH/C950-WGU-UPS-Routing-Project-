class Package:
    def __init__(self,package_id,package_address,package_city,package_state,package_zip,package_delivery_deadline,package_weight, package_note, package_status):
        self.package_id = package_id
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = package_zip
        self.package_delivery_deadline = package_delivery_deadline
        self.package_weight = package_weight
        self.package_note = package_note
        self.package_status = package_status
        self.package_delivery = None

    def __str__(self):
        details = [
            f"Package {self.package_id}: ",
            f"{self.package_address} ",
            f"{self.package_city} ",
            f"{self.package_state} {self.package_zip} ",
            f"Deadline: {self.package_delivery_deadline} ",
            f"Weight {self.package_weight} kg ",
            f"Status: {self.package_status}"

        ]
        return "".join(details)