# Question :- https://www.hackerrank.com/challenges/the-power-sum/problem
from math import pow, floor


def powerSum(X, N, counter=1):
    """
    counter is kind of iterative value for which we are checking if solution is
    possible for this value and subtraction is to reduce computation and divide it 
    to subproblems as much as possible because that particular value is going to be 
    checked in next recursion call
    """
    if pow(index,N)<X:
        return powerSum(X,N,index+1)+powerSum(X-pow(index,N),N,index+1)
    elif pow(index,N)==X:
        return 1
    
    else:
        return 0


X = int(input("Enter X"))
N = int(input("Enter N"))
no_of_ways = powerSum(X, N)
print("No of ways", no_of_ways)
