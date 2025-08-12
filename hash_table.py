#Created Hash table structure
class HashTable:
    def __init__(self):
        self.size = 50
        self.bucket = [None] * self.size
#Created hash Function
    def hash(self,key):
        return key % self.size
#Created Insert Function
    def insert(self,key,value):
        #Determines which bucket to use
        index = self.hash(key)
        #If the bucket located is empty
        if self.bucket[index] is None:
            self.bucket[index] = [(key, value)]
            return
        #If the bucket located is NOT empty. A collision has occurred
        for i, (package_id, package_info) in enumerate(self.bucket[index]):
            #IF the key already exist: Update the values
            if package_id == key:
                self.bucket[index][i] = (key,value)
                return
        self.bucket[index].append((key,value))
    #Creating Look up function
    def lookup(self, key):
        #Determinse the index for the key using that hash function
        index = self.hash(key)
        #If the bucket is located and has nothing in it
        if self.bucket[index] is None:
            return  "Package Cannot Be Located"
        #The program will loop through all the key-value pairs. If it finds a match, return the associated values
        for package_id, package_info in self.bucket[index]:
            if package_id == key:
                return package_info
        return "Package Cannot be Located"

    def search (self,key):
        return self.lookup(key)
