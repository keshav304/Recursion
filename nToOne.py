# Printing from one to N using Recursion
def printn(n):
    # Base Condition
    if n == 1:
        print("1")
    else:
        # Hypothesis - deciding signature of the function
        print(n)
        # Induction
        printn(n - 1)


printn(10)
