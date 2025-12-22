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


def test_hashmap():
    hm = Hashmap()

    # 1. Basic insert + get
    hm.insert(1, 100)
    hm.display()
    print()
    hm.insert(2, 200)
    hm.display()
    print()
    hm.insert(3, 300)
    hm.display()
    print()

    assert hm.get(1) == 100
    assert hm.get(2) == 200
    assert hm.get(3) == 300

    # 2. Update existing key
    hm.insert(2, 999)
    hm.display()
    print()
    assert hm.get(2) == 999
    assert hm.size == 3

    # 3. Force collisions (same hash index)

    k1 = 1
    k2 = 1 + hm.capacity
    k3 = 1 + 2 * hm.capacity

    hm.insert(k2, 400)
    hm.insert(k3, 500)

    assert hm.get(k2) == 400
    assert hm.get(k3) == 500

    # 4. Delete and ensure dummy slot reuse
    assert hm.delete(2) == 999
    assert hm.get(2) == -1
    assert hm.size == 4

    hm.insert(2, 222)
    hm.display()
    print()
    assert hm.get(2) == 222
    assert hm.size == 5

    # 5. Delete non-existing key
    assert hm.delete(9999) == -1

    # 6. Trigger rehash
    old_capacity = hm.capacity
    print("Before bulk insert")
    hm.display()
    print()
    for i in range(100):
        hm.insert(i + 1000, i)

    print("After bulk insert")
    hm.display()
    print()

    assert hm.capacity > old_capacity

    # 7. Validate all values after rehash
    assert hm.get(1) == 100
    assert hm.get(2) == 222
    assert hm.get(3) == 300
    assert hm.get(k2) == 400
    assert hm.get(k3) == 500

    for i in range(100):
        assert hm.get(i + 1000) == i

    # 8. Edge case: get from empty slot
    assert hm.get(-123) == -1

    print("ALL TEST CASES PASSED")

test_hashmap()