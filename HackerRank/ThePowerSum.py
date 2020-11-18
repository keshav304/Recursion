# Question :- https://www.hackerrank.com/challenges/the-power-sum/problem
from math import pow, floor


def powerSum(arr, X, N, index):
    # base conditions
    if X <= 0:
        return 1
    #return 0 if index goes out of range of arr
    if index >= len(arr):
        return 0
    
    ways = powerSum(arr, X, N, index + 1) + powerSum(arr, (X - pow(arr[index], N)), N, index + 1)
           #if the element is not added     #if the element is added
    return ways


X = int(input("Enter X"))
N = int(input("Enter N"))
arr = []
limit = floor(pow(X, 1 / N))
# the numbers whose powers is taken will less the Nth root Of X
for i in range(1, limit + 1):
    arr.append(i)
no_of_ways = powerSum(arr, X, N, index=0)
print("No of ways", no_of_ways)
