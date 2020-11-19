# Printing from one to N using Recursion
def printn(n):
    # Base Condition
    if n == 1:
        print("1")
    else:
        # Induction
        printn(n - 1)

        # Hypothesis
        print(n)


printn(10)
