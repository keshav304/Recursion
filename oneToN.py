# Printing from one to N using Recursion
def printn(n):

    # Base Condition
    if n == 1:
        return 1
    else:
        # Hypothesis
        print(n)
        # Induction
        return printn(n - 1)


print(printn(10))
