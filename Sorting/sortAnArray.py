# Sorting a Array using Recursion
def insert(arr, temp):
    print("insert",arr, temp)
    # arr is sorted
    # base condition
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return arr
    """
    remove the last element and insert the temporary element in the smaller array
    and then add the removed elements after the temprorary element 
    """

    val = arr.pop()
    arr = insert(arr, temp)
    arr.append(val)
    return arr


def sort(arr):
    # base condition
    if len(arr) == 1:
        return arr
    # remove the last element
    temp = arr.pop()
    print("sort", arr, temp)
    # sort the rest of the array
    sort(arr)
    # inserting the removed elements at correct position in the sorted array
    arr_sorted = insert(arr, temp)
    return arr_sorted


arr_unsorted = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Unsorted array", arr_unsorted)
print("Sorted array", sort(arr_unsorted))
