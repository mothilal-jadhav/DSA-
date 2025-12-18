# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.

# this can be solved using hashmap

def remove_duplicates(arr):
    seen = set()
    res = []

    for i in arr:
        if i not in seen:
            seen.add(i)
            res.append(i)

    return res

arr = [3,4,4,6,6,9]
print(remove_duplicates(arr))

# time complexity will be O(n) and space complexity will be O(n)

# for sorted array we dont need any hashset

def remove_dup(array):
    n = len(array)

    if n<=1:
        return n
    
    real = [array[0]]
    for i in range(1,n):
        if array[i] != array[i-1]:
            real.append(array[i])


    return real
print(remove_dup(arr))