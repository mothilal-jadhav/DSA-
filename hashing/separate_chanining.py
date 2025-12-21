# Chain hashing avoids collision. The idea is to make each cell of hash table point to a linked list of records that have same hash function value.


# Let's create a hash function, such that our hash table has 'n' number of slots

# To insert a node into the hash table, we first compute the hash index for the given key using a hash function: hashIndex = key % noOfSlots.

# for example the noOfSlots = 7, keys to be inserted are [15,11,27,8]. for each key the indexes will be 1,4,6,1

class Hash:
    def __init__(self,slots):
        self.slots = slots

        self.table = [[] for _ in range(self.slots)]

    def hash_index(self,key):
        return key%self.slots
    
    def insert(self,key):
        index = self.hash_index(key)

        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self,key):
        index = self.hash_index(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def display(self):
        for i in range(self.slots):
            print(i,end="")

            for key in self.table[i]:
                print(" -->", key, end="")

            print()
    
    def search(self, key):
        index = self.hash_index(key)
        return key in self.table[index]


hash = Hash(7)

keys = [7, 18, 12, 25]

for key in keys:
    hash.insert(key)
    hash.display()
    print()


# the outputs are:
# 0 --> 7
# 1
# 2
# 3
# 4
# 5
# 6

# 0 --> 7
# 1
# 2
# 3
# 4 --> 18
# 5
# 6

# 0 --> 7
# 1
# 2
# 3
# 4 --> 18
# 5 --> 12
# 6

# 0 --> 7
# 1
# 2
# 3
# 4 --> 18 --> 25
# 5 --> 12
# 6