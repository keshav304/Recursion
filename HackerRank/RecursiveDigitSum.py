# Recursive Digit Sum :- https://www.hackerrank.com/challenges/recursive-digit-sum/problem
"""
The Trick in the the problem is instead of finding super digit for string of length n*k
find the super digit for n and multiply the result with k and if the result is less than 10
return it and if the result is more than 10 just call the the function again on the new output
"""


def superDigit(n, k):
    def sum_digit(v):
        if v < 10:
            return v
        else:
            x = sum(int(i) for i in str(v))
            return sum_digit(x)

    s = sum_digit(int(n))
    return sum_digit(s * k)


nk = input("Input:--").split()

n = nk[0]

k = int(nk[1])
result = superDigit(n, k)
print(result)
