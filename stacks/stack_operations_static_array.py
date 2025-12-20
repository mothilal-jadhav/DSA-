class myStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.arr = [0]*capacity
        self.top = -1
    
# push operation on stack

# in fixed size stack if stack is full then upon adding an element it overflows so for this we will have to check if stack is full 
# is stack is full (top == capacity-1) then stack overflows and we cannot add another element otherwise we increment top by 1 and new value is inserted at top

    def push(self,x):
        if self.top == self.capacity -1:
            print('stack overflow')
            return
        
        self.top += 1
        self.arr[self.top] = x 

    def __str__(self):
        return str(self.arr[:self.top+1])
    
# pop operation on stack

# removes an item from stack and the items are pushed in reversed order in which they are pushed if stack is empty then it causes underflow
# before removing it we have to check if our stack is empty or not, if it is empty then it underflow happens and we cannot remove the element
# if stack is not empty then we remove the top most element and decrement our top by 1
# for that we have to look at the isEmpty function first and then perform pop
    def isEmpty(self):
        return self.top == -1
    
    def pop(self):
        if self.isEmpty():
            print("stack underflow")
            return
        val = self.arr[self.top]
        self.top -= 1
        return val
    
# checking the top element of stack 
# if stack is empty then top position would be -1 or else we see what is top element

    def peek(self):
        if self.isEmpty():
            print("the stack is empty ! so no top element")
            return -1

        return self.arr[self.top]
    
    def isFull(self):
        if self.top == self.capacity - 1:
            return True
        
        return False
    

st = myStack(6)
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
print(st.isFull())

# the outputs are :
# [3]
# [3, 4]
# [3, 4, 5]
# [3, 4, 5, 3]
# 3
# [3, 4, 5]
# 5
# [3, 4]
# 4
# [3]
# 3
# []
# True
# stack underflow
# None
# [8]
# [8, 2]
# [8, 2, 4]
# [8, 2, 4, 1]
# [8, 2, 4, 1, 7]
# [8, 2, 4, 1, 7, 6]
# 6
# True