# lets implement stacks using linked list 

# lets first implement linked list node so that we can use them in the stack implementation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# after constructing the node structure lets implement them in stack

class myStack:
    def __init__(self):
        self.top = None # here top will be none in the intial stage and for insertion top will be assigned for that
        self.count = 0

    def push(self,x):
        # unlike array implementation there is no fixed capacity in this case so no chance for overflow, so every push will will add a new node and new node current pointer will set as top
        temp = Node(x)
        temp.next = self.top
        self.top = temp
        self.count += 1

    def pop(self):
        # removes the top element from the top, if top is empty then it causes underflow

        if self.top == None:
            print('stack underflow')
            return -1
        
        temp = self.top
        self.top = self.top.next
        val = temp.data
        self.count -= 1

        del temp
        return val
    
    
    def peek(self):
        if self.top is None:
            print('stack is empty')
            return -1
        
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
    def size(self):
        return self.count
    
    def __str__(self):
        result = []
        curr = self.top
        while curr:
            result.append(curr.data)
            curr = curr.next
        return str(result)
    

st = myStack()
st.push(3)
print(st)
st.push(4)
print(st)
st.push(5)
print(st)
st.push(3)
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)
print(st.isEmpty())
print(st.pop())
st.push(8)
print(st)
st.push(2)
print(st)
st.push(4)
print(st)
st.push(1)
print(st)
st.push(7)
print(st)
st.push(6)
print(st)
print(st.peek())
print(st.size())

# the output are:
# [3]
# [4, 3]
# [5, 4, 3]
# [3, 5, 4, 3]
# 3
# [5, 4, 3]
# 5
# [4, 3]
# 4
# [3]
# 3
# []
# True
# stack underflow
# -1
# [8]
# [2, 8]
# [4, 2, 8]
# [1, 4, 2, 8]
# [7, 1, 4, 2, 8]
# [6, 7, 1, 4, 2, 8]
# 6
# 6