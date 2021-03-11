def maxSum(list1):
    return sum(max(list1, key = sum))

list1 = [[1,2,3], [5,7,6], [3, 2, 3]]

print(maxSum(list1))