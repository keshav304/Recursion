# Problem :- https://practice.geeksforgeeks.org/problems/tower-of-hanoi/0#

def tower(n, source, destination, helper):
    # Base Condition
    if n == 1:
        print(f"move disk 1 from {source} to {destination}")
        return
    # Move top n-1 disks from source to helper rod
    tower(n - 1, source, helper, destination)
    # Move bottom-most disk to destination tower
    print(f"move disk {n} from {source} to {destination}")
    # Now move n-1 disks from helper tower to destination tower
    tower(n - 1, helper, destination, source)


testCases = int(input())
for i in range(testCases):
    noOfDiscs = int(input("No of Discs"))
    source = 1
    helper = 2
    destination = 3
    tower(noOfDiscs, source, destination, helper)
    # Number of steps
    print(2 ** noOfDiscs - 1)
