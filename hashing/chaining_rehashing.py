# rehashing can be done to increase the no of slots for the table, typically when the load factoe is greater than 0.5

# in rehashing we double the size of array when lf is >0.5, and even hash function will be changed

class Hash:
    def __init__(self,slots):
        self.slots = slots
        self.no_of_elements = 0
        self.table = [[] for _ in range(self.slots)]

    def load_factor(self):
        return self.no_of_elements/self.slots
    
    def rehash(self):
        old = self.table
        self.slots *= 2
        self.table = [[] for _ in range(self.slots)]
        self.no_of_elements = 0

        for slot in old:
            for key in slot:
                self.insert(key)


    def hash_index(self,key):
        return key % self.slots
    
    def insert(self,key):
        index = self.hash_index(key)
        if key in self.table[index]:
            return

        self.table[index].append(key)
        self.no_of_elements += 1

        if self.load_factor() > 0.5:
            self.rehash()

    def remove(self,key):
        index = self.hash_index(key)

        if key in self.table[index]:
            self.table[index].remove(key)
            self.no_of_elements -= 1


    def display(self):
        for i in range(self.slots):
            print(i, end="")
            for key in self.table[i]:
                print(f" --> {key}", end="")
            print()


# h = Hash(7)
# h.insert(1)
# h.insert(2)
# h.insert(3)
# h.display()
# the outputs are:
# 0
# 1 --> 1
# 2 --> 2
# 3 --> 3
# 4
# 5
# 6

# h = Hash(7)
# keys = [15, 11, 27, 8]   # all collide at indices 1 and 6
# for k in keys:
#     h.insert(k)
# h.display()
# the outputs are:
# 0
# 1 --> 15
# 2
# 3
# 4
# 5
# 6
# 7
# 8 --> 8
# 9
# 10
# 11 --> 11
# 12
# 13 --> 27

# h = Hash(4)

# for k in [1, 2, 3]:
#     h.insert(k)
# print("Slots after rehash:", h.slots)
# h.display()
# the outputs are:
# Slots after rehash: 8
# 0
# 1 --> 1
# 2 --> 2
# 3 --> 3
# 4
# 5
# 6
# 7

h = Hash(2)

for i in range(20):
    h.insert(i)

print("Final slots:", h.slots)
print("Final load factor:", h.load_factor())

# Final slots: 64
# Final load factor: 0.3125