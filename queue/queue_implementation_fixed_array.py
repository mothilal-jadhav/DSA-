# in this implementations we maintain a fixed array to store elements, a variable size to track current no. of elements in the queue, and a variable capacity to represent the maximum no of elements our queue can hold

class myQueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0]*capacity

    def isFull(self):
        return self.size == self.capacity
        
    # enqueue will check if the queue reached its capacity or not by checking its size, it size == capacity then Queue overflow

    def enqueue(self,x):
        if self.isFull():
            print('queue overflow')
            return -1
        
        self.arr[self.size] = x
        self.size += 1
    
    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
        # checks if queue is empty or not, if empty then it causes underflow else removes the first element and size is decremented
        if self.isEmpty():
            print('queue underflow')
            return -1
        
        val = self.arr[0]
        # since removing elements will force elements to shift, it will take around O(n) time for this operation

        for i in range(1,self.size):
            self.arr[i-1] = self.arr[i]

        self.size -= 1
        return val
    
    def peek(self):
        # if stack is empty then it returns there is no element to peek else it will give the first element value
        if self.isEmpty():
            print('there is no element to peek')
            return 
        return self.arr[0]
    
    def getRear(self):
        if self.isEmpty():
            print('queue is empty')
            return
        
        return self.arr[self.size-1]
    

    def __str__(self):
        return str(self.arr[:self.size])
    
q = myQueue(8)
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
print(q.isFull())
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
print(q.peek())
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
# queue overflow
# [5, 7, 9, 11, 13, 15, 17, 19]
# True
# [7, 9, 11, 13, 15, 17, 19]
# [9, 11, 13, 15, 17, 19]
# [11, 13, 15, 17, 19]
# [13, 15, 17, 19]
# [13, 15, 17, 19, 21]
# 5
# 13
# 21