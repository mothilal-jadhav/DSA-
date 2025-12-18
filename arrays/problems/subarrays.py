# Given an array arr[], the task is to generate all the possible subarrays of the given array

# def sub_arr(arr):
#     n = len(arr)
#     res = []
#     for i in range(n):
#         for j in range(i+1, n+1):
#             res.append(arr[i:j])
#     return res
        

# print(sub_arr([1,2,3,4,5,6])) this is a naive approach lets solve in recursive way

# in recursive way we use two pointers start and end to maintain starting and ending point of array and we 
# stop if we reached the end of array 
# increment the end index if start has become more bigger than end 
# print the subarr from index start to end and increment starting index

def sub_arr(arr,start,end):

    if end == len(arr):
        return

    if start > end :
        return sub_arr(arr,0,end+1)
    
    else:
        print(arr[start:end+1])
        return sub_arr(arr,start+1,end)
    

arr = [1,2,3,4,5]
print(sub_arr(arr,0,0))