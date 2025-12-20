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