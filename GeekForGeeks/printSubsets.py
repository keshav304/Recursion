# Problem :- https://practice.geeksforgeeks.org/problems/power-set-using-recursion/1/?track=sp-recursion&batchId=105
def powerSet(string, output=""):
    if len(string) <= 0:
        arr = [output]
        return arr

    output1 = output
    output2 = list(output)
    output2.append(string[0])
    output2 = "".join(output2)

    string = string[1:]
    
    arr = []
    # Element not included so main arr not updated and string also became shorter
    arr.extend(powerSet(string, output1))
    # Element included so main arr updated to new array and string also became shorter
    arr.extend(powerSet(string, output2))
    
    return arr


# Driver code
s = input("Enter the strings")
array = powerSet(s)
print(sorted(array))

