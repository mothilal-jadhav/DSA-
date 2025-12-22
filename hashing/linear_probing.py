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

# the outputs are:
# 1 100

# 1 100
# 2 200

# 1 100
# 2 200
# 3 300

# 1 100
# 2 999
# 3 300

# 1 100
# 2 222
# 3 300
# 21 400
# 41 500

# Before bulk insert
# 1 100
# 2 222
# 3 300
# 21 400
# 41 500

# After bulk insert
# 1 100
# 2 222
# 3 300
# 21 400
# 1000 0
# 41 500
# 1001 1
# 1002 2
# 1003 3
# 1004 4
# 1005 5
# 1006 6
# 1007 7
# 1008 8
# 1009 9
# 1010 10
# 1011 11
# 1012 12
# 1013 13
# 1014 14
# 1015 15
# 1016 16
# 1017 17
# 1018 18
# 1019 19
# 1020 20
# 1021 21
# 1022 22
# 1023 23
# 1024 24
# 1025 25
# 1026 26
# 1027 27
# 1028 28
# 1029 29
# 1030 30
# 1031 31
# 1032 32
# 1033 33
# 1034 34
# 1035 35
# 1036 36
# 1037 37
# 1039 39
# 1040 40
# 1041 41
# 1042 42
# 1038 38
# 1043 43
# 1044 44
# 1045 45
# 1046 46
# 1047 47
# 1048 48
# 1049 49
# 1050 50
# 1051 51
# 1052 52
# 1053 53
# 1054 54
# 1055 55
# 1056 56
# 1057 57
# 1058 58
# 1059 59
# 1060 60
# 1061 61
# 1062 62
# 1063 63
# 1064 64
# 1065 65
# 1066 66
# 1067 67
# 1068 68
# 1069 69
# 1070 70
# 1071 71
# 1072 72
# 1073 73
# 1074 74
# 1075 75
# 1076 76
# 1077 77
# 1078 78
# 1079 79
# 1080 80
# 1081 81
# 1082 82
# 1083 83
# 1084 84
# 1085 85
# 1086 86
# 1087 87
# 1088 88
# 1089 89
# 1090 90
# 1091 91
# 1092 92
# 1093 93
# 1094 94
# 1095 95
# 1096 96
# 1097 97
# 1098 98
# 1099 99
