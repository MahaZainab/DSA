class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.keys = [None] * size

    def hash_function(self, key):
        # Simple hash function based on the sum of ASCII values of characters
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index

        # Linear probing in case of collision
        while self.table[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")

        self.table[index] = value
        self.keys[index] = key

    def search(self, key):
        index = self.hash_function(key)
        original_index = index

        # Linear probing to find the key
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.table[index]
            index = (index + 1) % self.size
            if index == original_index:
                break

        return None

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index

        # Linear probing to find the key
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.table[index] = None
                self.keys[index] = None
                # Rehash the rest of the cluster
                self._rehash(index)
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break

        return False

    def _rehash(self, start_index):
        index = (start_index + 1) % self.size
        while self.table[index] is not None:
            key_to_rehash = self.keys[index]
            value_to_rehash = self.table[index]
            self.table[index] = None
            self.keys[index] = None
            self.insert(key_to_rehash, value_to_rehash)
            index = (index + 1) % self.size

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: Key = {self.keys[i]}, Value = {self.table[i]}")

# Sample Usage
hash_table = HashTable()

# Inserting airport information
hash_table.insert("MEL", "Melbourne Tullamarine (MEL)")
hash_table.insert("JFK", "John F. Kennedy International Airport")
hash_table.insert("LAX", "Los Angeles International Airport")
hash_table.insert("LHR", "London Heathrow Airport")
hash_table.insert("BKK", "Bangkok Suvarnabhumi Airport")

# Searching for airport information
print("Search for LAX:", hash_table.search("LAX"))
print("Search for JFK:", hash_table.search("JFK"))

# Deleting an airport
print("Deleting LHR:", hash_table.delete("LHR"))
print("Search for LHR after deletion:", hash_table.search("LHR"))

# Display the hash table
hash_table.display()
