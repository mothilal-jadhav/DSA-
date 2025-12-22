class HashNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class Hashmap:
    def __init__(self):
        self.capacity = 23
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
        i = 0

        while i<self.capacity:
            idx = (hashIndex+ i*i)%self.capacity

            if self.arr[idx] is None or self.arr[idx] is self.dummy:
                self.arr[idx] = HashNode(key,value)
                self.size += 1
                return
            
            if self.arr[idx].key == key:
                self.arr[idx].value = value
                return
            
            i += 1


    def delete(self,key):
        hashIndex = self.hashFun(key)
        i = 0
        while i < self.capacity:
            idx = (hashIndex + i * i) % self.capacity

            if self.arr[idx] is None:
                    return -1
            
            if self.arr[idx] is not self.dummy and self.arr[idx].key == key:
                    val = self.arr[idx].value
                    self.arr[idx] = self.dummy
                    self.size -= 1
                    return val
        
            i+=1
        return -1


    def get(self,key):
        hashIndex = self.hashFun(key)
        i = 0

        while i < self.capacity:
            idx = (hashIndex + i * i) % self.capacity

            if self.arr[idx] is None:
                return -1

            if self.arr[idx] is not self.dummy and self.arr[idx].key == key:
                return self.arr[idx].value

            i += 1

        return -1

    
    def rehash(self):
        old_arr = self.arr

        self.capacity = self.capacity*2 + 1 
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


def test_quadratic_hashmap():
    hm = Hashmap()

    # 1. Basic insert + get
    hm.insert(10, 100)
    hm.display()
    print()
    hm.insert(20, 200)
    hm.display()
    print()
    hm.insert(30, 300)
    hm.display()
    print()

    assert hm.get(10) == 100
    assert hm.get(20) == 200
    assert hm.get(30) == 300

    # 2. Update existing key
    hm.insert(20, 999)
    hm.display()
    print()
    assert hm.get(20) == 999
    assert hm.size == 3

    # 3. Force same hash (secondary clustering test)
    base = hm.capacity
    k1 = 5
    k2 = 5 + base
    k3 = 5 + 2 * base

    hm.insert(k1, 111)
    hm.display()
    print()
    hm.insert(k2, 222)
    hm.display()
    print()
    hm.insert(k3, 333)
    hm.display()
    print()

    assert hm.get(k1) == 111
    assert hm.get(k2) == 222
    assert hm.get(k3) == 333

    # 4. Delete middle key and ensure probing still works
    assert hm.delete(k2) == 222
    assert hm.get(k2) == -1
    assert hm.get(k1) == 111
    assert hm.get(k3) == 333

    # 5. Reinsert into dummy slot
    hm.insert(k2, 444)
    hm.display()
    print()
    assert hm.get(k2) == 444

    # 6. Trigger rehash
    old_capacity = hm.capacity
    for i in range(200):
        hm.insert(i + 1000, i)
    
    hm.display()
    print()

    assert hm.capacity > old_capacity

    # 7. Validate data after rehash
    assert hm.get(10) == 100
    assert hm.get(20) == 999
    assert hm.get(30) == 300

    assert hm.get(k1) == 111
    assert hm.get(k2) == 444
    assert hm.get(k3) == 333

    for i in range(200):
        assert hm.get(i + 1000) == i

    # 8. Non-existing key
    assert hm.get(-999) == -1
    assert hm.delete(-999) == -1

    print("ALL QUADRATIC PROBING TESTS PASSED")

test_quadratic_hashmap()
