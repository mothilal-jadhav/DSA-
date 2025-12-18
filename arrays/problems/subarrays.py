# Given an array arr[], the task is to generate all the possible subarrays of the given array

def sub_arr(arr):
    n = len(arr)
    res = []
    for i in range(n):
        for j in range(i+1, n+1):
            res.append(arr[i:j])
    return res
        

print(sub_arr([1,2,3,4,5,6]))