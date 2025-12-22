class HashNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class Hashmap:
    def __init__(self):
        self.capacity = 20
        self.size = 0
        self.arr = [None]*self.capacity
        self.dummy = HashNode(None,None)

    def hashFun(self,key):
        return key%self.capacity
    
    def loadFactor(self):
        return self.size / self.capacity

    
    def insert(self,key,value):

        if self.loadFactor() >= 0.6:
            self.rehash()


        hashIndex = self.hashFun(key)
        start = hashIndex

        while self.arr[hashIndex] is not None and \
                self.arr[hashIndex] is not self.dummy and \
                self.arr[hashIndex].key != key:
            hashIndex = (hashIndex+1)%self.capacity
            if hashIndex == start:
                return

        if self.arr[hashIndex] is None or self.arr[hashIndex] is self.dummy:
            self.size += 1
        self.arr[hashIndex] = HashNode(key, value)


    def delete(self,key):
        hashIndex = self.hashFun(key)
        counter = 0
        while counter < self.capacity and self.arr[hashIndex] is not None:
            if self.arr[hashIndex] is not self.dummy and self.arr[hashIndex].key == key:
                temp = self.arr[hashIndex]
                self.arr[hashIndex] = self.dummy
                self.size -= 1
                return temp.value
            hashIndex = (hashIndex+1)%self.capacity
            counter += 1

        return -1
    

    def get(self,key):
        hashIndex = self.hashFun(key)
        counter = 0

        while counter < self.capacity and self.arr[hashIndex] is not None:
            if self.arr[hashIndex] is not self.dummy and self.arr[hashIndex].key == key:
                temp = self.arr[hashIndex]
                return temp.value
            hashIndex = (hashIndex+1)%self.capacity
            counter += 1

        return -1
    
    def rehash(self):
        old_arr = self.arr
        old_capacity = self.capacity

        self.capacity *= 2
        self.arr = [None] * self.capacity
        self.size = 0

        for node in old_arr:
            if node is not None and node is not self.dummy:
                self.insert(node.key, node.value)

    
    def sizeCount(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def display(self):
        for node in self.arr:
            if node is not None and node.key is not self.dummy:
                print(f"{node.key} {node.value}")


