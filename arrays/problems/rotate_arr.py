# Types of Rotations in Array

# 1. Right Rotation (or Clockwise) -> arr = [1,2,3,4,5,6] ---> [5,6,1,2,3,4] after right rotation by two position
# 2. Left Rotation (Or Counter Clockwise) -> arr = [1,2,3,4,5,6] ---> [3,4,5,6,1,2] after left rotation by two position

def right_rotate(arr,d):
    n = len(arr)
    d = d%n

    # first reverse whole array 

    arr.reverse()

    # now reverse first d elements which will be my given value for rotations

    arr[:d] = reversed(arr[:d])

    # now reverse the next n-d elements

    arr[d:] = reversed(arr[d:])

    return arr

arr = [1,2,3,4,5,6]

print(right_rotate(arr,3))

def left_rotate(arr,d):
    n = len(arr)
    d = d%n

    # reverse whole array

    arr.reverse()

    # reverse first n-d elements

    arr[:n-d] = reversed(arr[:n-d])

    # reverse last d elements

    arr[n-d : ] = reversed(arr[n-d:])

    return arr

arr1 = [1, 2, 3, 4, 5, 6]
print(left_rotate(arr1,2))