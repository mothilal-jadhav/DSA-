class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front is None 

    def enqueue(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print('queue underflow')
            return
        
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return temp.data


    def getFront(self):
        if self.isEmpty():
            print('queue is empty')
            return
        
        return self.front.data
    
    def size(self):
        return self.size
    
    def __str__(self):
        result = []

        curr = self.front
        while curr:
            result.append(curr.data)
            curr = curr.next

        return str(result)
    
    def getRear(self):
        if self.isEmpty():
            print('queue is empty')
            return
        
        return self.rear.data
    
q = myQueue()
q.enqueue(5)
print(q)
q.enqueue(7)
print(q)
q.enqueue(9)
print(q)
q.enqueue(11)
print(q)
print(q.isEmpty())
q.enqueue(13)
print(q)
q.enqueue(15)
print(q)
q.enqueue(17)
print(q)
q.enqueue(19)
print(q)
q.enqueue(21)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.enqueue(21)
print(q)
print(q.size)
print(q.getFront())
print(q.getRear())

# the output are:
# [5]
# [5, 7]
# [5, 7, 9]
# [5, 7, 9, 11]
# False
# [5, 7, 9, 11, 13]
# [5, 7, 9, 11, 13, 15]
# [5, 7, 9, 11, 13, 15, 17]
# [5, 7, 9, 11, 13, 15, 17, 19]
# [5, 7, 9, 11, 13, 15, 17, 19, 21]
# [7, 9, 11, 13, 15, 17, 19, 21]
# [9, 11, 13, 15, 17, 19, 21]
# [11, 13, 15, 17, 19, 21]
# [13, 15, 17, 19, 21]
# [13, 15, 17, 19, 21, 21]
# 6
# 13
# 21