# lets implement stack using dynamic array which also list in python, no fixed capacity so no overflow issue as well

class myStack:
    def __init__(self):
        self.arr = []

    def push(self,x):
        self.arr.append(x)

    def pop(self):
        if not self.arr:
            print('stack underflow')
            return -1
        return self.arr.pop()
    
    def peek(self):
        if not self.arr:
            print('stack is empty, nothing to peek')
            return -1
        
        return self.arr[-1]
    
    def isEmpty(self):
        return len(self.arr)==0
    
    def size(self):
        return len(self.arr)
    
    def __str__(self):
        return str(self.arr)
    

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
# -1
# [8]
# [8, 2]
# [8, 2, 4]
# [8, 2, 4, 1]
# [8, 2, 4, 1, 7]
# [8, 2, 4, 1, 7, 6]
# 6