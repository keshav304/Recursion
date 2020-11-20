# Problem :- https://practice.geeksforgeeks.org/problems/power-set-using-recursion/1/?track=sp-recursion&batchId=105
def powerSet(string, output=""):
    if len(string) <= 0:
        arr = []
        arr.append(output)
        return arr
    output1 = output
    output2 = list(output)
    output2.append(string[0])
    output2 = "".join(output2)
    string = string[1:]
    arr = []
    arr.extend(powerSet(string, output1))
    arr.extend(powerSet(string, output2))
    return arr


# Driver code
string = input("Enter the strings")
arr = powerSet(string)
print(sorted(arr))
