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
    
    def insert(self,key,value):

        hashIndex = self.hashFun(key)
        start = hashIndex

        while self.arr[hashIndex] is not None and \
                self.arr[hashIndex].key is not self.dummy and \
                self.arr[hashIndex].key != key:
            hashIndex = (hashIndex+1)%self.capacity
            if hashIndex == start:
                return

        if self.arr[hashIndex] is None or self.arr[hashIndex].key is self.dummy:
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
    
    def sizeCount(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def display(self):
        for node in self.arr:
            if node is not None and node.key != -1:
                print(f"{node.key} {node.value}")


