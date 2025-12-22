# Double hashing is the best open-addressing strategy

# instead of 1 hash function we use 2 hash functions, hence it eliminates both the primary and secondary clustering

# probe formula is index = (h1(key) + i*(h2(key)))%capacity

# hash functions are h1(key) = key% clustering, h2(key) = 1+ (key%(capacity-1))

# h2(key) should never be 0 and capacity should be prime no. for all slots reachability


class hashNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value


class Hashmap:
    def __init__(self):
        self.capacity = 23
        self.size = 0
        self.dummy = hashNode(None,None)
        self.arr = [None]*self.capacity

    def h1(self,key):
        return key%self.capacity
    
    def h2(self,key):
        return 1+ (key%(self.capacity-1))
    
    def loadFactor(self):
        return self.size / self.capacity
    

    def insert(self,key,value):
        if self.loadFactor() >= 0.6:
            self.rehash()

        index1 = self.h1(key)
        index2 = self.h2(key)

        i = 0
        while i<self.capacity:
            idx = (index1 + i*(index2))%self.capacity

            if self.arr[idx] is None or self.arr[idx] is self.dummy:
                self.arr[idx] = hashNode(key,value)
                self.size += 1
                return
            
            if self.arr[idx].key == key:
                self.arr[idx].value = value
                return
            
            i += 1

    def get(self,key):
        index1 = self.h1(key)
        index2 = self.h2(key)

        i = 0

        while i<self.capacity:
            idx = (index1 + i * index2) % self.capacity

            if self.arr[idx] is None:
                return -1

            if self.arr[idx] is not self.dummy and self.arr[idx].key == key:
                return self.arr[idx].value

            i += 1

        return -1
    

    def delete(self,key):
        index1 = self.h1(key)
        index2 = self.h2(key)

        i = 0
        while i < self.capacity:
            idx = (index1 + i * index2) % self.capacity

            if self.arr[idx] is None:
                return -1

            if self.arr[idx] is not self.dummy and self.arr[idx].key == key:
                val = self.arr[idx].value
                self.arr[idx] = self.dummy
                self.size -= 1
                return val

            i += 1

        return -1
    
    def rehash(self):
        old_arr = self.arr
        self.capacity = self.capacity * 2 + 1  # keep prime-ish
        self.arr = [None] * self.capacity
        self.size = 0

        for node in old_arr:
            if node is not None and node is not self.dummy:
                self.insert(node.key, node.value)

    def display(self):
        for node in self.arr:
            if node is not None and node is not self.dummy:
                print(node.key, node.value)


def test_double_hashmap():
    hm = Hashmap()

    # 1. Basic insert/get
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

    # 2. Update
    hm.insert(20, 999)
    hm.display()
    print()
    assert hm.get(20) == 999
    assert hm.size == 3

    # 3. Force same h1 but different h2
    base = hm.capacity
    k1 = 7
    k2 = 7 + base
    k3 = 7 + 2 * base

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

    # 4. Delete and dummy reuse
    assert hm.delete(k2) == 222
    assert hm.get(k2) == -1

    hm.insert(k2, 444)
    hm.display()
    print()
    assert hm.get(k2) == 444

    # 5. Rehash
    old_capacity = hm.capacity
    for i in range(300):
        hm.insert(i + 1000, i)
    
    hm.display()
    print()

    assert hm.capacity > old_capacity

    # 6. Validate after rehash
    assert hm.get(10) == 100
    assert hm.get(20) == 999
    assert hm.get(30) == 444
    assert hm.get(k1) == 111
    assert hm.get(k2) == 444
    assert hm.get(k3) == 333

    for i in range(300):
        assert hm.get(i + 1000) == i

    print("ALL DOUBLE HASHING TESTS PASSED")


test_double_hashmap()